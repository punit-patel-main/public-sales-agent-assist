import os
import random
import requests
import base64
import mimetypes
from typing import Optional, Dict, Any
import streamlit as st
import time
import ast
import json
import random
import shutil
import re

from dotenv import load_dotenv
load_dotenv()


def call_gemini_with_audio(system_prompt: str, user_prompt: str, audio_file_path: str) -> Dict[str, Any]:
    """
    Call Google's Gemini 2.5 Flash Preview model with audio input using randomly selected API keys.
    
    Args:
        system_prompt (str): System instruction for the model
        user_prompt (str): User's text prompt
        audio_file_path (str): Path to the audio file
        
    Returns:
        Dict[str, Any]: Response from the Gemini API or error information
        
    Raises:
        Exception: If all API keys are exhausted or other critical errors occur
    """
    
    # Define API keys
    GEMINI_API_KEYS = [
        os.getenv("GEMINI_API_KEY"),
        os.getenv("GEMINI_API_KEY_2"),
        os.getenv("GEMINI_API_KEY_3"),
        os.getenv("GEMINI_API_KEY_4"),
        os.getenv("GEMINI_API_KEY_5"),
        os.getenv("GEMINI_API_KEY_6"),
        os.getenv("GEMINI_API_KEY_7"),
        os.getenv("GEMINI_API_KEY_8")
    ]
    
    # Filter out None values (missing environment variables)
    valid_api_keys = [key for key in GEMINI_API_KEYS if key is not None]
    
    if not valid_api_keys:
        raise Exception("No valid API keys found in environment variables")
    
    # Shuffle the keys for random selection
    random.shuffle(valid_api_keys)
    
    # Prepare audio data
    try:
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
        
        # Get MIME type of the audio file
        mime_type, _ = mimetypes.guess_type(audio_file_path)
        if not mime_type or not mime_type.startswith('audio/'):
            mime_type = 'audio/mpeg'  # Default fallback
            
    except FileNotFoundError:
        raise Exception(f"Audio file not found: {audio_file_path}")
    except Exception as e:
        raise Exception(f"Error reading audio file: {str(e)}")
    
    # Prepare the request payload
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_prompt
                    },
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": audio_data
                        }
                    }
                ]
            }
        ],
        "systemInstruction": {
            "parts": [
                {
                    "text": system_prompt
                }
            ]
        },
        "generationConfig": {
            "temperature": 0.7,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 8192,
        }
    }
    
    # Try each API key until success or exhaustion
    last_error = None
    
    for i, api_key in enumerate(valid_api_keys):
        try:
            # Try different model names in order of preference
            model_names = [
                "gemini-2.5-flash-preview-05-20",           # Latest stable version
                "gemini-1.5-flash"           # Fallback to 1.5 if 2.5 not available
            ]
            
            # Set headers
            headers = {
                'Content-Type': 'application/json',
            }
            
            # Try each model with the current API key
            for model_name in model_names:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
                
                print(f"Attempting API call with key #{i+1}/{len(valid_api_keys)}, model: {model_name}")
                
                # Make the API request
                response = requests.post(url, json=payload, headers=headers, timeout=60)
                
                # Check if the response is successful
                if response.status_code == 200:
                    response_data = response.json()
                    
                    # Check if the response contains the expected content
                    if 'candidates' in response_data and len(response_data['candidates']) > 0:
                        print(f"✓ Success with API key #{i+1}, model: {model_name}")
                        print(response_data.get("usageMetadata", {}))
                        print('')
                        return {
                            'success': True,
                            'response': response_data,
                            'content': response_data['candidates'][0]['content']['parts'][0]['text'],
                            'api_key_used': i+1,
                            'model_used': model_name
                        }
                    else:
                        print(f"✗ API key #{i+1}, model {model_name} returned empty response")
                        continue  # Try next model
                        
                elif response.status_code == 404:
                    print(f"✗ Model {model_name} not found (404), trying next model...")
                    continue  # Try next model
                else:
                    print(f"✗ API key #{i+1}, model {model_name} failed with status code: {response.status_code}")
                    try:
                        error_detail = response.json()
                        print(f"Error details: {error_detail}")
                    except:
                        print(f"Error text: {response.text}")
                    continue  # Try next model
            
            # If we get here, all models failed for this API key
            last_error = f"API key #{i+1} - All models failed"
                
        except requests.exceptions.Timeout:
            print(f"✗ API key #{i+1} timed out")
            last_error = f"API key #{i+1} timed out"
            continue
            
        except requests.exceptions.RequestException as e:
            print(f"✗ API key #{i+1} request failed: {str(e)}")
            last_error = f"API key #{i+1} request error: {str(e)}"
            continue
            
        except Exception as e:
            print(f"✗ API key #{i+1} unexpected error: {str(e)}")
            last_error = f"API key #{i+1} unexpected error: {str(e)}"
            continue
    
    # All API keys exhausted
    raise Exception(f"All API keys exhausted. Last error: {last_error}")


