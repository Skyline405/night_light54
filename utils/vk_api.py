from urllib.parse import urlencode
from django.conf import settings

import requests


def send_request(method_name, params):
    req_url = settings.VK_API_URL.format(
        method=method_name,
        params=urlencode(params),
        token=settings.VK_TOKEN,
        version=settings.VK_API_VERSION,
    )
    return requests.get(req_url)
