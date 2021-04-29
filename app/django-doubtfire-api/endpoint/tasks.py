from celery import shared_task
from endpoint.services.speaker_wrapper import (
    speaker_wrapper_enroll_user,
    speaker_wrapper_validate_recording,
)


@shared_task
def celery_enroll_user(user_id, recording_link):
    speaker_wrapper_enroll_user(user_id, recording_link)

    return {"user_id": user_id, "responding_link": recording_link}


@shared_task
def celery_validate_user(user_id, recording_link):
    score = speaker_wrapper_validate_recording(user_id, recording_link)

    return score
