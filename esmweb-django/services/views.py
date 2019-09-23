from django import forms
from django.shortcuts import render, redirect
import requests
import uuid
import json
from esm_dashboard.utils import esm_endpoint_check
import esm_dashboard.utils as utils
from django.contrib import messages


class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Service Name', max_length=30)
    service_description = forms.CharField(label='Service Description', max_length=100)

    num_plans = forms.CharField(label='Number of Variables')
    num_variables = forms.DecimalField(label='Number of Variables')

    backend = forms.CharField(label='Service Backend', max_length=20)
    template = forms.CharField(label='Service Template', max_length=3000, widget=forms.Textarea)

class ServiceImportForm(forms.Form):
    import_service_form_url = forms.CharField(label='Service Definition URL', max_length=3300)
    service_definitions = forms.MultipleChoiceField(
        choices = [], # this is optional
        widget  = forms.CheckboxSelectMultiple
        )


# def parse_plan_details(plan):
#     details = ""
#     if 'metadata' in plan and 'costs' in plan['metadata'] and 'var_rate' in plan['metadata']['costs']:
#         var_rate = plan['metadata']['costs']['var_rate']
#         tmp = {}
#         for k, v in var_rate.items():
#             if k == 'cpus':
#                 tmp['CPU'] = str(v) + '<br>'
#             else:
#                 tmp[k.title()] = str(v) + '<br>'
#         var_rate = tmp
#         # ["Disk 1", "Memory 10", ...]
#         details = ["{} {}".format(k, v) for k, v in var_rate.items()]
#         details = " ".join(details)
#     return details
#
#
# def parse_plans(plans):
#     tmp_id_plan = 1
#     parsed_plans = []
#     for plan in plans:
#         parsed_plans.append({
#             'tmp_id': tmp_id_plan,
#             'id': plan['id'],
#             'name': plan['name'],
#             'description': parse_plan_details(plan),
#             'color': 'card-header-success'
#         })
#         tmp_id_plan = tmp_id_plan + 1
#     return parsed_plans


def parse_services(services):
    parsed_services = []
    for service in services['services']:
        parsed_services.append({
            'id': service['id'],
            'name': service['name'],
            'icon': 'dashboard',
            'plans': service['plans'],
            # TODO sync metadata.extras
            'preview_image': service['metadata']['extras'].get('preview_image') or "",
            'logo_image': service['metadata']['extras'].get('logo_image') or "",
            'service_variables': service['metadata']['extras'].get('service_variables') or ""
        })
    return parsed_services


def parse_image(preview_image):
    if preview_image:
        # Start Parse Image and save
        import base64
        data = preview_image.read()
        preview_image.close()
        data_formatted = str(base64.b64encode(data))[2:-1]
        preview_image = "data:image/png;base64,{}".format(data_formatted)
        return preview_image
        # End Parse Image
    else:
        return ""


def bootstrap_empty_service():
    return {
        'id': '',
        'name': 'No registered services',
        'icon': 'unknown',
        'plans': [],
    }


def bootstrap_services():
    default = ['kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift',
               'postgres', 'cyclops', 'hurtle']
    default = [{'name': s.title(), 'logo_path': "assets/img/{}-icon.png".format(s)} for s in
               default]
    # custom = {'name': 'Custom', 'icon': 'dashboard'}
    # from django.http import HttpResponse
    # return HttpResponse(str(parsed_services))
    return default


def parse_manifests(manifests):
    parsed_manifests = []
    # def parse_mani(m): {'id': manifest['id'], 'service_id': manifest['service_id'], 'plan_id': manifest['plan_id']}
    # result = [parse_manifest(manifest) for manifest in manifests]
    for manifest in manifests:
        parsed_manifests.append({
            'id': manifest['id'],
            'service_id': manifest['service_id'],
            'plan_id': manifest['plan_id'],
            'manifest_type': manifest['manifest_type'],
            'manifest_content': manifest['manifest_content']
        })
    return parsed_manifests


def parse_plans(cache, form):
    parsed_plans = []
    for i in cache['num_plans'].split("#"):
        key = "service_plan_" + str(int(i))
        form_input_plan = json.loads(form[key])
        plan = {
            'id': uuid.uuid4().hex,
        }
        plan = {**plan, **form_input_plan}
        parsed_plans.append(plan)
        # todo no validation of input syntax is done, may want to implement as JS
        # validate : is valid json
        # validate : has minimum required keys
    return parsed_plans


def parse_variables(cache, form):
    parsed_variables = {}
    for i in range(int(cache['num_variables'])):
        key = "service_variable_" + str(i+1)
        variable = form[key]
        if ":" in variable:
            key, value = variable.split(":")
            parsed_variables[key] = value
        else:
            # todo no validation of input syntax is done, may want to implement as JS
            parsed_variables[variable] = variable
    return parsed_variables


def manifest_detail(request, manifest_id=None):
    url = request.session.get('esm_endpoint') + "/v2/et/manifest"

    headers = {
        'X-Broker-API-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "40bc1976-f185-d0db-97fe-067162bbbcfc"
    }
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        parsed_manifests = parse_manifests(json.loads(response.text))
        if parsed_manifests and manifest_id:
            return [manifest for manifest in parsed_manifests if manifest_id == manifest['id']]
        else:
            return parsed_manifests
    else:
        # todo return error message item not found
        return None


def service_catalog(request, form: ServiceForm=None, received_context={}):
    if form is None:
        form = ServiceForm()

    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    url = request.session.get('esm_endpoint', "") + "/v2/catalog"
    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "72c68829-43b4-916d-afc8-a8ecc3d7f8bd"
    }
    response = requests.request("GET", url, headers=headers)

    context = {
        'services': parse_services(json.loads(response.text)),
        'bootstrap_services': bootstrap_services(),
        'form': form,
    }
    context = {**received_context, **context}

    return render(request, 'services/index.html', context)


