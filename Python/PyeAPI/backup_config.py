import pyeapi
import yaml
import os

pyeapi.load_config('eapi.conf')

# connect = pyeapi.connect_to('leaf1')
file = open('switches.yml', 'r')
switches_dict = yaml.safe_load(file)
directory = 'configs'
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

for switch in switches_dict['devices']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True') # Gets as a string instead of a list
    config_file_path = directory+'/'+switch+'.cfg'
    file = open(config_file_path, 'w')
    file.write(running_config)
    file.close()
    print(f"Backed up {switch} config to {config_file_path}")


