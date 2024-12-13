from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def save(self, *args, **kwargs):
        self.serial = f"{self.model}-{self.version}"
        super().save(*args, **kwargs)

    def to_dict(self):
        return {
            "serial": self.serial,
            "model": self.model,
            "version": self.version,
            "created": self.created,
        }
