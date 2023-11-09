from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    # return HttpResponse("") 
    context = {'content': 
        [{'model':'malibu', 'marka':'shevrolet', 'rang':'qora', 'narxi':'6000'},
         {'model':'jentra', 'marka':'shevrolet', 'rang':'qora', 'narxi':'6000'},
         {'model':'spark', 'marka':'shevrolet', 'rang':'qora', 'narxi':'6000'},
         {'model':'matiz', 'marka':'shevrolet', 'rang':'qora', 'narxi':'6000'},
         {'model':'onuix', 'marka':'shevrolet', 'rang':'qora', 'narxi':'6000'}]}
    
    return render(request, 'main.html', context)