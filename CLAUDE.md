# CLAUDE.md

## Project Overview

A terminal-based video summarization tool for non-technical users. Extracts audio from videos, transcribes to text, and generates AI summaries.

**Target Users:** Non-technical users who want to summarize long informational videos
**Key Priorities:** Ease of use, ease of setup, accuracy of summaries

## Current Status

**Implemented:**
- ✅ Video-to-audio extraction (ffmpeg)
- ✅ Audio-to-text transcription (OpenAI Whisper API)
- ✅ Text-to-summary generation (OpenAI GPT-3.5-turbo)

## Architecture

**Self-contained Python script** using PEP 723 dependency management:
- No separate requirements.txt needed
- Auto-installs dependencies with `uv`
- Single executable file

**Pipeline:** `video.mp4 → audio/video_audio.wav → transcripts/video_transcript.txt → summaries/video_summary.txt`

## Setup

1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Set OpenAI API key: `export OPENAI_API_KEY=your_key_here`
3. Run: `./summarizer.py video.mp4`

## Usage

```bash
./summarizer.py video.mp4
./summarizer.py "path/to/video file.mov"
```

**Output files:**
- `audio/video_audio.wav` - Extracted audio (16kHz mono)
- `transcripts/video_transcript.txt` - Speech-to-text transcript
- `summaries/video_summary.txt` - AI-generated summary with key points and actionable items