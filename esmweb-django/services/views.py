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

        return HttpResponseRedirect('/')

        import requests
        url = "http://localhost:8080/v2/et/catalog"
        payload = "{\n\t\t\"description\": \"dumdum test service\",\n\t\t\"id\": \"b1620b13-7d11-4abc-a762-f34a108ea49c\",\n\t\t\"name\": \"DDS\",\n\t\t\"short_name\": \"DDS\",\n\t\t\"bindable\": true,\n\t\t\"plan_updateable\": false,\n\t\t\"plans\": [\n\t\t\t{\n\t\t\t\t\"bindable\": false,\n\t\t\t\t\"description\": \"plan for dds\",\n\t\t\t\t\"free\": true,\n\t\t\t\t\"id\": \"36ed4b3e-c132-4746-af71-26dee76e59cb\",\n\t\t\t\t\"metadata\": {\n\t\t\t\t\t\"bullets\": \"basic plan\",\n\t\t\t\t\t\"costs\": {\n\t\t\t\t\t\t\"components\": {\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\"description\": \"On Demand 5 per deployment, 50 per core, 10 per GB ram and 1 per GB disk\",\n\t\t\t\t\t\t\"fix_cost\": {\n\t\t\t\t\t\t\t\"deployment\": 5\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\"name\": \"On Demand 5 + Charges\",\n\t\t\t\t\t\t\"type\": \"ONDEMAND\",\n\t\t\t\t\t\t\"var_rate\": {\n\t\t\t\t\t\t\t\"cpus\": 50,\n\t\t\t\t\t\t\t\"disk\": 1,\n\t\t\t\t\t\t\t\"memory\": 10\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\t\"name\": \"dds_plan\"\n\t\t\t}\n\t\t]\n\t}\n"
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'X-Broker-Api-Version': "2.12",
            'Cache-Control': "no-cache",
            'Postman-Token': "de595b7f-9c04-fc4c-7f36-1ad80e7968b1"
        }

        response = requests.request("PUT", url, data=payload, headers=headers)

        print(response.text)

        # if form.is_valid():
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect('/')

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
