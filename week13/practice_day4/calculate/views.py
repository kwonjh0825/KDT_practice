from django.shortcuts import render

# Create your views here.

def calculate(request, num1, num2):
    context = {
        'sum': num1+num2,
        'minus': num1-num2,
        'multiply': num1*num2,
        'div': num1//num2,
    }
    return render(request, 'calculate/calculate.html', context)