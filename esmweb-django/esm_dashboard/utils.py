from django.shortcuts import render
import requests


def endpoint_alive(url):
    try:
        r = requests.head(url + '/ui/')
        print(r.status_code)
        return r.status_code == 200
    except:
        return False


def esm_endpoint_check(request):
    print(request.build_absolute_uri())
    endpoint = request.session.get('esm_endpoint')
    if not endpoint:
        return redirect_first_time(request)

    request.session['esm_endpoint'] = endpoint
    if not endpoint_alive(endpoint):
        return redirect_offline(request)

    return None


def redirect_first_time(request):
    print('redirecting to FIRSTTIME')
    context = {
        "endpoint": 'http://localhost:8080',
        "message": 'First time connecting to the ESM?',
        "sub_message": 'This is the currently configured endpoint.',
        "button_message": 'Looks good!',
        "form_action": '/configure'
    }

    return render(request, 'esm_connect.html', context)


def redirect_offline(request):
    print('redirecting to OFFLINE')
    context = {
        "endpoint": 'http://localhost:8080',
        "message": 'This is embarassing.',
        "sub_message": 'ESM is offline. Want to change the endpoint?',
        "button_message": 'Retry!',
        "form_action": '/configure'
    }

    return render(request, 'esm_connect.html', context)


def set_esm_endpoint(request):
    endpoint = request.POST.get('new_endpoint', 'http://localhost:8080')
    request.session['esm_endpoint'] = endpoint

    if not endpoint_alive(endpoint):
        return redirect_offline(request)

    return render(request, 'welcome.html')

