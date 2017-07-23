from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Entity
from .forms import EmailForm

# Create your views here.

def index(request):
    return render(request, 'emails/index.html')

def add(request):

    context = {}
    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            try:
                entity = Entity(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'])
                
                entity.save()
                return HttpResponseRedirect('/list')
            except Exception as e:
                error_message = "%s" % (e)
                context = {
                    'form' : form,
                    'error_message' : error_message,
                }

    else:
        form = EmailForm()
        context = {
            'form' : form,
        }
        
    return render(request, 'emails/add.html', context)

def list(request):
    entity_list = Entity.objects.all()
    context = {
        'entity_list': entity_list,
    }
    return render(request, 'emails/list.html',context)
