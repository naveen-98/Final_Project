import subprocess


def get_wifi_passwords():
    command = subprocess.check_output(['nmcli', '-t', '-f', 'SSID,SECURITY,ACTIVE', 'dev', 'wifi']).decode(
        'utf-8').split('\n')
    networks = [line.split(':') for line in command if line.strip() and '*' not in line]

    wifi_info = []
    for network in networks:
        ssid = network[0]
        security = network[1]
        active = network[2] if len(network) > 2 else ''

        # Only try to get the password for networks with WPA security
        if 'WPA' in security:
            try:
                # nmcli will return the password for the currently active network only
                results = subprocess.check_output(
                    ['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', ssid]).decode(
                    'utf-8').strip()
                password = results if results else "No password found"
            except subprocess.CalledProcessError:
                password = "Cannot retrieve password"
        else:
            password = "No WPA security"

        wifi_info.append((ssid, password, active))

    return wifi_info


def display_wifi_passwords():
    wifi_info = get_wifi_passwords()
    print("{:<30}|  {:<30}|  {:<}".format("SSID", "Password", "Active"))
    print("-" * 70)
    for ssid, password, active in wifi_info:
        print("{:<30}|  {:<30}|  {:<}".format(ssid, password, active))


if __name__ == "__main__":
    display_wifi_passwords()
