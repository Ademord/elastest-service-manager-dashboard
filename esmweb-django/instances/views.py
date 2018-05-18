from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import json
import requests
from services.views import manifest_detail
from esm_dashboard.utils import esm_endpoint_check
import esm_dashboard.utils as utils
from django.contrib import messages
import uuid


class ServiceForm(forms.Form):
    service_name = forms.CharField(label='Your Service name', max_length=100)
    plan_name = forms.CharField(label='Your Plan name', max_length=100)
    plan_details = forms.CharField(label='Your Plan Details', max_length=100)
    template = forms.CharField(label='Your Template', max_length=100, widget=forms.Textarea)


def delete_instance(request, parameter):
    # todo add Are you sure? modal
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    url = request.session.get('esm_endpoint') + "/v2/service_instances/{}".format(parameter)

    querystring = {"service_id": "b1620b13-7d11-4abc-a762-f34a108ea49c", "plan_id": "36ed4b3e-c132-4746-af71-26dee76e59cb", "accept_incomplete": "false"}

    headers = {
        'Accept': "application/json",
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "fd232188-3e1e-68c3-f1ef-79135efb9be1"
    }

    response = requests.request("DELETE", url, headers=headers, params=querystring)
    print('instance deprovisioned', response.text)

    if response.status_code == 200:
        messages.success(request, utils.SUCCESS_DEPROVISION_MESSAGE)
        return redirect('/instances/index.html')

    else:
        messages.error(request, utils.ERROR_DEPROVISION_MESSAGE)
        return redirect('/instances/index.html')


def create_instance(request, parameter=None):
    # todo block to create an instance thats already running (plan, service) too often
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    if 'k' in parameter:
        service_id, plan_id = parameter.split("k")
        url = request.session.get('esm_endpoint') + "/v2/service_instances/" + uuid.uuid4().hex

        querystring = {"accept_incomplete": "false"}

        payload = "{\"organization_guid\": \"org\", \"plan_id\": \"" + plan_id + "\", \"service_id\": \"" + service_id + "\",\"space_guid\": \"space\"}"

        headers = {
           'Accept': "application/json",
           'Content-Type': "application/json",
           'X-Broker-Api-Version': "2.12",
           'Cache-Control': "no-cache",
           'Postman-Token': "7d98544d-3d9c-aa34-b6b1-4755fad9c8b6"
        }

        response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)
        print('instance', response.text)
        if response.status_code == 200:
            messages.success(request, utils.SUCCESS_PROVISION_MESSAGE)
            return redirect('/instances/')

        else:
            messages.error(request, response.text)
            return redirect('/instances/'.format(service_id))
    else:
        # this would only happen when someone tries to forge a request
        messages.error(request, utils.ERROR_MESSAGE)
        return redirect('/instances/')


def bootstrap_instances():

    instances = [
            {'id': '92', 'service_name': 'Spark', 'backend': 'Kubernetes', 'time_alive': '26 days', 'color': 'text-danger'},
            {'id': '62', 'service_name': 'Custom_LabCC2', 'backend': 'OpenStack', 'time_alive': '156 days',
             'color': 'text-warning'},
            {'id': '55', 'service_name': 'Wordpress', 'backend': 'Openshift', 'time_alive': '106 days',
             'color': 'text-success'},
            {'id': '12', 'service_name': 'Hurtle', 'backend': 'OpenStack', 'time_alive': '276 days', 'color': 'text-danger'},
            {'id': '43', 'service_name': 'Elastest', 'backend': 'Docker', 'time_alive': '20 seconds', 'color': 'text-success'},
            {'id': '31', 'service_name': 'Cyclops', 'backend': 'Unikernel', 'time_alive': '2 hours', 'color': 'text-success'}
        ]
    return instances


def str_to_datetime(s = "2016-03-26T09:25:55.000Z"):
    # from stackoverflow.com/questions/28408614/time-data-2015-02-10t130000z-does-not-match-format-y-m-d-hms
    import dateutil.parser
    # '2015-02-10T13:00:00Z'
    return dateutil.parser.parse(s)


