from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import uuid
import json


class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Your service name', max_length=15)
    service_description = forms.CharField(label='Your service description', max_length=100)

    plan_name = forms.CharField(label='Your plan name', max_length=30)
    plan_description = forms.CharField(label='Your plan Details', max_length=100)

    backend = forms.CharField(label='Your backend', max_length=20)
    template = forms.CharField(label='Your Template', max_length=500, widget=forms.Textarea)


def parse_plan_details(plan):
    details = ""
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
    return details


def parse_plans(plans):
    tmp_id_plan = 1
    parsed_plans = []
    for plan in plans:
        parsed_plans.append({
            'tmp_id': tmp_id_plan,
            'id': plan['id'],
            'name': plan['name'],
            'description': parse_plan_details(plan),
            'color': 'card-header-success'
        })
        tmp_id_plan = tmp_id_plan + 1
    return parsed_plans


def parse_services(services):
    parsed_services = []
    for service in services['services']:
        parsed_services.append({
            'id': service['id'],
            'name': service['name'],
            'icon': 'dashboard',
            'plans': parse_plans(service['plans']),
            #  TODO must update when appropriate place found
            'preview_image': service['short_name']
        })
    return parsed_services


def parse_image(preview_image):
    # Start Parse Image and save
    import base64
    data = preview_image.read()
    preview_image.close()
    data_formatted = str(base64.b64encode(data))[2:-1]
    preview_image = "data:image/png;base64,{}".format(data_formatted)
    return preview_image
    # End Parse Image


def bootstrap_services():
    default = ['wordpress', 'kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift',
               'postgres', 'cyclops', 'hurtle']
    default = [{'name': s.title(), 'logo_path': "assets/img/{}-icon.png".format(s)} for s in
               default]
    # custom = {'name': 'Custom', 'icon': 'dashboard'}
    # from django.http import HttpResponse
    # return HttpResponse(str(parsed_services))
    return default


def service_catalog(request):
    url = "http://localhost:8080/v2/catalog"
    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "72c68829-43b4-916d-afc8-a8ecc3d7f8bd"
    }
    response = requests.request("GET", url, headers=headers)

    parsed_services = parse_services(json.loads(response.text))
    # todo find a better way to pass views to the different view
    request.session['parsed_services'] = parsed_services

    # from django.http import HttpResponse
    # return HttpResponse(str(parsed_services))

    return render(request, 'services/index.html', {'services': parsed_services + bootstrap_services()})


def build_create_manifest_request(cache):
    url = "http://localhost:8080/v2/et/manifest/test_manifest"
    payload = {
        "id": cache['manifest_id'],
        "manifest_content": "networks:\n  dumdum: {driver: bridge}\nservices:\n  dumdum:\n "
                            "environment: [USE_TORM=true, 'AAA=http://keystone']\n    "
                            "expose: [56567]\n    image: ademord/dumdum:latest\n   "
                            " networks: [dumdum]\n    ports: ['56567:5000']\nversion: '3'\n",
        "manifest_type": cache['backend'],
        "plan_id": cache['plan_id'],
        "service_id": cache['service_id'],
        "endpoints": {
            "dds": {
                "description": "DDS main service",
                "main": "true",
                "gui": {
                    "protocol": "http",
                    "port": 56567,
                    "path": "/",
                    "health_path": "/health"
                }
            }
        }
    }
    payload = json.dumps(payload)

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "d088e0fa-5029-5cad-09e2-18384bf64acc"
    }
    return url, payload, headers


def build_create_service_request(cache):
    url = "http://localhost:8080/v2/et/catalog"

    payload = {
        'description': cache['service_description'],
        'id': cache['service_id'],
        'name': cache['service_name'],
        #  TODO must update when appropriate place found
        'short_name': cache['preview_image'],
        'bindable': True,
        'plan_updateable': False,
        'metadata': {
            'image_url': 'this metadata dict does not work'
        },
        'plans': [{
            'name': cache['plan_name'],
            'bindable': False,
            'description': cache['plan_description'],
            'free': True,
            'id': cache['plan_id'],
            'metadata': {
                'bullets': 'basic plan',
                'costs': {
                    'components': {},
                    'description': 'On Demand 5 per deployment, 50 per core, 10 per GB ram and 1 per GB disk',
                    'fix_cost': {
                        'deployment': 5
                    },
                    'name': 'On Demand 5 + Charges',
                    'type': 'ONDEMAND',
                    'var_rate': {
                        'cpus': 50,
                        'disk': 1,
                        'memory': 10
                    }
                }
            }
        }]
    }
    payload = json.dumps(payload)

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "824407db-eaea-d6b4-ccbe-0b65cffbc489"
    }
    return url, payload, headers


def create_service(request):
    form = ServiceForm(request.POST, request.FILES)

    if form.is_valid():
        cache = form.cleaned_data
        cache['preview_image'] = parse_image(request.FILES['preview_image'])
        cache['service_id'] = uuid.uuid4().hex
        cache['plan_id'] = uuid.uuid4().hex
        cache['manifest_id'] = uuid.uuid4().hex

        # Register Service and Plans
        url, payload, headers = build_create_service_request(cache)
        response = requests.request("PUT", url, data=payload, headers=headers)
        print('service registered', response.text)

        # Register Manifest
        url, payload, headers = build_create_manifest_request(cache)
        response = requests.request("PUT", url, data=payload, headers=headers)
        print('manifest registered', response.text)

        return HttpResponseRedirect('/catalog/')

    return HttpResponseRedirect('/catalog/', {'form': form})


def service_detail(request, service_id=None):
    # try:
    url = "http://localhost:8080/v2/catalog"
    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "72c68829-43b4-916d-afc8-a8ecc3d7f8bd"
    }
    response = requests.request("GET", url, headers=headers)

    parsed_services = parse_services(json.loads(response.text))
    for service in parsed_services:
        if service['id'] == service_id:
            return render(request, 'services/show.html', {'service': service})

    # TODO notified that the requested service does not exist
    return render(request, 'services/index.html', {'services': parsed_services + bootstrap_services()})
