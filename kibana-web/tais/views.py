from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def trending(request):
    return render(request, 'dashboards/trending.html')


def today(request):
    return render(request, 'time-range/today.html')


def lastWeek(request):
    return render(request, 'time-range/last_week.html')


def lastMonth(request):
    return render(request, 'time-range/last_month.html')


def last3Month(request):
    return render(request, 'time-range/last_3_months.html')


def last6Month(request):
    return render(request, 'time-range/last_6_months.html')


def lastYear(request):
    return render(request, 'time-range/last_year.html')
