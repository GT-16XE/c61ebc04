# -*- coding: utf-8 -*-

# https://developer.cisco.com/site/dna-center-rest-api/
# https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-platform-overview

import sys
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, "../"))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)

from config.device_config import CONFIG
from device_model.dnac import DNAC

if __name__ == '__main__':
    # target device
    dnac = DNAC(CONFIG['dnac'])

    list_network_devices = dnac.get_url('network-device')['response']

    print(
        "{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".format("hostname", "mgmt IP", "serial", "platformId", "SW Version",
                                                            "role", "Uptime"))

    for device in list_network_devices:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".format(device['hostname'], device['managementIpAddress'],
                                                                  device['serialNumber'], device['platformId'],
                                                                  device['softwareVersion'], device['role'], uptime))
