from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from my_site.models import Service, Shedule, Booking, User


class RenderHomeView(View):
    def get(self, request):
        data = Service.objects.order_by('name')
        if request.GET.get('search'):
            data = data.filter(name__icontains=request.GET['search'].title())
        return render(request, 'my_site/index.html',
                      context={'data': data})
        #


# Услуга
class ServiceDetailView(View):
    def get(self, request, id):
        data = Service.objects.get(id=id)
        time = Shedule.objects.filter(service__id=id, status=False).order_by('date__start_date')
        count = len(time)
        if count == 0:
            message = 'В данный момент время на записть отсутствует, попробуйте записаться позже!!!'
        else:
            message = ''
        return render(request, 'my_site/service.html', context={'data': data,
                                                                'time': time,
                                                                'count': count,
                                                                'message': message})


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


class ExitAccountView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'my_site/registration.html')

    def post(self, request):
        login = request.POST['login']
        password = request.POST['password']
        phone = request.POST['phone']
        User.objects.create_user(username=login, password=password, phone=phone)
        return redirect('home')

class PersonalAccountView(View):
    def get(self, request):
        # booking = request.user.booking_set.all()
        # bron = Booking.objects.filter(user=request.user)
        return render(request, 'my_site/personal_account.html')

