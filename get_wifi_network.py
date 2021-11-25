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

tn.write(b"lan/dhcp/show\n")
tn.write(b"quit\n")

tn.read_until(b"Type")
tn.read_until(b"\r\n")
tn.read_until(b"\r\n")

cols = [0]*7
data = []

line = tn.read_until(b"\r\n")
line_d = line.decode("utf8", "ignore").replace(' ','').replace('\r\n','')
while line.decode("utf8", "ignore")[0] != "+":
  cols = line_d[1:-1].split("|")
  line = tn.read_until(b"\r\n")
  line_d = line.decode("utf8", "ignore").replace(' ','').replace('\r\n','')
  data.append(cols)

print(data)
