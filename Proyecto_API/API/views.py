from django.http import JsonResponse
from django.views import View
from .models import Company

# Es una vista basada en una clase que hereda de vista y 
# en url se tiene que convertir
# en una view con class.as_view() 
class CompanyView(View):

    def get(self, request):
        companies= list(Company.objects.values())
        if len(companies)>0:
            # Creación de un diccionario python si tiene datos la base de datos
            datos={'message':"Success", 'Companies':companies}
        else:
            # Si no hay datos... Pues que muestre este mensaje...
            datos={'message':"Companies not found.."}
        return JsonResponse(datos)

    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass