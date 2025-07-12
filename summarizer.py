#!/usr/bin/env -S uv run --refresh
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ffmpeg-python",
# ]
# ///

import os
import sys
import tempfile
from pathlib import Path
import ffmpeg

def is_video_file(file_path):
    """Check if file is a supported video format"""
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.m4v', '.webm'}
    return Path(file_path).suffix.lower() in video_extensions

def extract_audio_from_video(video_path, output_path=None):
    """
    Extract audio from video file using ffmpeg
    
    Args:
        video_path: Path to input video file
        output_path: Optional path for output audio file. If None, creates file in audio/ directory
    
    Returns:
        Path to extracted audio file
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    if not is_video_file(video_path):
        raise ValueError(f"File is not a supported video format: {video_path}")
    
    # Create output path if not provided
    if output_path is None:
        # Create audio directory in same location as script
        script_dir = Path(__file__).parent
        audio_dir = script_dir / "audio"
        audio_dir.mkdir(exist_ok=True)
        
        # Create filename based on original video name
        video_name = Path(video_path).stem
        output_path = audio_dir / f"{video_name}_audio.wav"
    
    print(f"Extracting audio from: {video_path}")
    print(f"Output audio file: {output_path}")
    
    try:
        # Use ffmpeg to extract audio
        # -ac 1: mono audio (reduces file size, sufficient for speech)
        # -ar 16000: 16kHz sample rate (good for speech recognition)
        # -f wav: output format
        (
            ffmpeg
            .input(video_path)
            .output(str(output_path), ac=1, ar=16000, f='wav')
            .overwrite_output()
            .run(quiet=True)
        )
        
        print(f"Audio extraction completed: {output_path}")
        return output_path
        
    except ffmpeg.Error as e:
        print(f"Error extracting audio: {e}")
        # Clean up output file if it was created but extraction failed
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except:
                pass
        raise

def main():
    """Main function for testing video-to-speech extraction"""
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <video_file>")
        print("Example: python summarizer.py video.mp4")
        sys.exit(1)
    
    video_path = sys.argv[1]
    
    try:
        audio_path = extract_audio_from_video(video_path)
        print(f"Success! Audio extracted to: {audio_path}")
        
        # For now, just show file info
        audio_size = os.path.getsize(audio_path)
        print(f"Audio file size: {audio_size / 1024 / 1024:.2f} MB")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()