# AssemblyAI Universal-3 Pro Sample

A simple Python example demonstrating how to transcribe audio using AssemblyAI's [Universal-3 Pro](https://www.assemblyai.com/universal-3-pro) speech model.

## What it does

This script sends an audio file to AssemblyAI's API for transcription using the Universal-3 Pro model. It includes:

- Automatic language detection
- Custom prompting to control transcription formatting
- Polling mechanism to wait for transcription completion

## Setup

1. Install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

2. Create a `.env` file with your AssemblyAI API key:

```
ASSEMBLYAI_API_KEY=your_api_key_here
```

3. Run the script:

```bash
uv run main.py
```

## Configuration

The script uses the following configuration options:

- `speech_models`: Uses the `universal-3-pro` model
- `language_detection`: Automatically detects the spoken language
- `prompt`: Custom instructions for formatting (e.g., using Euros instead of dollars)
- `temperature`: Set to 0 for deterministic output

## Learn more

- [Universal-3 Pro](https://www.assemblyai.com/universal-3-pro) - AssemblyAI's latest speech model
- [AssemblyAI Documentation](https://www.assemblyai.com/docs)
