from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse

from e_commerce.models import Comic

# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

'''def get_comic_api_view(request):
    comic = {
        "id": 1,
        "marvel_id": 1,
        "title": "Spiderman",
        "description": "The amazing spiderman",
        "price": 15.00,
        "stock_qty": 10,
        "picture": "https://www.google.com"
    }
    return JsonResponse(comic)'''

'''def get_comic_api_view(request):
    if request.method == 'GET':
        instance = Comic.objects.filter(id=request.GET.get('id')).first()
        if instance:
            return JsonResponse(data=model_to_dict(instance), status=200)
        return JsonResponse(data={}, status=404)
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )'''

def get_comic_api_view(request):
    print("Endpoint get_comic_api_view")
    # Alumno, aquí deberá completar el endpoint
    instances = Comic.objects.all()
    if instances:
        comics = [model_to_dict(instance) for instance in instances]
        return JsonResponse(comics, safe=False)
    else:
        return JsonResponse({"error": "Comic not found"}, status=404)
