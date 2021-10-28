import socket

# Functions
import requests as requests


def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        # legal
        return True
    except socket.error:
        return False


# Not legal
def get_list_details(file_name):
    file = open(file_name)

    for line in file.readlines():
        ip = line.split(" ")[0]
        if not valid_ip(ip):
            continue

        response = requests.get("https://geolocation-db.com/json/" + ip + "&position=true").json()
        if valid_ip(response['IPv4']):
            print(response)


# Main

if __name__ == '__main__':
    get_list_details("access.log")
