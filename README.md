# Speech to Text and Translation Web Application

A Django-based Speech-to-Text web application that records audio directly from the user's microphone, processes the recorded speech using a Faster-Whisper NLP model, generates a text transcript, and provides an English translation.

The application provides a simple web interface where users can start and stop microphone recording, submit the recorded audio to the Django backend, process the audio using the NLP model, and display the detected language, original transcript, and English translation.

The project is designed as a practical implementation of Natural Language Processing, speech recognition, audio processing, and Django web development.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Project Architecture](#project-architecture)
* [Application Workflow](#application-workflow)
* [Technologies Used](#technologies-used)
* [Structure](#project-structure)
* [Requirements](#requirements)
* [Django Setup](#django-setup)
* [Running the Application](#running-the-application)
* [Using the Application](#using-the-application)
* [NLP Model](#nlp-model)
* [Speech Recognition Process](#speech-recognition-process)
* [Translation](#translation)
* [Database](#database)
* [Saving Transcripts](#saving-transcripts)
* [Frontend](#frontend)
* [Backend](#backend)
* [API and Request Flow](#api-and-request-flow)
* [Important Files](#important-files)
* [Configuration](#configuration)
* [Troubleshooting](#troubleshooting)
* [Common Errors](#common-errors)
* [Development Notes](#development-notes)
* [Future Improvements](#future-improvements)
* [Limitations](#limitations)
* [Security Considerations](#security-considerations)
* [Learning Outcomes](#learning-outcomes)
* [Conclusion](#conclusion)

---

# Project Overview

The Speech to Text and Translation Web Application is a web-based NLP project developed using Django.

The main purpose of the project is to convert spoken audio into written text.

Instead of requiring users to upload an audio file manually, the application uses the browser's microphone to record speech.

The recorded audio is then sent to the Django backend, where it is processed by the Faster-Whisper speech recognition model.

The model produces:

1. Detected language
2. Original speech transcript
3. English translation

The results are then returned to the browser and displayed on the webpage.

The application can also store transcription results in an SQLite database for future access and transcription history.

---

# Features

## 1. Microphone Recording

The application can access the user's microphone through the browser.

The user can start and stop recording directly from the website.

The browser handles microphone access using the Web Media API.

---

## 2. Speech-to-Text Conversion

Recorded speech is processed using Faster-Whisper.

The model analyzes the audio and converts spoken language into written text.

---

## 3. Automatic Language Detection

Faster-Whisper can detect the language spoken in the recorded audio.

The detected language is returned by the backend and displayed on the webpage.

---

## 4. English Translation

The application can translate supported spoken languages into English.

For example:

```text
Input Speech:
Namaste, mera naam Akshay hai.

Detected Language:
Hindi

Transcript:
Namaste, mera naam Akshay hai.

English Translation:
Hello, my name is Akshay.
```

---

## 5. Web-Based Interface

The application provides a simple browser-based interface.

The interface contains:

* Start Recording button
* Stop Recording functionality
* Restart button
* Recording status
* Detected language
* Transcript section
* Translation section

---

## 6. Django Backend

Django handles:

* HTTP requests
* Audio uploads
* NLP model execution
* Transcription processing
* Translation
* Database operations
* JSON responses

---

## 7. SQLite Database

The project uses SQLite as the default Django database.

Transcription information can be stored in the database, including:

* Detected language
* Original transcript
* English translation
* Creation date and time

---

# Project Architecture

The application follows a client-server architecture.

```text
                User
                 |
                 v
        Web Browser
                 |
                 | Microphone
                 v
        Audio Recording
                 |
                 | HTTP POST
                 v
        Django Backend
                 |
                 v
       Audio Processing
                 |
                 v
        Faster-Whisper
                 |
          +------+------+
          |             |
          v             v
     Transcript     Translation
          |             |
          +------+------+
                 |
                 v
          SQLite Database
                 |
                 v
          JSON Response
                 |
                 v
          Web Interface
```

---

# Application Workflow

The complete application workflow is:

```text
1. User opens the website
        |
2. User clicks Start Recording
        |
3. Browser requests microphone permission
        |
4. Browser records microphone audio
        |
5. User clicks Stop Recording
        |
6. Audio recording is converted into a Blob
        |
7. JavaScript sends audio to Django
        |
8. Django receives the audio
        |
9. Audio is temporarily stored
        |
10. Faster-Whisper processes the audio
        |
11. Speech is converted to text
        |
12. Language is detected
        |
13. Speech is translated into English
        |
14. Result is saved to SQLite
        |
15. Django returns JSON response
        |
16. JavaScript displays the result
```

---

# Technologies Used

## Programming Language

Python

Python is used for:

* Django backend
* NLP model processing
* Audio processing
* Database operations

---

## Web Framework

Django

Django is responsible for the backend web application.

---

## NLP Model

Faster-Whisper

Faster-Whisper is an optimized implementation of OpenAI Whisper using CTranslate2.

It is used for:

* Speech recognition
* Language detection
* Speech translation

---

## Frontend

The frontend uses:

* HTML
* CSS
* JavaScript

JavaScript is responsible for microphone recording and sending audio to Django.

---

## Database

SQLite

SQLite is used as the default database for storing application data and transcription history.

---

## Development Tools

The project can be developed using:

* Visual Studio Code
* Python
* Django
* Git
* GitHub
* Browser Developer Tools

---

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

The exact structure may differ depending on the final version of the project.

---

# Requirements

Before installing the project, make sure the system has:

* Python 3.12 or compatible Python version
* pip
* Git
* A modern web browser
* Working microphone
* Internet connection for initial model download

Recommended browsers include:

* Google Chrome
* Microsoft Edge
* Mozilla Firefox

---

# Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If a requirements file is not available, install the main dependencies manually:

```bash
pip install django
pip install faster-whisper
```

Additional audio-related dependencies may be required depending on the implementation.

---

# Django Setup

After installing dependencies, move into the directory containing `manage.py`.

Run:

```bash
python manage.py migrate
```

This creates the default Django database tables.

If a custom `Transcript` model has been added, run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

The terminal should display something similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

# Using the Application

## Step 1: Open the Website

Open:

```text
http://127.0.0.1:8000/
```

---

## Step 2: Allow Microphone Access

When the browser asks for microphone permission, select:

```text
Allow
```

The application cannot record audio if microphone access is blocked.

---

## Step 3: Start Recording

Click:

```text
Start Recording
```

The browser begins recording audio from the selected microphone.

---

## Step 4: Speak

Speak normally into the microphone.

For example:

```text
Hello, this is a speech to text application.
```

---

## Step 5: Stop Recording

Click:

```text
Stop Recording
```

The recorded audio is sent to the Django backend.

---

## Step 6: Wait for Processing

Django processes the audio using Faster-Whisper.

The processing time depends on:

* Audio length
* Whisper model size
* CPU performance
* GPU availability
* System memory

---

## Step 7: View Results

The application displays:

```text
Language:
English

Transcript:
Hello, this is a speech to text application.

Translation:
Hello, this is a speech to text application.
```

---

# NLP Model

The core NLP functionality is implemented using Faster-Whisper.

Faster-Whisper is designed for efficient Whisper inference.

The model can perform automatic speech recognition and translation.

A typical configuration may look like:

```python
from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)
```

The model size can be changed according to the system's hardware.

Common model sizes include:

```text
tiny
base
small
medium
large
```

Larger models generally provide better recognition quality but require more computational resources.

---

# Speech Recognition Process

The basic transcription process is:

```python
segments, info = model.transcribe(
    audio_path,
    beam_size=5
)
```

The returned segments contain recognized speech.

The segments can then be combined into a complete transcript.

Conceptually:

```text
Audio
  |
  v
Whisper Model
  |
  v
Speech Segments
  |
  v
Combined Text
  |
  v
Transcript
```

---

# Translation

Faster-Whisper can also perform speech translation.

For example:

```python
segments, info = model.transcribe(
    audio_path,
    task="translate",
    beam_size=5
)
```

The translation task converts supported spoken languages into English.

Example:

```text
Original Speech:
Bonjour, comment allez-vous?

Translation:
Hello, how are you?
```

---

# Database

The project uses SQLite.

The database file is:

```text
db.sqlite3
```

SQLite is useful for this project because it does not require a separate database server.

Django communicates with SQLite through Django's ORM.

---

# Transcript Model

A transcript model can contain fields such as:

```python
class Transcript(models.Model):

    language = models.CharField(max_length=50)

    transcript = models.TextField()

    translation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
```

This allows each transcription to be stored as a separate database record.

Example database data:

```text
--------------------------------------------------------------
ID | Language | Transcript              | Translation
--------------------------------------------------------------
1  | en       | Hello everyone          | Hello everyone
2  | hi       | Mera naam XYZ hai   | My name is XYZ
3  | fr       | Bonjour tout le monde  | Hello everyone
--------------------------------------------------------------
```

---

# Saving Transcripts

When a transcription is successfully generated, Django can create a database record:

```python
Transcript.objects.create(
    language=result["language"],
    transcript=result["transcript"],
    translation=result["translation"]
)
```

The data is stored in:

```text
db.sqlite3
```

The database should not be edited manually.

Django migrations should be used to create and modify database tables.

---

# Frontend

The frontend consists of HTML, CSS, and JavaScript.

The main HTML template is:

```text
transcriber/templates/transcriber/index.html
```

The stylesheet is:

```text
transcriber/static/transcriber/style.css
```

The HTML loads the CSS using Django's static template tag:

```django
{% load static %}
```

and:

```html
<link rel="stylesheet" href="{% static 'transcriber/style.css' %}">
```

---

# Microphone Recording

The browser records audio using:

```javascript
navigator.mediaDevices.getUserMedia({
    audio: true
});
```

The `MediaRecorder` API is then used to record the audio.

Example:

```javascript
const stream =
    await navigator.mediaDevices.getUserMedia({
        audio: true
    });

const mediaRecorder =
    new MediaRecorder(stream);
```

The audio data is collected in chunks:

```javascript
mediaRecorder.ondataavailable = function(event) {
    audioChunks.push(event.data);
};
```

When recording stops, the chunks are combined:

```javascript
const audioBlob = new Blob(
    audioChunks,
    { type: "audio/webm" }
);
```

The resulting audio is then sent to Django.

---

# Backend

The Django backend receives the recorded audio through an HTTP POST request.

The JavaScript sends:

```javascript
const formData = new FormData();

formData.append(
    "audio",
    audioBlob,
    "recording.webm"
);
```

Then:

```javascript
fetch("/transcribe/", {
    method: "POST",
    body: formData
});
```

Django receives the uploaded audio and sends it to the NLP model.

---

# API and Request Flow

The application uses a Django endpoint for transcription.

Example endpoint:

```text
/transcribe/
```

The frontend sends:

```text
POST /transcribe/
```

with the recorded audio.

The backend processes the request and returns JSON.

Example response:

```json
{
    "language": "en",
    "transcript": "Hello, this is my project.",
    "translation": "Hello, this is my project."
}
```

JavaScript reads this response:

```javascript
.then(data => {
    document.getElementById("language").innerText =
        data.language;

    document.getElementById("transcript").innerText =
        data.transcript;

    document.getElementById("translation").innerText =
        data.translation;
});
```

---

# Important Files

## manage.py

The main Django command-line utility.

Used for:

```bash
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```

---

## settings.py

Contains the Django project configuration.

It controls:

* Installed applications
* Middleware
* Database
* Templates
* Static files
* Security settings
* Internationalization

---

## urls.py

Defines URL routing.

The main URL configuration connects application URLs to the Django project.

---

## views.py

Contains the request-handling logic.

The view can:

1. Receive the uploaded audio
2. Save the temporary audio
3. Call the NLP model
4. Save the result
5. Return a JSON response

---

## models.py

Contains Django database models.

The `Transcript` model defines the structure of transcription records.

---

## nlp_model.py

Contains the NLP and speech recognition logic.

This file is responsible for communicating with Faster-Whisper.

Keeping the model logic separate from the Django view makes the project easier to maintain.

---

## index.html

The main user interface.

It contains:

* Recording controls
* Status information
* Transcript display
* Translation display
* JavaScript microphone functionality

---

## style.css

Contains the visual styling for the web interface.

It controls:

* Layout
* Colors
* Buttons
* Result sections
* Spacing
* Responsive behavior

---

## db.sqlite3

The SQLite database file.

It stores Django database information and, after the transcript model is configured, transcription records.

---

# Configuration

Important Django configuration is located in:

```text
config/settings.py
```

The database configuration normally uses:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Static files are configured using:

```python
STATIC_URL = "static/"
```

Django automatically discovers static files inside installed applications when `django.contrib.staticfiles` is enabled.

---

# Troubleshooting

## Microphone Permission Error

If the application displays an error such as:

```text
Microphone access denied or unavailable
```

check:

1. Browser microphone permission
2. Windows microphone permission
3. Correct microphone device
4. Whether another application is using the microphone
5. Browser security settings

The browser should have permission to access the microphone.

---

## CSS Is Not Loading

Make sure the CSS file exists at:

```text
transcriber/static/transcriber/style.css
```

The HTML should contain:

```django
{% load static %}
```

and:

```html
<link rel="stylesheet"
      href="{% static 'transcriber/style.css' %}">
```

After making changes, refresh the browser using:

```text
Ctrl + F5
```

---

## Template Static Error

If Django reports:

```text
Invalid block tag: 'static'
```

make sure this appears at the top of the template:

```django
{% load static %}
```

---

## Django Server Does Not Start

Make sure the terminal is in the directory containing:

```text
manage.py
```

Then run:

```bash
python manage.py runserver
```

Do not run:

```bash
python runserver
```

---

## Python Command Not Found

Check the Python installation:

```bash
python --version
```

If Python is installed correctly, the command should return the installed Python version.

A common typing mistake is:

```text
pyhton
```

The correct command is:

```text
python
```

---

## Virtual Environment Activation Error

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If using Command Prompt:

```cmd
venv\Scripts\activate
```

---

## Migration Warning

If Django displays:

```text
You have unapplied migration(s)
```

run:

```bash
python manage.py migrate
```

For a newly created model:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Common Errors

## Error: App Name Conflicts With Existing Python Module

If Django reports that an app name conflicts with an existing Python module, use another app name.

For example:

```bash
python manage.py startapp transcriber
```

instead of using a conflicting name such as:

```bash
python manage.py startapp speech
```

---

## Error: 404 on `/transcribe/`

Check that the application URL configuration contains the correct route.

For example:

```python
path("transcribe/", views.transcribe_audio, name="transcribe")
```

Also make sure the application's URLs are included in the main project URL configuration.

---

## Error: NLP Model Not Found

Make sure Faster-Whisper is installed:

```bash
pip install faster-whisper
```

The first time a model is used, the required model files may need to be downloaded.

---

# Development Notes

The project separates responsibilities into different components.

The frontend is responsible for:

```text
User interaction
Microphone recording
Displaying results
```

Django is responsible for:

```text
Routing
File handling
Request processing
NLP integration
Database operations
```

The NLP module is responsible for:

```text
Audio processing
Speech recognition
Language detection
Translation
```

The database is responsible for:

```text
Persistent transcription records
```

This separation makes it easier to modify individual parts of the application without rewriting the complete project.

---

# Future Improvements

The project can be extended with several additional features.

## 1. Transcription History

Create a dedicated history page that displays previous recordings.

Possible information:

```text
Date
Language
Transcript
Translation
```

---

## 2. Audio File Storage

Instead of processing only temporary audio files, recordings could optionally be stored for later playback.

---

## 3. Download Transcript

Allow users to download their transcription as:

```text
.txt
.docx
.pdf
```

---

## 4. User Authentication

Add Django authentication so each user has their own transcription history.

Possible features:

* Registration
* Login
* Logout
* User-specific history
* Password management

---

## 5. Multiple Translation Languages

The application can be extended to support translation into languages other than English.

For example:

```text
English
Hindi
French
German
Spanish
Japanese
```

---

## 6. Real-Time Transcription

The current implementation processes recorded audio after recording stops.

A future version could process audio continuously and display partial transcription results while the user is speaking.

---

## 7. Audio Playback

Add an audio player so users can listen to the original recording.

---

## 8. Searchable History

Users could search previous transcripts by:

* Keyword
* Language
* Date
* User

---

## 9. Improved UI

The frontend can be extended with:

* Recording timer
* Recording indicator
* Loading animation
* Better error messages
* Responsive mobile layout

---

## 10. GPU Acceleration

Faster-Whisper can be configured to use a compatible GPU to improve processing speed.

This can be useful when processing long recordings or multiple requests.

---

# Limitations

The current project has several limitations.

## Processing Time

Speech recognition can take time depending on the model size and hardware.

Larger models require more computational resources.

---

## Microphone Dependency

The browser must have access to a working microphone.

---

## Browser Permissions

Microphone access must be explicitly allowed by the user.

---

## Audio Format

The browser may produce audio in a format such as WebM.

The backend and NLP processing pipeline must support the received audio format.

---

## Local Development Server

The Django development server is intended for development and testing.

It should not be directly exposed as a production server.

---

# Security Considerations

Microphone data can contain sensitive information.

A production version of the application should consider:

* Secure HTTPS connections
* Authentication
* Authorization
* Secure file handling
* File size limits
* Input validation
* Temporary file cleanup
* CSRF protection
* Secure secret key management
* Database security
* Access control for transcription history

The Django development `SECRET_KEY` should never be committed publicly.

Production configuration should use environment variables or another secure configuration mechanism.

---

# Environment Variables

Sensitive configuration should not be placed directly in source code.

A `.env` file can be used for local development.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=True
```

A `.env.example` file can be committed to GitHub without containing real secrets:

```text
SECRET_KEY=
DEBUG=True
```

The actual `.env` file should be included in `.gitignore`.

---

# Git and GitHub

Before pushing the project to GitHub, make sure unnecessary or sensitive files are excluded.

A typical `.gitignore` should include:

```text
venv/
__pycache__/
*.pyc
.env
db.sqlite3
media/
*.log
```

Depending on the project's requirements, `db.sqlite3` may be committed for demonstration purposes, but it is generally better to exclude databases containing personal or production data.

---

# Testing

The application should be tested using different types of speech.

Recommended tests include:

## Test 1: English Speech

```text
Hello, my name is Akshay.
```

Expected result:

```text
Detected Language: English
Transcript: Hello, my name is Akshay.
```

---

## Test 2: Hindi Speech

Speak a Hindi sentence and verify that:

```text
Detected Language
```

is correctly identified and that the English translation is generated.

---

## Test 3: Short Recording

Record approximately 5 to 10 seconds.

Verify:

* Recording starts
* Recording stops
* Audio reaches Django
* NLP processing completes
* Transcript appears
* Translation appears

---

## Test 4: Long Recording

Record a longer speech sample and verify that the backend can process the complete audio.

---

## Test 5: Microphone Denied

Block microphone access and verify that the application displays an appropriate error message.

---

# Performance Considerations

Model performance depends on several factors:

```text
Model Size
    +
CPU/GPU
    +
RAM
    +
Audio Duration
    +
Compute Type
    =
Processing Time
```

For CPU-based systems, an optimized configuration such as:

```python
device="cpu"
compute_type="int8"
```

can reduce resource requirements.

The best model size depends on the hardware available.

---

# Learning Outcomes

This project demonstrates practical knowledge of several areas of software development and machine learning.

## Python

The project uses Python for backend and NLP development.

---

## Django

The project demonstrates:

* Django project structure
* Django applications
* URL routing
* Views
* Templates
* Static files
* Models
* Migrations
* Database integration
* HTTP requests
* JSON responses

---

## Natural Language Processing

The project demonstrates a practical NLP application using speech recognition and translation.

---

## Machine Learning Model Integration

The project demonstrates how a pre-trained NLP model can be integrated into a web application.

---

## Frontend Development

The project uses:

* HTML
* CSS
* JavaScript
* Browser APIs

---

## Database Management

The project demonstrates how Django ORM can be used to store transcription results in SQLite.

---

## API Communication

The project demonstrates communication between frontend JavaScript and the Django backend using HTTP POST requests and JSON responses.

---

# Conclusion

The Speech to Text and Translation Web Application combines web development, Natural Language Processing, audio processing, and database management into a single practical application.

The application allows a user to record speech through a browser microphone, send the recording to a Django backend, process the audio using Faster-Whisper, generate a transcript, translate the speech into English, and display the results on a web interface.

The project also provides a foundation for more advanced features such as user authentication, transcription history, downloadable transcripts, real-time transcription, multilingual translation, audio storage, and GPU acceleration.

The architecture is intentionally modular so that the frontend, Django backend, NLP model, and database can be developed and improved independently.

---

# Author

**Akshay Dhiman**

Speech-to-Text and Translation Web Application

Technologies:

```text
Python
Django
Faster-Whisper
HTML
CSS
JavaScript
SQLite
Natural Language Processing
```
---
