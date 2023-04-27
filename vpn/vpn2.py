import subprocess

# Specify the path to the OpenVPN configuration file
config_path = "/etc/openvpn/vpnbook-us1-udp25000.ovpn"

# Specify the name of the VPN server you want to connect to
server_name = "us1.vpnbook.com"

# Specify the port number used by the VPN server
port_number = "25000"

# Specify the authentication details (if required)
username = "vpnbook"
password = "3ev7r8m"

# Construct the OpenVPN command with the appropriate arguments
cmd = ["sudo", "openvpn", "--config", config_path, "--remote", server_name, port_number]

if username and password:
    cmd += ["--auth-user-pass", "<(echo '{0}\n{1}')".format(username, password)]

# Use the subprocess module to run the OpenVPN command
p = subprocess.Popen(cmd)

# Wait for the OpenVPN command to finish
p.wait()

# i connected to vpn by running
# sudo openvpn /etc/openvpn/vpnbook-us1-udp25000.ovpn
# and then enter username and password
# how can i do this in python script