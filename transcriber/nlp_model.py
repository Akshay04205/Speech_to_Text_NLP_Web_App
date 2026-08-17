from faster_whisper import WhisperModel


# CHANGED: Load the Faster-Whisper model once when Django starts.
# Problem: Loading the model for every recording would be very slow.
# Fix: Keep one model in memory and reuse it.
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path: str) -> dict:

    # CHANGED: Transcribe the original spoken language.
    # This uses your existing Faster-Whisper approach.
    segments, info = model.transcribe(
        audio_path,
        beam_size=5
    )

    transcript = " ".join(
        segment.text for segment in segments
    ).strip()


    # CHANGED: Translate the same recording into English.
    # Faster-Whisper performs the translation when task="translate".
    translation_segments, _ = model.transcribe(
        audio_path,
        task="translate",
        beam_size=5
    )

    translation = " ".join(
        segment.text for segment in translation_segments
    ).strip()


    # CHANGED: Return the exact dictionary expected by views.py.
    return {
        "language": info.language,
        "transcript": transcript,
        "translation": translation,
    }