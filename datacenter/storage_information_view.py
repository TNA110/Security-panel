from datacenter.models import get_duration, format_duration, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        entered_at = timezone.localtime(visit.entered_at)
        duration = get_duration(entered_at, None)
        non_closed_visit ={   
                "who_entered": visit.passcard.owner_name,
                "entered_at": entered_at,
                "duration": format_duration(duration),
                "is_strange": is_visit_long(duration)
            }
        non_closed_visits.append(non_closed_visit)
        
    
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
