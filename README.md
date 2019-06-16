# c61ebc04

## 需求

实现一个网络软件，完成接收事件、故障告警，及时发现和快速定位有线或无线网络的问题等功能，让网管人员可以随时随地掌握校园网的健康状况，预先发现网络故障隐患，及时排除网络故障。

## 目录结构


|目录|描述|
|:---:|:---:|
|/config|dnac与nx9kv的相关设置|
|/device_model|dnac与nx9kv的模型，拥有对dnac/nx9kv执行操作的功能函数|
|/main_api|dnac与nx9kv的API测试|
|/main.py|正式入口文件|


## 思路

### Step 1

依据用户提供的dnac、nx9kv的信息（域名、端口、账号密码等）预设置dnac以及多台nx9kv。

```python
from config.device_config import CONFIG
from device_model.dnac import DNAC
from device_model.nx9kv import Nx9kv

nx9kv_1 = Nx9kv(CONFIG['nx9kv_1'])
dnac = DNAC(CONFIG['dnac'])
```

### Step 2

可以通过cli指令配置nx9kv

```python
aaa_accounting = nx9kv_1.cli('cli_show', 'show aaa accounting')
print(aaa_accounting)
```

可以通过调用API获取dnac的相关信息、控制dnac，通过调用部分API可以获取设备、链路的健康状况，以达到故障告警的要求，还能推断出故障出现的地方

```python
list_network_devices = dnac.get_url('network-device')['response']
dnac.get_url('network-health')
```

### Step 3

给dnac配置代理，用来接收事件通知

```python
dnac.setup_proxy()
```


## 未知及未解决

1、**dnac代理服务器的搭建完全未知**

2、**获取设备、链路的健康信息的具体API，以及如何通过返回信息判断设备是否健康、发生故障的地方**

3、未有交互式界面