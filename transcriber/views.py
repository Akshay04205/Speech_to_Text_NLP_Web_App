import os
import uuid

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .nlp_model import transcribe_audio


def index(request):
    """Render the single-page frontend."""
    return render(request, "transcriber/index.html")


@csrf_exempt  # simplest option for a local/demo project; see note in README
@require_POST
def transcribe_view(request):
    """
    Receives an uploaded audio file (field name: 'audio'),
    saves it temporarily, runs it through transcribe_audio(),
    and returns the result as JSON.
    """
    audio_file = request.FILES.get("audio")
    if not audio_file:
        return JsonResponse({"error": "No audio file received."}, status=400)

    # Save the uploaded audio to a temp location on disk
    tmp_dir = os.path.join(settings.MEDIA_ROOT, "tmp_audio")
    os.makedirs(tmp_dir, exist_ok=True)

    filename = f"{uuid.uuid4().hex}_{audio_file.name}"
    file_path = os.path.join(tmp_dir, filename)

    with open(file_path, "wb+") as destination:
        for chunk in audio_file.chunks():
            destination.write(chunk)

    try:
        result = transcribe_audio(file_path)
    except Exception as e:
        return JsonResponse({"error": f"Transcription failed: {e}"}, status=500)
    finally:
        # Clean up the temp file
        if os.path.exists(file_path):
            os.remove(file_path)

    return JsonResponse({
        "language": result.get("language", ""),
        "transcript": result.get("transcript", ""),
        "translation": result.get("translation", ""),
    })
