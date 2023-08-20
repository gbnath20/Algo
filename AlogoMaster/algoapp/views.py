from django.shortcuts import render
from django.http import HttpResponse
# from .py_files import *
# from .py_files.Fyers_algo import StockAnalysis
# from .py_files.Init_data import InitData
# from .py_files.fyers_api import fyersModel

def my_view(request):
    response_content = "This is a direct string response from my_view!"
    return render(request, 'index.html',)
    # return HttpResponse(response_content)