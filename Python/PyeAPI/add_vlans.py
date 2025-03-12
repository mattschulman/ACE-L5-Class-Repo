import pyeapi
import yaml

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    for vlan in vlan_dict['vlans']:
        vlan_api = connect.api('vlans')
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding vlan {vlan_id} with name {vlan_name}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)