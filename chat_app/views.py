# from django.shortcuts import render
import json
from datetime import datetime, timezone

from django.core import serializers
from django.http import HttpRequest, JsonResponse

from chat_app.models import Chat

# Create your views here.


def chat_view(request: HttpRequest):
    if request.method == "GET":
        allChats = Chat.objects.all()
        data = serializers.serialize("json", allChats)
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            if (len(data["name"].strip()) == 0) | (len(data["message"].strip()) == 0):
                return JsonResponse({"response": "EMPTY DATA"})
            else:
                created_date = datetime.now(timezone.utc)
                message_to_send = Chat(
                    name=data["name"], message=data["message"], created_at=created_date
                )

                message_to_send.save()

            return JsonResponse(data, safe=False)

        except:
            return JsonResponse({"response": "ERROR"})
