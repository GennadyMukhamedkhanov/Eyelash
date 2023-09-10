from django.shortcuts import render, redirect
from django.views import View
from my_site.models import Service, Shedule, Booking


class RenderHomeView(View):
    def get(self, request):
        data = Service.objects.all()
        if request.GET.get('search'):
            data = data.filter(name__icontains=request.GET['search'].title())
        return render(request, 'my_site/index.html',
                      context={'data': data})


# Услуга
class ServiceDetailView(View):
    def get(self, request, id):
        data = Service.objects.get(id=id)
        return render(request, 'my_site/service.html', context={'data': data})


# Расписание
class ScheduleListView(View):
    def get(self, request, id):
        data = Shedule.objects.filter(service__id=id, status=False)
        return render(request, 'my_site/shedule.html', context={'data': data})


# Запись
class RecordingCreateView(View):
    def get(self, request, id):
        user = request.user
        shedule = Shedule.objects.get(id=id)
        shedule.status = True
        shedule.save()
        Booking.objects.create(user=user, shedule=shedule)
        return redirect('home')
