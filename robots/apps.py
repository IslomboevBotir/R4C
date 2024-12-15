from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'

    def ready(self):
        from . import signals
