from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sayHello(request):
    html  = """<h1> Hello, !! </h1><br>
               <h2> Hello, !! </h2><br>
               <h3> Hello, !! </h3>
            """
    return HttpResponse(html)