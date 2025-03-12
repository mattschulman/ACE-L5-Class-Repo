from cvprac import cvp_client as cvp_client
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
# cvp2 = "192.168.0.6"
# cvp3 = "192.168.0.7"
cvp_user = "arista"
cvp_password = "arista1234"

client = cvp_client.CvpClient()

client.connect([cvp1], cvp_user, cvp_password)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

configlets = client.api.get_configlets(start=0,end=0)

for item in configlets['data']:
    file = open(directory+'/'+item['name']+'.txt','w')
    file.write(item['config'])
    file.close()