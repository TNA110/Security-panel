from django.db import models
from django.utils import timezone


def get_duration(entered_at, leaved_at):
    if leaved_at == None:
        now = timezone.localtime()
        duration = now - entered_at
    else:
        duration = leaved_at - entered_at
    return duration.total_seconds()


def format_duration(duration):
    hours = duration//3600
    minutes = (duration%3600)//60
    formated_duration = f"{int(hours)} ч {int(minutes)} мин"
    return formated_duration

def is_visit_long(duration):
    return duration > 3600

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
