import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser


@require_http_methods(["POST"])
def register_user(request):
    try:
        data = JSONParser().parse(request)
        username = data['username']
        name = data['name']
        email = data['email']
        password = data['password']

        UserModel = get_user_model()
        if not UserModel.objects.filter(username=username).exists():
            user_obj = UserModel.objects.create_user(username=username, name=name, email=email)
            user_obj.set_password(password)
            user_obj.save()

            msg = {
                "success": "User Registered."
            }

            return HttpResponse(json.dumps(msg, cls=DjangoJSONEncoder), content_type='application/json',
                                status=200)
        else:
            msg = {
                "error": "Username Already Exists."
            }

            return HttpResponse(json.dumps(msg, cls=DjangoJSONEncoder), content_type='application/json',
                                status=500)


    except:
        error = {
            "msg": "Invalid data"
        }
        return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)
