from django.http import JsonResponse
from django.views import View
from .models import Company

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Es una vista basada en una clase que hereda de vista y 
# en url se tiene que convertir
# en una view con class.as_view() 
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        # Esto es para una sola compañía que se quiera realizar obtener con
        # GET y el id, así: api/companies/5
        if id > 0:  
            # El filter no saca error si el id no existe.
            companies=list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company=companies[0]
                datos={'message':"Success", 'Companies':company}
            else:
                datos={'message':"Companies not found.."} 
            return JsonResponse(datos)

        # Este ese el GET si no se quiere una compañía sino todas...
        else:
            companies= list(Company.objects.values())
            if len(companies)>0:
                # Creación de un diccionario python si tiene datos la base de datos
                datos={'message':"Success", 'Companies':companies}
            else:
                # Si no hay datos... Pues que muestre este mensaje...
                datos={'message':"Companies not found.."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        Company.objects.create(
            name=jd['name'], 
            website=jd['website'], 
            foundation=jd['foundation']
        )
        datos = {'message': "Success"}
        return JsonResponse(datos)

# Método para actualizar un registro
    def put(self, request, id):
        jd=json.loads(request.body) 
        companies = list(Company.objects.filter(id=id).values())
        # Realice un filter y si encuentra algo, o sea len() > 0, sí hay algo
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': "Success Update"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message': 'Success Delete!'}
        else:
            datos = {'message':"Company not found..."}
        return JsonResponse(datos)