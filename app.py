from vpn.vpn import connect, stop, config_path
from chromeProfiles.chromeProfile import openChrome, profile_folder_name
import time

import subprocess

# Run the trigger_vpn function to start the VPN connection
vpn_connected = connect(config_path)

if vpn_connected == 1:
    # VPN connection established, launch Chrome
    chrome_script = "/home/sai/.config/google-chrome/Profile 1"
    subprocess.Popen(["python", chrome_script])
else:
    # VPN connection failed or was interrupted
    print("VPN connection failed")
