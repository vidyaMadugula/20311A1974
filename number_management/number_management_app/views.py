from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from time import time


# @require_GET
# def get_numbers(request):
#     # urls = request.GET.getlist('url')
#     test_case_url = 'http://localhost:port/numbers?url=http://104.211.219.98/numbers/primes&url=http://104.211.219.98/numbers/fibo &url=http://104.211.219.98/numbers/odd'
#     test_case_output_urls = test_case_url.GET.getlist('url')
#     numbers = set()
#
#     start_time = time()
#     # for url in urls:
#     for url in test_case_output_urls:
#         try:
#             response = requests.get(url, timeout=0.5)
#             if response.status_code == 200:
#                 data = response.json()
#                 if 'numbers' in data:
#                     numbers.update(data['numbers'])
#         except requests.exceptions.Timeout:
#             pass
#
#     sorted_numbers = sorted(numbers)
#     response_data = {'numbers': sorted_numbers}
#     return JsonResponse(response_data)


import requests
from urllib.parse import urlparse, parse_qs
from django.http import JsonResponse
from time import time


def get_numbers(request):
    url = 'http://localhost:port/numbers?url=http://104.211.219.98/numbers/primes&url=http://104.211.219.98/numbers/fibo&url=http://104.211.219.98/numbers/odd'

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    urls = query_params.get('url', [])
    numbers = set()

    start_time = time()
    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                if 'numbers' in data:
                    numbers.update(data['numbers'])
        except requests.exceptions.Timeout:
            pass

    sorted_numbers = sorted(numbers)
    response_data = {'numbers': sorted_numbers}
    return JsonResponse(response_data)

