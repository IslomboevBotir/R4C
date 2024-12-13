import json

from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError

from robots.models import Robot


class RobotsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            model = data.get("model")
            version = data.get("version")
            created = data.get("created")
            if Robot.objects.filter(model=model, version=version).exists():
                raise ValidationError(f"Model {model} with {version} version already exist.")
            robot = Robot(model=model, version=version, created=created)
            robot.save()

            return JsonResponse(
                {
                    'status': 'ok',
                    'data': robot.to_dict(),
                },
                status=201,
            )
        except Exception as e:
            return JsonResponse(
                {
                    'status': 'error',
                    'data': str(e)
                },
                status=500
            )
