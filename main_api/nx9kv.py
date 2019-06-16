# -*- coding: utf-8 -*-

# https://developer.cisco.com/docs/cisco-nexus-9000-series-nx-api-cli-reference-release-9-2x/#!aaa-commands

import sys
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, "../"))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)

from config.device_config import CONFIG
from device_model.nx9kv import Nx9kv

if __name__ == '__main__':
    # target device
    nx9kv_1 = Nx9kv(CONFIG['nx9kv_1'])

    # input command type and command string into the device
    aaa_accounting = nx9kv_1.cli('cli_show', 'show aaa accounting')
    print(aaa_accounting)

    conf_t = nx9kv_1.cli('cli_conf', 'configure terminal')
    print(conf_t)
