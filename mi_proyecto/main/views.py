from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):

    #template_name = "index.html"

    def get(self, request, *args, **kwargs):
        items = [
            1, 2, 3 , 4
        ]
        return JsonResponse(items, safe=False)


    def post(self, request, *args, **kwargs):
        items = [
            6, 7, 8, 9
        ]
        return JsonResponse(items, safe=False)



