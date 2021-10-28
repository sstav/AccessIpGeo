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
    compare_date = "24/Oct/2021"
    use_date = input("Include the date: " + compare_date + " : (Yes \ No) Default(No) : ")
    if use_date.lower() == "yes":
        use_date = True
    else:
        use_date = False

    for line in file.readlines():
        ip = line.split(" ")[0]
        action = line.split('] "')[1][:-2]
        date_line = str(line.split('[')[1].split(']')[0].split(" ")[0]).split(":")[0]
        if not valid_ip(ip):
            continue
        if use_date and date_line.lower() != compare_date.lower():
            continue

        response = requests.get("https://geolocation-db.com/json/" + ip + "&position=true").json()
        response["date"] = date_line
        response["action"] = action

        if valid_ip(response['IPv4']):
            print(response)


# Main

if __name__ == '__main__':
    get_list_details("access.log")
