from django.shortcuts import render
from django.views import View


class RenderHomeView(View):

    def get(self, request):
        return render(request, 'my_site/index.html')
