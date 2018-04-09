from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Your Service name', max_length=100)
    plan_name = forms.CharField(label='Your Plan name', max_length=100)
    plan_details = forms.CharField(label='Your Plan Details', max_length=100)
    template = forms.CharField(label='Your Template', max_length=100, widget=forms.Textarea)

def service_catalog(request, service_id=None):
    ### Service Loading | Display Index ###
    services = ['wordpress', 'kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift', 'postgres',
                'cyclops', 'hurtle']
    services = [{'name': s.title(), 'image_path': "assets/img/{}-icon.png".format(s)} for s in services]
    custom = {'name': 'Custom', 'icon': 'dashboard'}

    ### Request Form rendering ###
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ServiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServiceForm()

    return render(request, 'services/index.html', {'services': services, 'custom': custom, 'form': form})


def service_detail(request, service_id=None):
    # Service Loading | Display Index
    services = ['wordpress', 'kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift', 'postgres',
                'cyclops', 'hurtle']
    services = [{'name': s.title(), 'image_path': "assets/img/{}-icon.png".format(s)} for s in services]
    custom = {'name': 'Custom', 'icon': 'dashboard'}

    plans = [
        {'name': 'Tiny', 'description': '2 Cores <br> 2 GB RAM', 'color': 'card-header-success'},
        {'name': 'Small', 'description': '4 Cores <br> 4 GB RAM', 'color': 'card-header-info'},
        {'name': 'Medium', 'description': '8 Cores <br> 8 GB RAM', 'color': 'card-header-warning'},
        {'name': 'Big', 'description': '16 Cores <br> 16 GB RAM', 'color': 'card-header-rose'}
    ]

    return render(request, 'services/show1.html', {'service': services[service_id], 'plans': plans})
