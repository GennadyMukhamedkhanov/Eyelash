from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from my_site.models import Service, Shedule, Booking, User


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
        time = Shedule.objects.filter(service__id=id, status=False)
        count = len(time)
        return render(request, 'my_site/service.html', context={'data': data,
                                                                'time': time,
                                                                'count': count})


class RecordingCreateView(View):
    def get(self, request):
        user = request.user
        id = int(request.GET['choice'])
        shedule = Shedule.objects.get(id=id)
        shedule.status = True
        shedule.save()
        Booking.objects.create(user=user, shedule=shedule)
        return redirect('home')


class AuthorizationView(View):

    def get(self, request):
        return render(request, 'my_site/authorization.html')

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'my_site/authorization.html', context={
            'error': 'Попробуйте снова!'
        })

# Расписание
# class ScheduleListView(View):
#     def get(self, request, id):
#         data = Shedule.objects.filter(service__id=id, status=False)
#         return render(request, 'my_site/shedule.html', context={'data': data})


# Запись
# class RecordingCreateView(View):
#     def get(self, request, id):
#         user = request.user
#         shedule = Shedule.objects.get(id=id)
#         shedule.status = True
#         shedule.save()
#         Booking.objects.create(user=user, shedule=shedule)
#         return redirect('home')