def get_running_time(started_date, now):
    from datetime import timedelta
    print(now)
    print(started_date)
    # bug: the time on the ESM is a bit off by 15sec
    td = now - (started_date - timedelta(seconds=30))

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


def parse_instances(request, instances):
    parsed_instances = []

    for instance in instances:
        # get Status
        preview = ['status']
        type([v for k, v in instance['context'].items() if any(possible_key in k for possible_key in preview)])
        status = [v for k, v in instance['context'].items() if any(possible_key in k for possible_key in preview)][0]
        # color and icon for instances.index/.show
        color = 'danger'
        status_icon = 'clear'
        if status == 'running':
            color = 'success'
            status_icon = 'done'

        # get Status
        preview = ['startedat']
        started_date = [v for k, v in instance['context'].items() if any(possible_key in k for possible_key in preview)][0]
        started_date = str_to_datetime(started_date)
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        running_time = get_running_time(started_date, now)

        # get id
        id = instance['context']['id']
        ip = next(v for (k, v) in instance['context'].items() if '_Ip' in k)
        port = next(v for (k, v) in instance['context'].items() if 'portbindings' in k)
        import ast
        port = ast.literal_eval(port)[0]['HostPort']

        # prerequisites
        manifest_id = instance['context']['manifest_id']
        # this could in an impossible case break.
        manifest = manifest_detail(request, manifest_id)[0]
        # get the plan
        plan = None
        for plan in instance['service_type']['plans']:
            if plan['id'] == manifest['id']:
                plan = plan
                break

        parsed_instances.append({
            'id': id,
            'color': color,
            'status_icon': status_icon,

            'service_id': instance['service_type']['id'],
            'service_name': instance['service_type']['name'],
            'service_description': instance['service_type']['description'],

            'plan_name': plan['name'],
            'plan_description': plan['description'],
            'plan': plan,

            'backend': manifest['manifest_type'],
            'template': manifest['manifest_content'],

            'status': status,
            'time_alive': running_time,
            'started_time': str(started_date),
            'current_time': str(now),
            'ip': ip,
            'port': port
        })

    return parsed_instances


def instance_catalog(request, previous_context={}):
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    url = request.session.get('esm_endpoint') + "/v2/et/service_instances"
    headers = {
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "8a6bfa39-d96f-fa28-61d8-e3a480c937db"
    }
    response = requests.request("GET", url, headers=headers)

    parsed_instances = parse_instances(request, json.loads(response.text))
    # return render(request, 'instances/index.html', {'instances': parsed_instances + bootstrap_instances()})
    context = {
        'instances': parsed_instances,
        'bootstrap_instances': bootstrap_instances(),
    }
    context = {**context, **previous_context}
    return render(request, 'instances/index.html', context)


def instance_detail(request, instance_id=None):
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    url = request.session.get('esm_endpoint') + "/v2/et/service_instances/{}".format(instance_id)

    headers = {
        'X-Broker-Api-Version': "2.12",
        'Cache-Control': "no-cache",
        'Postman-Token': "66fba99d-2fe6-d11e-0424-1488c889132b"
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        parsed_instance = parse_instances(request, [json.loads(response.text)])[0]

        host = 'kafka.cloudlab.zhaw.ch'
        port = 8086
        user = 'root'
        password = 'pass1234'
        dbname = 'user-1-elastest_tss'
        query = 'select * from "service-docker-stats" group by "container-name" order by desc limit 10;'
        from influxdb import InfluxDBClient

        client = InfluxDBClient(host, port, user, password, dbname)

        print("Querying data: " + query)
        result = client.query(query)
        # name = result.raw['series'][0]['name']  # str
        # columns = result.raw['series'][0]['columns']  # []
        # values = result.raw['series'][0]['values']  # [[]]
        containers = []
        for serie in result.raw['series']:
            CPU_series = []
            RAM_series = []
            name = serie['tags']['container-name']
            for x in serie['values']:
                CPU_series.append(x[3])
            for x in serie['values']:
                RAM_series.append(x[5])
            containers.append([name, CPU_series, RAM_series])
        print(containers)
        return render(request, 'instances/show.html', {'instance': parsed_instance, 'containers': json.dumps(containers)})
    else:
        # todo return error message isntance not found
        return instance_catalog(request)
