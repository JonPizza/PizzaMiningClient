import requests
import time
import os
import json
import time

import trex

base_url = "https://10.0.0.247:6969/api"

def file_exsists(f):
    try:
        open(f)
    except FileExistsError:
        return False 
    else:
        return True


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


def start_mining(options):
    os.system(f'/mine/miners/t-rex {options} > out &')


def send_report():
    return requests.post(base_url + f'/report{build_qs()}', json={
        'report': trex.build_report()
    })


def handle_report_response(res):
    os.system(res.text)


def install_miner():
    os.system('chmod +x install_miner.sh')
    os.system('./install_miner.sh')


def miner_exsists():
    return file_exsists('/mine/miners/trex')


def main():
    if miner_exsists():
        start_mining()
    else:
        install_miner()
        start_mining()
    
    # while True:
    #     time.sleep(30)
    #     res = send_report()
    #     handle_report_response(res)

if __name__ == '__main__':
    main()