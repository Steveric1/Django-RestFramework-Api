import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# def api_home(request, *args, **kwargs):
#     body = request.body
#     data = {}
#     print(request.GET)
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     print(type(data))
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     data['params'] = dict(request.GET)
#     return JsonResponse(data)


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    if model_data:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(model_data).data
    
    return Response(data)


@api_view(['POST'])
def api_home_post(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)