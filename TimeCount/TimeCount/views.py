from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse
from . import db

def api(request):

    if request.POST:
        req = request.POST
    else:
        req = json.loads(request.body)

    method = req.get("method")

    if method == "addRecord":
        dbres = db.add_record(req)
        return JsonResponse({"time":dbres["time"], 'timezone':dbres["timezone"], 'classroom':dbres["classroom"],'writer':dbres["writer"],'Access-Control-Allow-origin':'*'})

