import streamlit as st
import time
import os
import tempfile
import shutil

from getSuggestions import call_gemini_with_audio
from getSuggestions import get_suggestions
from audioManipulations import get_segments, get_audio_duration, get_audio_base64
from getWaves import get_wave_loader
import samples

# st.set_page_config(layout='wide')

def main():
    selected_option = st.sidebar.radio(
        "Do you have a call & knowledge base to try the app?",
        ("Yes", "No, I need a sample"),
        index=0, # Option A is selected by default
        key="sidebar_radio"
    )

    if selected_option == 'No, I need a sample':
        st.subheader('Sample to try the app.')
        samples.main()

    else:
        st.title('Agent Assist')
        # Initialize session state
        if 'uploaded_file' not in st.session_state:
            st.session_state.uploaded_file = None
        if 'knowledge_base' not in st.session_state:
            st.session_state.knowledge_base = ""
        if 'demo_started' not in st.session_state:
            st.session_state.demo_started = False
        if 'start_time' not in st.session_state:
            st.session_state.start_time = None
    
        if 'suggestions' not in st.session_state:
            st.session_state.suggestions = []
        if 'transcript' not in st.session_state:
            st.session_state.transcript = ""
    
        if 'segments_of_audio' not in st.session_state:
            st.session_state.segments_of_audio = []
        if 'audio_duration' not in st.session_state:
            st.session_state.audio_duration = 0
        if 'last_suggestion_interval' not in st.session_state:
            st.session_state.last_suggestion_interval = 0
    
        # Update interval duration here
        if 'interval_in_seconds' not in st.session_state:
            st.session_state.interval_in_seconds = 45
        
        # Phase 1: File Upload
        if st.session_state.uploaded_file is None:
            
            uploaded_file = st.file_uploader(
                "Upload audio file of a call here.",
                type=['m4a', 'mp3', 'wav'],
                help="Upload the sales call recording to analyze"
            )
            
            if uploaded_file is not None:
                st.session_state.uploaded_file = uploaded_file
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{uploaded_file.name.split(".")[-1]}') as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    st.session_state.temp_audio_path = tmp_file.name
    
                    # Create audio segments as per interval
                    if not st.session_state.segments_of_audio:
                        st.session_state.segments_of_audio = get_segments(st.session_state.interval_in_seconds, st.session_state.temp_audio_path)
    
                        # # Define the destination folder
                        # destination_folder = os.path.join(os.getcwd(), "stored_audio")
                        # os.makedirs(destination_folder, exist_ok=True)
    
                        # # Copy and rename each audio file
                        # for idx, audio_path in enumerate(st.session_state.segments_of_audio):
                        #     if os.path.exists(audio_path):
                        #         # Preserve original file extension
                        #         extension = os.path.splitext(audio_path)[1]
                        #         new_filename = f"{idx}{extension}"
                        #         new_path = os.path.join(destination_folder, new_filename)
                        #         shutil.copy(audio_path, new_path)
                        #     else:
                        #         st.warning(f"File not found: {audio_path}")
                
                # Get audio duration (simplified estimation)
                st.session_state.audio_duration = get_audio_duration(st.session_state.temp_audio_path)
                st.rerun()
        
        # Phase 2: Knowledge Base Input and Start Demo Button
        elif st.session_state.uploaded_file is not None and not st.session_state.demo_started:
            st.success("✅ Audio file uploaded successfully!")
            
            # Knowledge Base Input
            st.markdown("### 📚 Knowledge Base")
            knowledge_base = st.text_area(
                "Enter your knowledge base information:",
                value=st.session_state.knowledge_base,
                height=150,
                placeholder="Enter product information, company policies, FAQs, or any relevant knowledge that the AI should use for suggestions...",
                help="This information will be used by the AI to provide contextual suggestions during the call."
            )
            
            if knowledge_base != st.session_state.knowledge_base:
                st.session_state.knowledge_base = knowledge_base
            
            # Start Demo Button
            # st.markdown('<div style="text-align: center; margin: 20px 0;">', unsafe_allow_html=True)
            # if st.button("🚀 Start Demo", type="primary", use_container_width=True):
            if st.button("🚀 Start Demo"):
                if st.session_state.knowledge_base.strip():
                    st.session_state.demo_started = True
                    # st.session_state.start_time = time.time() + 3
                    st.session_state.suggestions = []
                    st.session_state.last_suggestion_interval = 0
                    st.rerun()
                else:
                    st.error("Please enter knowledge base information before starting the demo.")
            st.markdown('</div>', unsafe_allow_html=True)
                
        # Phase 3: Demo Running
        elif st.session_state.demo_started:
            
            # Hidden audio player for auto-play (no controls shown)
            if 'audio_player_added' not in st.session_state:
                st.session_state.audio_player_added = True
                
            # Determine audio file type for proper MIME type
            file_extension = st.session_state.uploaded_file.name.split('.')[-1].lower()
            if file_extension == 'm4a':
                audio_type = "audio/mp4"
            elif file_extension == 'mp3':
                audio_type = "audio/mpeg"
            elif file_extension == 'wav':
                audio_type = "audio/wav"
            else:
                audio_type = "audio/mpeg"
                
            # Create hidden auto-play audio (no visible controls)
            audio_html = f"""
            <audio autoplay style="display: none;">
                <source src="data:{audio_type};base64,{get_audio_base64(st.session_state.temp_audio_path)}" type="{audio_type}">
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
            
            # # Top control bar with stop button and wave animation
            # col1, col2 = st.columns([1, 4])
            
            # with col1:
            #     if st.button("⏹️ Stop Demo", type="secondary"):
            #         st.session_state.demo_started = False
            #         st.session_state.suggestions = []
            #         st.session_state.audio_player_added = False
            #         st.session_state.transcript = ""
            #         # Clean up temp files
            #         if hasattr(st.session_state, 'temp_audio_path'):
            #             try:
            #                 os.unlink(st.session_state.temp_audio_path)
            #             except:
            #                 pass
            #         st.rerun()
            
            # with col2:
            st.markdown(get_wave_loader(), unsafe_allow_html=True)
    
            if not st.session_state.start_time:
                st.session_state.start_time = time.time() + 10
    
            # Calculate elapsed time
            elapsed_time = time.time() - st.session_state.start_time
                    
            # Check if we need to generate new suggestion
            current_interval = int(elapsed_time // st.session_state.interval_in_seconds)
    
            if current_interval > st.session_state.last_suggestion_interval and elapsed_time >= st.session_state.interval_in_seconds:
    
                audio_segment_path = st.session_state.segments_of_audio[current_interval - 1]
    
                if audio_segment_path:
                    # Get new suggestion with knowledge base
                    new_suggestion, transcript = get_suggestions(
                        audio_segment_path,
                        st.session_state.transcript,
                        st.session_state.suggestions,
                        st.session_state.knowledge_base
                    )
    
                    st.session_state.suggestions.append(new_suggestion)
                    st.session_state.transcript += transcript
                    st.session_state.last_suggestion_interval = current_interval
                    
                    # No need to clean up since we're using the original file
            # Display current suggestions (Full Width)
            if st.session_state.suggestions:
    
                # st.subheader('Transcript')
                # st.write(st.session_state.transcript)
    
                current_suggestion = st.session_state.suggestions[-1]
    
                # suggestion_blocks = ""
                # for item in current_suggestion:
                #     # talked_about = item['talked_about']
                #     suggestion = item['suggestion']
    
                #     suggestion_blocks += f"""
                #         <div style="background: #f8f9fa; border-left: 4px solid #1f77b4; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                #             <div style="color: #1f77b4; font-size: 16px; font-weight: 500;">
                #                 <strong>💡:</strong> {suggestion}
                #             </div>
                #         </div>
                #     """
    
                # st.markdown(suggestion_blocks, unsafe_allow_html=True)
            
                suggestion_blocks = ""
                for item in current_suggestion:
                    suggestion = item['suggestion']
                    
                    suggestion_blocks += f"""
                        <div style="
                            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%); 
                            border: 1px solid #e2e8f0; 
                            padding: 20px 24px; 
                            margin: 16px 0; 
                            border-radius: 12px; 
                            box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
                            transition: all 0.2s ease;
                            position: relative;
                            overflow: hidden;
                        ">
                            <div style="
                                position: absolute;
                                left: 0;
                                top: 0;
                                bottom: 0;
                                width: 3px;
                                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            "></div>
                            <div style="
                                color: #334155; 
                                font-size: 15px; 
                                font-weight: 500;
                                line-height: 1.6;
                                letter-spacing: -0.01em;
                            ">
                                {suggestion}
                            </div>
                        </div>
                    """
                
                st.markdown(suggestion_blocks, unsafe_allow_html=True)
    
            else:
                st.info("🔄 Analyzing conversation and generating AI suggestions...")
            
            # Auto-refresh every second
            time.sleep(1)
            st.rerun()

if __name__ == "__main__":
    main()
