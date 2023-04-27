import subprocess

config_paths = ["/etc/openvpn/vpnbook-us1-udp25000.ovpn", "/etc/openvpn/vpnbook-us2-udp25000.ovpn", "/etc/openvpn/vpnbook-fr1-udp25000.ovpn", "/etc/openvpn/vpnbook-fr8-udp25000.ovpn", "/etc/openvpn/vpnbook-ca222-udp25000.ovpn"]
config_path = "/etc/openvpn/vpnbook-us1-udp25000.ovpn"
server_name = "us1.vpnbook.com"
username = "vpnbook"
password = "3ev7r8m"


def connect(config_path):
    # Construct the command to connect to the VPN server
    command = [
        "sudo",            # Run the command as superuser
        "openvpn",         # The OpenVPN command
        "--config",        # Specify the configuration file
        config_path,
        "--auth-user-pass",  # Specify the username/password file
        "/dev/stdin",
        "--verb",          # Increase the verbosity of the output
        "3"
    ]

    # Start the OpenVPN process and send the username/password to stdin
    with subprocess.Popen(command, stdin=subprocess.PIPE) as process:
        # Construct the username/password string with a newline separator
        userpass = f"{username}\n{password}\n".encode("utf-8")

        # Send the username/password to stdin
        process.stdin.write(userpass)
        process.stdin.flush()

        # # Wait for the process to finish
        # process.wait()
        # Wait for the VPN connection to be established
        while True:
            output = process.stdout.readline()
            if "Initialization Sequence Completed" in output.decode("utf-8"):
                return 1
        # now you are connected to vpn
        return 0


def stop():
    cmd = ["sudo", "killall", "openvpn"]
    subprocess.run(cmd)


if __name__ == "__main__":
    connect(config_path)