# Speech-to-Text Django Project

## Structure
```
speech_to_text_project/
├── manage.py
├── requirements.txt
├── db.sqlite3                (created after first migrate)
├── speech_to_text_project/   # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── transcriber/               # The app
    ├── nlp_model.py           # <-- PASTE YOUR NLP CODE HERE
    ├── views.py                # handles the /transcribe/ endpoint
    ├── urls.py
    └── templates/transcriber/index.html   # the frontend page
```

## 1. Install dependencies
```bash
pip install -r requirements.txt
```
Add whatever libraries your NLP project needs (whisper, torch, speechrecognition, etc.) to `requirements.txt`, then reinstall.

## 2. Plug in your NLP project
Open `transcriber/nlp_model.py`. There is a single function:

```python
def transcribe_audio(audio_path: str) -> dict:
    # PASTE YOUR CODE HERE
    return {
        "language": ...,
        "transcript": ...,
        "translation": ...,
    }
```

Paste your model-loading/inference code inside that function (or import it and call it from there). It receives the path to the recorded audio file on disk and must return a dict with `language`, `transcript`, and `translation` keys — those three values are what get displayed on the page.

## 3. Run the project
```bash
python manage.py migrate
python manage.py runserver
```
Then open **http://127.0.0.1:8000/** in your browser.

## How it works
- The page has a **Recording Start/stop** button. Clicking it uses the browser's microphone (via `MediaRecorder`, plain JavaScript — no frameworks) to record audio.
- Clicking it again stops the recording and automatically uploads the audio to the Django endpoint `/transcribe/`.
- The Django view saves the audio temporarily, calls `transcribe_audio()` from `nlp_model.py`, deletes the temp file, and returns JSON with `language`, `transcript`, and `translation`.
- The page fills those into the "Language detected", "transcript", and "translation" boxes.
- **restart** clears everything on the page back to blank.

## Notes
- The frontend has **no CSS** (plain unstyled HTML, matching your blueprint) and only the minimal JavaScript needed for mic recording and calling the backend — there's no way to record live audio from a webpage using HTML alone.
- The `@csrf_exempt` decorator on `transcribe_view` is there to keep things simple for local development. If you deploy this publicly, replace it with proper CSRF handling (e.g. fetch a CSRF token and send it in the request header).
- Recorded audio is saved in `audio/webm` format by the browser. If your NLP code needs a different format (e.g. `.wav`), convert it inside `transcribe_audio()` (e.g. with `pydub` or `ffmpeg`) before running inference.
