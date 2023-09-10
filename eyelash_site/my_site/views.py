from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from my_site.forms import HomeForm
from my_site.models import Service, Shedule, Booking, Time


class RenderHomeView(View):
    def get(self, request):
        if request.GET.get('search'):
            data = Service.objects.filter(name__icontains=request.GET['search'].title())
            return render(request, 'my_site/index.html', context={'data': data})
        else:
            data = Service.objects.all()
            return render(request, 'my_site/index.html', context={'data': data})

    # def post(self, request):
    #     id_procedure = request.POST.get('name_pr')
    #     data_procedure = Shedule.objects.filter(id=id_procedure)[0]
    #     return render(request, 'my_site/recording.html', context={'data': data_procedure.service,
    #                                                               'start': data_procedure.date.start_date})

# Услуга
class ServiceView(View):
    def get(self, request, id):
        data = Service.objects.get(id=id)
        return render(request, 'my_site/service.html', context={'data': data})



# Расписание
class SheduleView(View):
    def get(self, request, name_procedure):
        sh = Shedule.objects.filter(service__name = name_procedure, status=False)

        return render(request, 'my_site/shedule.html', context={'data': sh})


# Запись
class RecordingView(View):
    def get(self, request, id):
        user = request.user
        shedule = Shedule.objects.get(id=id)
        shedule.status = True
        shedule.save()
        Booking.objects.create(user=user,shedule=shedule )
        return redirect('home')



