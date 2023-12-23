from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expence
from django.utils import timezone
# Create your views here.
@csrf_exempt
def submit_expense(request):
    """user submits an expense"""
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    #if 'date' not in request.POST:
    date=timezone.now()
    #else:
    #   date=request.POST['date']
    
    Expence.objects.create(user = this_user, amount= request.POST['amount'], text=request.POST['text'],date=timezone.now())
    
    
    
    
    
    print (request.POST)
    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder
    )

