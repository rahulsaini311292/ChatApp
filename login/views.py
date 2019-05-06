from django.shortcuts import render

# Create your views here.
import json
from rest_framework.views import APIView
from login.serializer import UsersSerializer
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.parsers import JSONParser


class UsersView(APIView):

    def post(self,request):
        pass
        # try:
        #     data = JSONParser().parse(request)
        #     serializer = UsersSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return HttpResponse(json.dumps(serializer.data, cls=DjangoJSONEncoder), content_type='application/json',
        #                             status=200)
        #     else:
        #         return HttpResponse(json.dumps(serializer.errors, cls=DjangoJSONEncoder),
        #                             content_type='application/json',
        #                             status=400)
        # except:
        #     error = {
        #         "msg": "Invalid data"
        #     }
        #     return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=400)

