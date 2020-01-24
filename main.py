import requests
import time
import os
import json

import trex

base_url = "https://localhost:6969/api"


def get_username():
    return open('username').read()


def get_rig_name():
    return open('rig').read()


def build_qs():
    return f'?user={get_username()}&rig={get_rig_name()}'


def do_get(path):
    return requests.get(f'{base_url}{path}{build_qs()}')


def get_miner():
    miner_url = do_get(f'/miner-url{build_qs()}').text
    os.system(f'curl {miner_url} > /mine/miners/t-rex')


def start_mining(miner_path, options, out_file):
    os.system(f'{miner_path} {options} > {out_file} &')


def send_report():
    return requests.post(base_url + f'/report{build_qs()}', json={
        'report': trex.build_report()
    })


def handle_report_response(res):
    j = json.loads(res.text)
    if 'run' in j:
        os.system(j)

def main():
    start_mining()