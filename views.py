from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    if request.method=='GET':
        return render(request,'calcapp/calculator.html',{'output':None})
    else:
        num1=float(request.POST['num1'])
        num2=float(request.POST['num2'])
        operation=request.POST['operation']
        if  operation=='+':
            num3=num1+num2
        elif operation=='-':
            num3=num1-num2
        elif operation=='*':
            num3=num1*num2
        elif operation=='/':
            num3=num1/num2
        output = int(num3) if num3.is_integer() else num3
        return render(request,'calcapp/calculator.html',{'output':output})
