import os
import requests

host = '127.0.0.1'
port = 4067

def build_url(path):
    return f'http://{host}:{port}/{path}'

def get_summary():
    return requests.get(build_url('summary'))

def get_gpus_from_summary(summary):
    gpus = []
    for gpu in summary['gpus']:
        gpus.append({
            'id': gpu['device_id'],
            'fan': gpu['fan_speed'],
            'temp': gpu['temperature'],
            'name': gpu['name'],
            'hashrate': gpu['hashrate_minute'],
        })

def build_report():
    summary = get_summary()
    gpus = get_gpus_from_summary(summary)
    return {
        'uptime': summary['uptime'],
        'gpus': gpus,
    }