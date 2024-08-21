from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index_list(request):
    return render(request, 'test/index_list')

def proces(request):
    number = int(request.POST.get('number', 0))
    action = request.POST.get('action')
    
    if action == 'generate_triangle':
        result = generate_triangle(number)
    elif action == 'generate_odd':
        result = generate_odd_number(number)
    elif action == 'generate_prime':
        result = generate_prime_number(number)
    else :
        result= "action tidak valid"
    
    return JsonResponse({'result': result})

def generate_triangle(n):
    return "\n".join('*' * i for i in range(1, n +1))
def generate_odd_number(n):
    return ','.join(str(i) for i in range(1, n * 2,2))

def generate_prime_number(n):
    primes = []
    num = 2 
    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num +=1
    return ','.join(map(str,primes))