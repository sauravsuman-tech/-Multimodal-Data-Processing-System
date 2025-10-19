from parsers import download_youtube_audio, transcribe_audio_file
from pathlib import Path
import tempfile

def transcribe_youtube(url: str):
    tmp = Path(tempfile.mkdtemp())
    download_youtube_audio(url, tmp)
    docs = transcribe_audio_file(tmp)
    try:
        tmp.unlink()
    except Exception:
        pass
    return docs
