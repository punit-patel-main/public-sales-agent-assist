import streamlit as st
import tempfile
import base64
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_segments(interval_in_seconds, temp_audio_path):
    try:
        audio = AudioSegment.from_file(temp_audio_path)
        duration_ms = len(audio)
        interval_ms = int(interval_in_seconds * 1000)
        overlap_ms = 5000  # 5 seconds
        suffix = f".{temp_audio_path.split('.')[-1]}"

        if interval_ms <= overlap_ms:
            raise ValueError("interval_ms must be greater than overlap_ms")

        # Step 1: Create list of (index, start_ms, end_ms)
        segments_info = []
        start_ms = 0
        index = 0

        while start_ms < duration_ms:
            end_ms = min(start_ms + interval_ms, duration_ms)
            segments_info.append((index, start_ms, end_ms))
            if end_ms == duration_ms:
                break
            start_ms = end_ms - overlap_ms
            index += 1

        # Step 2: Define segment export function
        def export_segment(index, start, end):
            segment = audio[start:end]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                segment.export(tmp_file.name, format=suffix[1:])
                return index, tmp_file.name

        # Step 3: Process in parallel
        segment_dict = {}
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(export_segment, idx, start, end) for idx, start, end in segments_info]
            for future in as_completed(futures):
                idx, path = future.result()
                segment_dict[idx] = path

        # Step 4: Create ordered list
        ordered_segments = [segment_dict[i] for i in sorted(segment_dict.keys())]
        st.session_state["audio_segments"] = ordered_segments
        return ordered_segments

    except Exception as e:
        st.error(f"Error splitting audio: {str(e)}")
        return []

def get_audio_base64(file_path):
    """Convert audio file to base64 for HTML audio player"""
    try:
        with open(file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            encoded = base64.b64encode(audio_bytes).decode()
            return encoded
    except Exception as e:
        st.error(f"Error encoding audio: {str(e)}")
        return None

def get_audio_duration(audio_file):
    audio = AudioSegment.from_file(audio_file)
    return round(len(audio) / 1000.0, 2)  # Convert from milliseconds to seconds