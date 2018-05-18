from django.shortcuts import render
from django.shortcuts import redirect
import requests
import os


ERROR_TITLE = 'Oh no!'
SUCCESS_TITLE = 'Success!'
INFO_TITLE = 'Info!'

SUCCESS_MESSAGE = 'Operation was successfully executed.'
ERROR_MESSAGE = 'Oops! Something went wrong, \n you should try again.'

# instances
SUCCESS_PROVISION_MESSAGE = 'Your Service Instance has been deployed.'
ERROR_PROVISION_MESSAGE = 'Oops! Something went wrong, \n Check your variables and try again.'
SUCCESS_DEPROVISION_MESSAGE = 'Your Service Instance has been deprovisioned.'
ERROR_DEPROVISION_MESSAGE = ERROR_MESSAGE

notify_error_dict = {
    'notify_title': ERROR_TITLE,
    'notify_message': ERROR_MESSAGE,
    'notify_fa_icon': 'fa-thumbs-down',
    'notify_fa_color': 'error',
    'button_message': 'Try again'
}

notify_info_dict = {
    'notify_title': INFO_TITLE,
    'notify_message': 'unset',
    'notify_fa_icon': 'fa-info',
    'notify_fa_color': 'success neutral',
    'button_message': 'OK'
}

notify_success_dict = {
    'notify_title': SUCCESS_TITLE,
    'notify_message': SUCCESS_MESSAGE,
    'notify_fa_icon': 'fa-check',
    'notify_fa_color': 'success',
    'button_message': 'OK'
}


def endpoint_alive(url):
    try:
        r = requests.head(url)
        print(r.status_code)
        return r.status_code == 404
    except:
        return False


def esm_endpoint_check(request, original_url=None):
    print("checking esm_alive", request.build_absolute_uri())
    request.session['original_url'] = request.build_absolute_uri()

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
        "endpoint": request.session.get('esm_endpoint') or os.getenv("ET_ESM_API") or 'http://localhost:8080',
        "message": 'First time connecting to the ESM?',
        "sub_message": 'This is the currently configured endpoint.',
        "button_message": 'Looks good!',
        "form_action": '/configure'
    }

    return render(request, 'esm_connect.html', context)


def redirect_offline(request):
    print('redirecting to OFFLINE')
    context = {
        "endpoint": request.session.get('esm_endpoint') or os.getenv("ET_ESM_API") or 'http://localhost:8080',
        "message": 'This is embarassing.',
        "sub_message": 'ESM is offline. Want to change the endpoint?',
        "button_message": 'Retry!',
        "form_action": '/configure'
    }

    return render(request, 'esm_connect.html', context)


def set_esm_endpoint(request):

    print(request.POST.__dict__)
    endpoint = request.POST.get('esm_endpoint') or os.getenv("ET_ESM_API") or 'http://localhost:8080'
    request.session['esm_endpoint'] = endpoint
    print('changing endpoint', request.session['esm_endpoint'])
    if not endpoint_alive(endpoint):
        return redirect_offline(request)

    print('redirecting after configure...')
    return redirect(request.session.get('original_url', 'welcome.html'))
    # return render(request, 'welcome.html')

