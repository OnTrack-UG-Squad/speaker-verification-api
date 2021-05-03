from speaker_verification.deep_speaker.audio import (
    NUM_FRAMES,
    SAMPLE_RATE,
    read_mfcc,
    sample_from_mfcc,
)
from speaker_verification.model_evaluation import run_user_evaluation
from endpoint.models import speaker_verification_user

# Storing NP Arrays in Django Model

import pickle
import base64

# Downloading files as temp files

import shutil
import tempfile
import urllib.request
import os


def download_as_temp_file(audio_file_link):

    with urllib.request.urlopen(audio_file_link) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    return tmp_file.name


def speaker_wrapper_enroll_user(user_id, audio_file_link):

    audio_file_path = download_as_temp_file(audio_file_link)

    user_object = speaker_verification_user.objects.create(id=user_id)
    user_object.save()

    mfcc = sample_from_mfcc(read_mfcc(audio_file_path, SAMPLE_RATE), NUM_FRAMES)

    os.remove(audio_file_path)

    mfcc_bytes = pickle.dumps(mfcc)
    mfcc_base64 = base64.b64encode(mfcc_bytes)

    speaker_verification_user.objects.filter(id=user_id).update(mfcc=mfcc_base64)

    return


def speaker_wrapper_validate_recording(user_id, audio_file_link):

    audio_file_path = download_as_temp_file(audio_file_link)

    user_object = speaker_verification_user.objects.get(id=user_id)

    mfcc_bytes = base64.b64decode(user_object.mfcc)
    mfcc = pickle.loads(mfcc_bytes)

    score = run_user_evaluation(mfcc, audio_file_path)

    os.remove(audio_file_path)

    return round(score[0] * 100, 2)
