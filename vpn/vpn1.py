from openvpn_api import OpenvpnAPI

# Specify the path to the OpenVPN configuration file
config_path = "/etc/openvpn/vpnbook-us1-udp25000.ovpn"

# Specify the name of the profile you want to use
profile_name = "vpnbook"

# Specify the name of the server you want to connect to
server_name = "vpnbook-us1-udp25000.ovpn"

# Create an instance of the OpenvpnAPI class
api = OpenvpnAPI()

# Load the OpenVPN configuration file for the specified profile
api.load_config(config_path, profile_name)

# Connect to the specified VPN server
api.connect(server_name)
