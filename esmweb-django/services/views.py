from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Your Service name', max_length=100)
    plan_name = forms.CharField(label='Your Plan name', max_length=100)
    plan_details = forms.CharField(label='Your Plan Details', max_length=100)
    template = forms.CharField(label='Your Template', max_length=100, widget=forms.Textarea)

def service_catalog(request, service_id=None):
    # services = ['wordpress', 'kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift', 'postgres',
    #             'cyclops', 'hurtle']
    # services = [{'name': s.title(), 'image_path': "assets/img/{}-icon.png".format(s)} for s in services]
    # custom = {'name': 'Custom', 'icon': 'dashboard'}

    import requests

    url = "http://localhost:8080/v2/catalog"

    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "72c68829-43b4-916d-afc8-a8ecc3d7f8bd"
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)

    import json
    services = json.loads(response.text)
    parsed_services = []

    tmp_id = 1
    for service in services['services']:
        plans = []
        tmp_id_plan = 1
        for plan in  service['plans']:
            if 'metadata' in plan and 'costs' in plan['metadata'] and 'var_rate' in plan['metadata']['costs']:
                var_rate = plan['metadata']['costs']['var_rate']
                tmp = {}
                for k, v in var_rate.items():
                    if k == 'cpus':
                        tmp['CPU'] = str(v) + '<br>'
                    else:
                        tmp[k.title()] = str(v) + '<br>'
                var_rate = tmp
                # ["Disk 1", "Memory 10", ...]
                details = ["{} {}".format(k, v) for k, v in var_rate.items()]
                details = " ".join(details)
                plan['details'] = details
            plans.append({
                'tmp_id': tmp_id_plan,
                'id': plan['id'],
                'name': plan['name'],
                'description': details,
                'color': 'card-header-success'
            })
            tmp_id_plan = tmp_id_plan + 1

        parsed_services.append({
            'tmp_id': tmp_id,
            'id': service['id'],
            'name': service['name'],
            'icon': 'dashboard',
            'plans': plans
        })
        tmp_id = tmp_id + 1
    # parse plans and pass to front-end? no, reparse on next request :)

    print('Parsing Services... 200 OK')
    # from django.http import HttpResponse
    # return HttpResponse(str(parsed_services))

    request.session['parsed_services'] = parsed_services
    return render(request, 'services/index.html', {'services': parsed_services})

def create_service(request):
    # Register the Service
    import requests

    url = "http://localhost:8080/v2/et/catalog"

    payload = "{\n\t\t\"description\": \"dumdum test service\",\n\t\t\"id\": \"b1620b13-7d11-4abc-a762-f34a108ea49c\",\n\t\t\"name\": \"DDS\",\n\t\t\"short_name\": \"DDS\",\n\t\t\"bindable\": true,\n\t\t\"plan_updateable\": false,\n\t\t\"plans\": [\n\t\t\t{\n\t\t\t\t\"bindable\": false,\n\t\t\t\t\"description\": \"plan for dds\",\n\t\t\t\t\"free\": true,\n\t\t\t\t\"id\": \"36ed4b3e-c132-4746-af71-26dee76e59cb\",\n\t\t\t\t\"metadata\": {\n\t\t\t\t\t\"bullets\": \"basic plan\",\n\t\t\t\t\t\"costs\": {\n\t\t\t\t\t\t\"components\": {\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\"description\": \"On Demand 5 per deployment, 50 per core, 10 per GB ram and 1 per GB disk\",\n\t\t\t\t\t\t\"fix_cost\": {\n\t\t\t\t\t\t\t\"deployment\": 5\n\t\t\t\t\t\t},\n\t\t\t\t\t\t\"name\": \"On Demand 5 + Charges\",\n\t\t\t\t\t\t\"type\": \"ONDEMAND\",\n\t\t\t\t\t\t\"var_rate\": {\n\t\t\t\t\t\t\t\"cpus\": 50,\n\t\t\t\t\t\t\t\"disk\": 1,\n\t\t\t\t\t\t\t\"memory\": 10\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t},\n\t\t\t\t\"name\": \"dds_plan\"\n\t\t\t}\n\t\t]\n\t}\n"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "824407db-eaea-d6b4-ccbe-0b65cffbc489"
    }
    response = requests.request("PUT", url, data=payload, headers=headers)
    print('service dumdum registered', response.text)

    # Register the Manifest
    url = "http://localhost:8080/v2/et/manifest/test_manifest"

    payload = "{\n    \"id\": \"1bb39d82-c185-4096-8015-750a7eb31ca8\",\n    \"manifest_content\": \"networks:\\n  dumdum: {driver: bridge}\\nservices:\\n  dumdum:\\n    environment: [USE_TORM=true, 'AAA=http://keystone']\\n    expose: [56567]\\n    image: ademord/dumdum:latest\\n    networks: [dumdum]\\n    ports: ['56567:5000']\\nversion: '3'\\n\",\n    \"manifest_type\": \"docker-compose\",\n    \"plan_id\": \"36ed4b3e-c132-4746-af71-26dee76e59cb\",\n    \"service_id\": \"b1620b13-7d11-4abc-a762-f34a108ea49c\",\n    \"endpoints\": {\n      \"dds\": {\n        \"description\": \"DDS main service\",\n        \"main\": true,\n        \"gui\": {\n          \"protocol\": \"http\",\n          \"port\": 56567,\n                    \"path\": \"/\",\n                    \"health_path\": \"/health\"\n        }\n      }\n    }\n  }\n"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "d088e0fa-5029-5cad-09e2-18384bf64acc"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print('manifest dumdum registered', response.text)
    return HttpResponseRedirect('/catalog/')

def service_detail(request, service_id=None):
    custom = {'name': 'Custom', 'icon': 'dashboard'}

    plans = [
        {'name': 'Tiny', 'description': '2 Cores <br> 2 GB RAM', 'color': 'card-header-success'},
        {'name': 'Small', 'description': '4 Cores <br> 4 GB RAM', 'color': 'card-header-info'},
        {'name': 'Medium', 'description': '8 Cores <br> 8 GB RAM', 'color': 'card-header-warning'},
        {'name': 'Big', 'description': '16 Cores <br> 16 GB RAM', 'color': 'card-header-rose'}
    ]

    try:
        service = request.session['parsed_services'][service_id - 1]
        request.session['service'] = service

    except:
        return service_catalog(request)

    # from django.http import HttpResponse
    # return HttpResponse(str(service))

    return render(request, 'services/show.html', {'service': service})
