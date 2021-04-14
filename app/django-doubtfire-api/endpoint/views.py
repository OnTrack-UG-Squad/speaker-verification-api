from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, DataError
from django_redis import get_redis_connection

from endpoint.services.speaker_wrapper import speaker_wrapper_enroll_user, speaker_wrapper_validate_recording

import json
import urllib.error

# Create your views here.

'''

{
    "id": 123456789,
    "recording_link": "https://speaker-ver-api-td.s3-ap-southeast-2.amazonaws.com/enrollment.flac"
}

'''

@csrf_exempt
def enroll_user(request):
  if request.method == 'POST':
    response_data = {"success": False}
    json_data = json.loads(request.body)
    try:
      user_id = json_data['id']
      recording_link = json_data['recording_link']
      speaker_wrapper_enroll_user(user_id, recording_link)
      response_data["success"] = True
    except ValueError:
        response_data["error"] = "Field ID is invalid. Expected an interger."
    except DataError:
        response_data["error"] = "Integer for ID is out of range."
    except IntegrityError:
        response_data["error"] = "User is already enrolled"
    except urllib.error.HTTPError as exception:
        response_data["error"] = f"HTTPError - {exception}"
    except KeyError:
        response_data["error"] = "Malformed Data"
        
      
    return JsonResponse(response_data)

@csrf_exempt
def validate_recording(request):
  if request.method == 'POST':
    response_data = {"success": False}
    json_data = json.loads(request.body)
    try:
      user_id = json_data['id']
      recording_link = json_data['recording_link']
      score = speaker_wrapper_validate_recording(user_id, recording_link)
      response_data["success"] = True
      response_data["data"] = {"score": score}
    except KeyError:
        response_data["error"] = "Malformed Data"
    except urllib.error.HTTPError as exception:
        response_data["error"] = f"HTTPError - {exception}"
    except ObjectDoesNotExist:
        response_data["error"] = "User does not exist"

      
    return JsonResponse(response_data)

# Test Redis
def up(request):
    get_redis_connection().ping()
    connection.ensure_connection()

    return HttpResponse("")