def get_prompts(previous_suggestions, knowledge_base, transcript):
    system_prompt = '''
Your goal is to act as a real-time sales assistant. You will provide sales pitch suggestions to a human agent conversing with a customer.

You will receive the ongoing call's conversation history in two parts:
1.  **Transcript:** The transcript of the earlier portion of the call.
2.  **Audio file:** The audio of the recent part of the call.

Based on this information, and by referencing the **Knowledge Base** provided below, you must perform two critical tasks:

1.  **Summarize the recent conversation from the audio file:** Provide a concise summary of what was discussed in the provided audio file. This summary should capture the key points, customer's intent, and any questions or concerns raised.
2.  **Provide Sales Suggestions:** Analyze the *entire* conversation so far (combining the provided transcript and the summary of the recent audio), cross-reference it with the **Knowledge Base**, and offer concise suggestions to the sales agent. These suggestions should aim to:
    * Improve the sales pitch with relevant information.
    * Phrase the pitch more effectively.
    * Ensure the customer perceives value in the product.
    * Effectively handle any objections raised.
    * Each suggestion should be a single liner using just a few words which is easy to read for the sales agent while he is talking to the customre.

**Important:** You will also be given a list of suggestions previously provided. **Do not repeat any past suggestions.** All new suggestions must be concise and to the point.

---

**Knowledge Base about the company:**

    '''
    system_prompt += knowledge_base
    
    system_prompt += '''

---

**Response Format:**

Your response **must strictly adhere** to the following JSON format. **Do not include any additional text or formatting outside of this JSON structure (e.g., no "```json" at the beginning or end).**

```json
{    
    "suggestions": [
        {
            "suggestion": "A very short and concise suggestion (e.g., Pitch this plan, Ask about budget, Highlight XYZ benefit)."            
        },
        {
            "suggestion": ""
        }
    ],
    "summary_of_audio_file": "A concise summary of the key points discussed in the provided audio file. Focus on what was said and implied by the customer and agent."
}
    '''

    user_prompt = '''
You are provided with the following:
- Transcript (Transcript of the earlier part of the ongoing call)
- Audio file (This is an audio file of the recent part of the ongoing call, from which a summary is needed.)
- Suggestions that you have already made of a live call that is happening at the moment.

Give new suggestions & a **concise summary** of the provided audio file as per system instructions.

previous_suggestions:
    '''
    if previous_suggestions:
        for suggestion in previous_suggestions:
            user_prompt += '\n'
            user_prompt += str(suggestion)

    user_prompt += '''

    Transcript:
    '''

    user_prompt += transcript

    return system_prompt, user_prompt

def get_suggestions(audio_segment_path, transcript, previous_suggestions, knowledge_base):

    # Define the destination folder
    destination_folder = os.path.join(os.getcwd(), "stored_audio")
    os.makedirs(destination_folder, exist_ok=True)

    if os.path.exists(audio_segment_path):
        # Preserve original file extension
        extension = os.path.splitext(audio_segment_path)[1]
        random_number = random.randint(1, 10000)
        new_filename = f"{random_number}{extension}"
        print(new_filename)
        new_path = os.path.join(destination_folder, new_filename)
        shutil.copy(audio_segment_path, new_path)
    else:
        st.warning(f"File not found: {audio_segment_path}")
    
    system_prompt, user_prompt = get_prompts(previous_suggestions, knowledge_base, transcript)
    suggestion = call_gemini_with_audio(system_prompt, user_prompt, audio_segment_path)

    print('Parsed Suggestion:')
    print(suggestion)
    print('\n\n')

    content = suggestion['content']
    # Find JSON in the response
    start = content.find('{')
    end = content.rfind('}') + 1
    json_str = content[start:end]
    result = json.loads(json_str)

    new_suggestion = result['suggestions']
    transcript = result['summary_of_audio_file']
    transcript += '''

    '''

    print('Transcript:')
    print(transcript)
    print('')
    print('')

    return new_suggestion, transcript

