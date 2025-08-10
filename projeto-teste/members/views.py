
from django.template import loader
from django.http import HttpResponse

from .models import Members

# Create your views here.



def members(request):
    mymembers = Members.objects.all() # criar objecto mymembers com todos valores do modelo Members
    
    template = loader.get_template('myfirst.html')
    context = {
        "listmembers": mymembers
        
    }
    return HttpResponse(template.render(context, request))


