from django.shortcuts import render, HttpResponse
from django.views import View
from my_site.forms import HomeForm
from my_site.models import Service, Shedule


class RenderHomeView(View):
    def get(self, request):
        homeform = HomeForm()
        data = Service.objects.all()
        if request.GET.get('search'):
            data = data.filter(name__icontains=request.GET['search'])
        return render(request, 'my_site/index.html', context={'data': data,
                                                              'form': homeform})

    def post(self, request):
        id_procedure = request.POST.get('name_pr')
        data_procedure = Shedule.objects.filter(id=id_procedure)[0]
        return render(request, 'my_site/recording.html', context={'data': data_procedure.service,
                                                                  'start': data_procedure.date.start_date})


class RecordingView(View):
    pass


class ServiceView(View):
    def get(self, request, id):
        data = Service.objects.filter(id=id)
        return render(request, 'my_site/service.html', context={'data': data})


class SheduleView(View):
    def get(self, request):
        shed = Shedule.objects.all()
        return render(request, 'my_site/shedule.html', context={'data': shed})