def build_create_manifest_request(request, cache, plan_id = None):
    manifest_id = uuid.uuid4().hex
    url = request.session.get('esm_endpoint') + "/v2/et/manifest/" + manifest_id
    print("Submitting mainfest content of type: {} with:\n{}".format(type(cache.get('manifest_content')),cache.get('manifest_content')))
    payload = {
        "id": cache.get('manifest_id') or cache.get('id'),
        "manifest_content": cache.get('template') or cache.get('manifest_content'),
        "manifest_type": cache.get('backend') or cache.get('manifest_type'),
        # support for same manifest for many plans
        "plan_id": plan_id or cache.get('plan_id'),
        "service_id": cache.get('service_id') or '',
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


def build_create_service_request(request, cache):
    url = request.session.get('esm_endpoint') + "/v2/et/catalog"

    payload = {
        'description': cache.get('service_description') or cache.get('description'),
        'id': cache.get('service_id') or cache.get('id'),
        'name': cache.get('service_name') or cache.get('name'),
        'short_name': cache.get('service_name') or cache.get('name'),
        'bindable': True,
        'plan_updateable': False,
        'metadata': {
                'extras': {
                    'preview_image': cache.get('preview_image') or '',
                    'logo_image': cache.get('logo_image') or '',
                    'service_variables': cache.get('service_variables') or ''
                }
            },
        'plans': cache.get('plans') or ''
    }
    print(payload)
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
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    form = ServiceForm(request.POST, request.FILES)

    if form.is_valid():
        cache = form.cleaned_data
        cache['preview_image'] = parse_image(request.FILES.get('preview_image'))
        cache['logo_image'] = parse_image(request.FILES.get('logo_image'))
        cache['plans'] = parse_plans(cache, request.POST)
        cache['service_variables'] = parse_variables(cache, request.POST)
        cache['service_id'] = uuid.uuid4().hex
        # TODO add support for multiple plans
        # cache['plan_id'] = uuid.uuid4().hex
        cache['manifest_id'] = uuid.uuid4().hex


        # Register Service and Plans
        url, payload, headers = build_create_service_request(request, cache)
        response = requests.request("PUT", url, data=payload, headers=headers)
        print('service registered', response.text)

        # Register Manifest
        # todo adjust to new plans
        for plan in cache['plans']:
            url, payload, headers = build_create_manifest_request(request, cache, plan['id'])
            response = requests.request("PUT", url, data=payload, headers=headers)
            print('manifest registered', response.text)

        if response.status_code == 200:
            messages.success(request,  utils.SUCCESS_MESSAGE)
            return redirect('/catalog/')

        else:
            messages.error(request, utils.ERROR_MESSAGE)
            return redirect('/catalog/')


    # from django.http import HttpResponse
    # return HttpResponse('errors' + str(form.errors))
    else:
        return service_catalog(request, form)

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url) and url is not ""


def get_selected_services(selected_indexes_raw, url):
    selected_indexes = list(map(int, selected_indexes_raw))

    print("List of Service Definitions: ", selected_indexes)
    print("URL: ", url)

    if not is_valid_url(url):
        messages.error(request, utils.INVALID_IMPORT_URL)
        return redirect('/catalog/') 

    json_file = requests.get(url).json()
    counter = 0
    selected = {}
    
    for k, v in json_file.items():
        if counter in selected_indexes:
            selected[k] = v
        counter+=1
    
    return selected
    
# TODO kubernetes locally could not be tested, since a deployment 
# in docker cannot access the host network and reach the minikube endpoint
def import_service(request):
    json_data = json.loads(json.dumps(request.POST))
    print("Received form JSON: {}".format(json_data))

    # verify ESM connection established
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    # validate URL and get what matters
    selected = get_selected_services(request.POST.getlist('service_definitions'), request.POST.get('import_service_form_url'))
    print("Filtered selected: {}".format(selected))

    responses = {}
    responses_numeric = 0
    for k,v in selected.items():
        response_temp = 0

        # Register Service and Plans
        service_cache = v['service']
        url, payload, headers = build_create_service_request(request, service_cache)
        response = requests.request("PUT", url, data=payload, headers=headers)
        print('service registered', response.text)
        if response.status_code == 200:
          response_temp += 1
            
        # Register Manifest
        for manifest_cache in v['manifests']:
            url, payload, headers = build_create_manifest_request(request, manifest_cache)
            response = requests.request("PUT", url, data=payload, headers=headers)
            print('manifest registered', response.text)
            if response.status_code == 200:
                response_temp += 1
            
        responses[k] = True if response_temp > 0 else False
        responses_numeric += response_temp

    if responses_numeric > 0:
        # TODO adapt message to show the result of each service :]
        messages.success(request,  utils.SUCCESS_MESSAGE + str(responses)) 
        return redirect('/catalog/')

    else:
        messages.error(request, utils.ERROR_MESSAGE + str(responses))
        return redirect('/catalog/')

    # base_cache = {}
    # base_cache['service_id'] = uuid.uuid4().hex
    # # cache['plan_id'] = uuid.uuid4().hex
    # base_cache['manifest_id'] = uuid.uuid4().hex


def service_detail(request, service_id=None):
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    url = request.session.get('esm_endpoint') + "/v2/catalog"
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
            context = {'service': service}
            return render(request, 'services/show.html', context)

    # todo return error message item not found
    return redirect('/catalog/')
