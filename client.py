#!/usr/bin/python

import math
import urllib.request, urllib.error
import _thread
import time

OSCILLATION_PERIOD_SECONDS = 300.0


def send_request(method, path):
    data = None
    if method == 'POST':
        data = ''
    try:
        urllib.request.urlopen('http://localhost:8001' + path, data)
    except urllib.error.HTTPError:
        pass
    except:
        pass

start = time.time()

def oscillation_factor():
    return 2 + math.sin(math.sin(2 * math.pi * (time.time() - start) / OSCILLATION_PERIOD_SECONDS))

def request_worker(method, path, sleep):
    while True:
        send_request(method, path)
        time.sleep(sleep * oscillation_factor())

def start_request_workers():
    _thread.start_new_thread(request_worker, ('GET', '/', .01))
    _thread.start_new_thread(request_worker, ('GET', '/', .15))
    _thread.start_new_thread(request_worker, ('GET', '/', .02))
    _thread.start_new_thread(request_worker, ('GET', '/', .1))
    _thread.start_new_thread(request_worker, ('GET', '/', .5))
