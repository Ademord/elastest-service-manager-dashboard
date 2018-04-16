from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect


class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Your Service name', max_length=100)
    plan_name = forms.CharField(label='Your Plan name', max_length=100)
    plan_details = forms.CharField(label='Your Plan Details', max_length=100)
    template = forms.CharField(label='Your Template', max_length=100, widget=forms.Textarea)


def delete_instance(request):
    import requests

    url = "http://localhost:8080/v2/service_instances/test_service_instance"

    querystring = {"service_id": "b1620b13-7d11-4abc-a762-f34a108ea49c", "plan_id": "36ed4b3e-c132-4746-af71-26dee76e59cb", "accept_incomplete": "false"}

    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "fd232188-3e1e-68c3-f1ef-79135efb9be1"
    }

    response = requests.request("DELETE", url, headers=headers, params=querystring)

    print('instance deprovisioned', response.text)
    import time
    time.sleep(1)
    return HttpResponseRedirect('/instances/')


def create_instance(request, plan_id=None):
    service = request.session['service']
    service_id = service['id']
    plan_id = service['plans'][plan_id - 1]['id']
    # from django.http import HttpResponse
    # return HttpResponse(service_id + plan_id)

    del request.session['service']
    del request.session['parsed_services']
    import requests

    url = "http://localhost:8080/v2/service_instances/test_service_instance"

    querystring = {"accept_incomplete": "false"}

    # payload = "{\n  \"organization_guid\": \"org\",\n  \"plan_id\": \"36ed4b3e-c132-4746-af71-26dee76e59cb\",\n  \"service_id\": \"b1620b13-7d11-4abc-a762-f34a108ea49c\",\n  \"space_guid\": \"space\"\n}"
    payload = "{\"organization_guid\": \"org\", \"plan_id\": \"" + plan_id + "\", \"service_id\": \"" + service_id + "\",\"space_guid\": \"space\"}"

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "7d98544d-3d9c-aa34-b6b1-4755fad9c8b6"
    }

    response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

    print('instance provisioned', response.text)
    import time
    time.sleep(5)
    return HttpResponseRedirect('/instances/')


def get_instance():

    instances = [
            {'id': '92', 'name': 'Spark', 'backend': 'Kubernetes', 'time_alive': '26 days', 'color': 'text-danger'},
            {'id': '62', 'name': 'Custom_LabCC2', 'backend': 'OpenStack', 'time_alive': '156 days',
             'color': 'text-warning'},
            {'id': '55', 'name': 'Wordpress', 'backend': 'Openshift', 'time_alive': '106 days',
             'color': 'text-success'},
            {'id': '12', 'name': 'Hurtle', 'backend': 'OpenStack', 'time_alive': '276 days', 'color': 'text-danger'},
            {'id': '43', 'name': 'Elastest', 'backend': 'Docker', 'time_alive': '20 seconds', 'color': 'text-success'},
            {'id': '31', 'name': 'Cyclops', 'backend': 'Unikernel', 'time_alive': '2 hours', 'color': 'text-success'}
        ]
    return instances


def str_to_datetime(s = "2016-03-26T09:25:55.000Z"):
    # from datetime import datetime
    # # 2018-04-11T14:39:53.7037297Z
    # f = "%Y-%m-%dT%H:%M:%S.%fZ"
    # print('received, ', s)
    # datetime = datetime.strptime(s, f)
    # return datetime
    # from stackoverflow.com/questions/28408614/time-data-2015-02-10t130000z-does-not-match-format-y-m-d-hms
    import dateutil.parser
    # '2015-02-10T13:00:00Z'
    return dateutil.parser.parse(s)


def get_running_time(started_date, now):
    td = now - started_date
    days, hours, minutes = td.days, td.seconds // 3600, (td.seconds // 60) % 60
    running_time = 0
    if days > 0:
        if days == 1:
            running_time = '{} day'.format(days)
        else:
            running_time = '{} days'.format(days)
    elif hours > 0:
        if hours == 1:
            running_time = '{} hour'.format(hours + 2)
        else:
            running_time = '{} hours'.format(hours + 2)
    elif minutes > 0:
        if minutes == 1:
            running_time = '{} minute'.format(minutes)
        else:
            running_time = '{} minutes'.format(minutes)
    else:
        running_time = '< 1 minute'
    return running_time


# TODO incomplete
def instance_catalog(request):
    # instances = get_instance()
    import requests

    url = "http://localhost:8080/v2/et/service_instances"

    headers = {
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "8a6bfa39-d96f-fa28-61d8-e3a480c937db"
    }

    response = requests.request("GET", url, headers=headers)
    import json
    instances = json.loads(response.text)
    parsed_instances = []

    for instance in instances:
        # get Status
        preview = ['status']
        status = [v for k, v in instance['context'].items() if any(possible_key in k for possible_key in preview)][0]
        color = 'text-danger'
        if status == 'running':
            color = 'text-success'

        # get Status
        preview = ['startedat']
        started_date = [v for k, v in instance['context'].items() if any(possible_key in k for possible_key in preview)][0]
        started_date = str_to_datetime(started_date)
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        running_time = get_running_time(started_date, now)

        # get id
        id = instance['context']['id']
        backend = 'Docker'

        service_name = instance['service_type']['name']

        parsed_instances.append({
            'id': id,
            'status': status,
            'time_alive': running_time,
            'started_time': str(started_date),
            'current_time': str(now),
            'color': color,
            'backend': backend,
            'name': service_name
        })

    print('Parsing Instances... 200 OK')
    from django.http import HttpResponse
    # return HttpResponse(str(parsed_instances))
    return render(request, 'instances/index.html', {'instances': parsed_instances})

# TODO incomplete
# def instance_detail(request, service_id=None):
#     # Service Loading | Display Index
#     services = ['wordpress', 'kubernetes', 'openstack', 'redis', 'elastest', 'spark', 'openshift', 'postgres',
#                 'cyclops', 'hurtle']
#     services = [{'name': s.title(), 'image_path': "assets/img/{}-icon.png".format(s)} for s in services]
#     custom = {'name': 'Custom', 'icon': 'dashboard'}
#
#     plans = [
#         {'name': 'Tiny', 'description': '2 Cores <br> 2 GB RAM', 'color': 'card-header-success'},
#         {'name': 'Small', 'description': '4 Cores <br> 4 GB RAM', 'color': 'card-header-info'},
#         {'name': 'Medium', 'description': '8 Cores <br> 8 GB RAM', 'color': 'card-header-warning'},
#         {'name': 'Big', 'description': '16 Cores <br> 16 GB RAM', 'color': 'card-header-rose'}
#     ]
#
#     return render(request, 'services/show1.html', {'service': services[service_id], 'plans': plans})
