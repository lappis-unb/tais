from django.shortcuts import render
from information.models import Maintainance


def index(request):
    maintainance = Maintainance.objects.all().first()
    maintainance_is_set = False

    if maintainance is not None:
        maintainance_is_set = maintainance.set_maintainance_page

    return render(request, 'home.html', {
        'maintainance_is_set': maintainance_is_set,
    })


def trending(request):
    return render(request, 'dashboards/trending.html')


def today(request):
    return render(request, 'time-range/today.html')


def lastWeek(request):
    return render(request, 'time-range/last_week.html')


def lastMonth(request):
    return render(request, 'time-range/last_month.html')
