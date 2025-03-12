from cvprac import cvp_client as cvp_client
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
# cvp2 = "192.168.0.6"
# cvp3 = "192.168.0.7"
cvp_user = "arista"
cvp_password = "aristax1234"

client = cvp_client.CvpClient()

client.connect([cvp1], cvp_user, cvp_password)

tasks = client.api.get_tasks_by_status('Pending')

for task in tasks:
    taskId = task['workOrderId']
    hostname = task['workOrderDetails']['netElementHostName']
    print(f"{taskId} for {hostname}")
    client.api.execute_task(taskId)