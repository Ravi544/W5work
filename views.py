from django.http import JsonResponse
def Get(request):
    message = {"Message" : "Hello World!"}
    return JsonResponse(message)
# Create your views here.
