# -*- coding: utf-8 -*-

from config.device_config import CONFIG
from device_model.dnac import DNAC
from device_model.nx9kv import Nx9kv

if __name__ == '__main__':
    # target device
    nx9kv_1 = Nx9kv(CONFIG['nx9kv_1'])
    dnac = DNAC(CONFIG['dnac'])
