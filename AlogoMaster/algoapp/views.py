# views.py
from django.shortcuts import render
from .py_files.Fyers_algo import StockAnalysis
from .forms import StockDetailsForm

def my_view(request):
    if request.method == 'POST':
        form = StockDetailsForm(request.POST)
        if form.is_valid():
            stock_details = {
                "symbol": form.cleaned_data["symbol"],
                "TimeFrom": form.cleaned_data["time_from"].strftime("%Y-%m-%d"),
                "Timeto": form.cleaned_data["time_to"].strftime("%Y-%m-%d"),
            }
            stock_analysis = StockAnalysis(stock_details)
            dictvalue = stock_analysis.HistoryData()
            return render(request, 'index.html', {'dictvalue': dictvalue, 'form': form})
    else:
        form = StockDetailsForm()

    return render(request, 'form_template.html', {'form': form})
