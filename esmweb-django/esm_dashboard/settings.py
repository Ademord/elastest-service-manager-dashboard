from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from services.views import service_catalog, create_service, import_service, service_detail
from instances.views import instance_catalog, create_instance, delete_instance, instance_detail
from esm_dashboard.utils import esm_endpoint_check, set_esm_endpoint

import requests
import json
import os

# InfluxDB
from influxdb import InfluxDBClient

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DEBUG = True
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3nouuuugh15'
ROOT_URLCONF = __name__
DATABASES = {
    'default': {'ENGINE': 'django.db.backends.dummy'}
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prettyjson',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/usr/src/app/templates/'],
        # 'DIRS': ['/Users/ribr/Documents/elastest-service-manager-dashboard/esmweb-django/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Cookie Domain
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# def test(request):
#     title = 'Tinyapp'
#     author = 'Vitor Freitas'
#     return render(request, 'tests/login.html', {'title': title, 'author': author})


def test(request, host='kafka.cloudlab.zhaw.ch', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'pass1234'
    dbname = 'user-1-elastest_tss'
    query = 'select * from "service-docker-stats" group by "container-name";'

    client = InfluxDBClient(host, port, user, password, dbname)

    print("Querying data: " + query)
    result = client.query(query)

    name = result.raw['series'][0]['name']  # str
    columns = result.raw['series'][0]['columns']  # []
    values = result.raw['series'][0]['values']  # [[]]

    return HttpResponse("{}".format(str([serie['tags']['container-name'] for serie in result.raw['series']])))


def welcome(request):
    must_configure = esm_endpoint_check(request)
    if must_configure:
        return must_configure

    return render(request, 'welcome.html')


# error views
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf.urls import (handler400, handler403, handler404, handler500 )

# handler400 = 'esm_dashboard.settings.bad_request'
# handler403 = 'settings.permission_denied'
handler400 = 'esm_dashboard.settings.bad_request'
handler404 = 'esm_dashboard.settings.page_not_found'
handler500 = 'esm_dashboard.settings.server_error'
# handler500 = 'esm_dashboard.settings.server_error'


# HTTP Error 400
def bad_request(request, exception):
    response = render_to_response('400.html')
    response.status_code = 400
    return render(request, 'welcome.html')


# HTTP Error 404
def page_not_found(request, exception):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


# HTTP Error 500
def server_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response

# Respective imports for each method in each controller are listed above.
urlpatterns = [
    path('',                            service_catalog,            name='welcome_page'),
    path('catalog',                     service_catalog,    name='service_catalog_page'),
    path('catalog/',                    service_catalog,    name='service_catalog_page'),
    path('catalog/create',              create_service,    name='service_catalog_page'),
    path('catalog/import',              import_service,    name='service_catalog_page'),
    path('catalog/<str:service_id>',    service_detail,     name='service_detail_page'),
    path('catalog/<str:service_id>/',   service_detail,     name='service_detail_page'),

    path('instances',                   instance_catalog,   name='instance_catalog_page'),
    path('instances/',                  instance_catalog,   name='instance_catalog_page'),
    path('instances/create',            create_instance,   name='instance_catalog_page'),
    path('instances/create/<str:parameter>',     create_instance,   name='instance_catalog_page'),
    path('instances/delete/<str:parameter>',     delete_instance,   name='instance_catalog_page'),
    path('instances/<str:instance_id>',     instance_detail,   name='instance_catalog_page'),

    path('configure', set_esm_endpoint, name='set_esm_endpoint_page'),
    path('test', test, name='test_page')
]

STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')