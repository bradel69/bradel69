import getpass
import telnetlib

HOST = "192.168.1.254"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"/device-info/show\n")
tn.write(b"quit\n")

tn.read_until(b"WAN IPv4 Address                        |")

data = ""

line = tn.read_until(b" ")
data = line.decode("utf8", "ignore").replace(' ','').replace('\r\n','')

print(data)
