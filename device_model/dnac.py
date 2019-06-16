# -*- coding: utf-8 -*-

""" Cisco DNA Center """

import requests
import sys
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


class DNAC(object):
    def __init__(self, config):
        self.config_protocol = config['protocol']
        self.config_host = config['host']
        self.config_port = config['port']
        self.config_username = config['username']
        self.config_password = config['password']

    def get_auth_token(self):
        login_url = "{}://{}:{}/dna/system/api/v1/auth/token".format(self.config_protocol, self.config_host,
                                                                     self.config_port)
        # Cisco DNA Center设备上有自签名证书，不是由CA颁发的，所以参数verify置False
        result = requests.post(url=login_url, auth=HTTPBasicAuth(self.config_username, self.config_password),
                               verify=False)
        # 如果请求有任何问题，并且有任何响应代码不同于200 OK，则raise_for_status()将退出脚本并显示一条Traceback消息，指示请求的问题
        result.raise_for_status()

        # token只有10分钟有效期
        return result.json()["Token"]

    def get_url(self, path):
        url = "{}://{}:{}/dna/intent/api/v1/{}".format(self.config_protocol, self.config_host, self.config_port, path)
        token = self.get_auth_token()
        headers = {
            'X-auth-token': token
        }
        try:
            response = requests.get(url, headers=headers, verify=False)
        except requests.exceptions.RequestException as cerror:
            print("Error processing request", cerror)
            sys.exit(1)

        return response.json()
