from django.http import HttpResponse
import os
from django.shortcuts import render
from django.urls import path
from services.views import service_catalog
from services.views import service_detail

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3nouuuugh15'
ROOT_URLCONF = __name__

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/usr/src/app/templates/'],
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


def about(request):
    title = 'Tinyapp'
    author = 'Vitor Freitas'
    return render(request, 'about.html', {'title': title, 'author': author})


def welcome(request):
    return render(request, 'welcome.html')


def instance_catalog(request):
    instances = [
        {'id': '92', 'name': 'Spark', 'backend': 'Kubernetes', 'time_alive': '26 days', 'color': 'text-danger'},
        {'id': '62', 'name': 'Custom_LabCC2', 'backend': 'OpenStack', 'time_alive': '156 days', 'color': 'text-warning'},
        {'id': '55', 'name': 'Wordpress', 'backend': 'Openshift', 'time_alive': '106 days', 'color': 'text-success'},
        {'id': '12', 'name': 'Hurtle', 'backend': 'OpenStack', 'time_alive': '276 days', 'color': 'text-danger'},
        {'id': '43', 'name': 'Elastest', 'backend': 'Docker', 'time_alive': '20 seconds', 'color': 'text-success'},
        {'id': '31', 'name': 'Cyclops', 'backend': 'Unikernel', 'time_alive': '2 hours', 'color': 'text-success'}
    ]
    return render(request, 'instances/index.html', {'instances': instances})


urlpatterns = [
    path('',                            welcome,            name='welcome_page'),
    path('catalog',                     service_catalog,    name='service_catalog_page'),
    path('catalog/',                    service_catalog,    name='service_catalog_page'),
    path('catalog/<int:service_id>',    service_detail,     name='service_detail_page'),
    path('catalog/<int:service_id>/',   service_detail,     name='service_detail_page'),
    path('instances',                   instance_catalog,   name='instance_catalog_page'),
    path('instances/',                  instance_catalog,   name='instance_catalog_page'),
    path('test', about, name='catalogpage')
]

STATIC_URL = '/static/'

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')