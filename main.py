import os
import time

import dotenv
import requests

dotenv.load_dotenv()
base_url = "https://api.assemblyai.com"

headers = {"authorization": os.getenv("ASSEMBLYAI_API_KEY")}

FILE_URL = "https://dn710604.ca.archive.org/0/items/flittlepigrobinson_2601_librivox/taleoflittlepigrobinson_01_potter_128kb.mp3"


PROMPT = """
Format financial figures using Euros, not dollars.
"""

config = {
    "audio_url": FILE_URL,
    "speech_models": ["universal-3-pro"],
    "speaker_labels": False,
    "language_detection": True,
    "prompt": PROMPT,
    "temperature": 0,
}


def main():
    url = base_url + "/v2/transcript"
    response = requests.post(url, json=config, headers=headers)

    transcript_id = response.json()["id"]
    polling_endpoint = base_url + "/v2/transcript/" + transcript_id

    while True:
        transcription_result = requests.get(polling_endpoint, headers=headers).json()
        transcription_text = transcription_result["text"]

        if transcription_result["status"] == "completed":
            print("Transcript Text:", transcription_text)
            break

        elif transcription_result["status"] == "error":
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        else:
            time.sleep(3)


if __name__ == "__main__":
    main()
