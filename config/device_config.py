# -*- coding: utf-8 -*-

""" config """

CONFIG = {
    'dnac': {
        'protocol': 'https',
        'host': 'sandboxdnac.cisco.com',
        'port': 443,
        'username': 'devnetuser',
        'password': 'Cisco123!',
        'proxy': {
            'proxy_settings': {
                'httpProxyHost': '',
                'httpsProxyHost': '',
                'httpProxyPort': '',
                'httpsProxyPort': '',
                'httpNonProxyHosts': '',
            },
            'username': '',
            'password': ''
        }
    },
    'nx9kv_1': {
        'protocol': 'https',
        'host': 'sbx-nxos-mgmt.cisco.com',
        'aaa_attributes': {
            'name': 'admin',
            'pwd': 'Admin_1234!'
        }
    },
}
