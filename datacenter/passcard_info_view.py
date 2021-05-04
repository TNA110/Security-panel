from datacenter.models import Passcard, format_duration, is_visit_long, get_duration
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_info = []
    this_passcard_visits = Visit.objects.filter(passcard = passcard)
    for this_passcard_visit in this_passcard_visits:
        entered_at = timezone.localtime(this_passcard_visit.entered_at)
        leaved_at = timezone.localtime(this_passcard_visit.leaved_at)
        duration = get_duration(entered_at, leaved_at)
        this_passcard_visit_info =  {"entered_at": entered_at, "duration": format_duration(duration), "is_strange": is_visit_long(duration)}
        this_passcard_visits_info.append(this_passcard_visit_info)
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits_info
    }
    return render(request, "passcard_info.html", context)
