import sys
import bluetooth

server_address = "B8:27:EB:50:9F:B3"
port = 1
uuid = "4abeaf0f-033e-4ab1-acb6-8a087b7ccbff"

print("Finding service...")

service_matches = bluetooth.find_service(uuid = uuid)
if len(service_matches) == 0:
    print("PiPlayer service not found")
    sys.exit(0)
    
first_match = service_matches[0]
host = first_match["host"]
port = first_match["port"]
name = first_match["name"]

print("Connecting to " + name + " on " + host)

#nearby_devices = bluetooth.discover_devices()
#print(nearby_devices)

#for addr in nearby_devices:
#    a = addr
#    print(bluetooth.lookup_name(a))
#    if a == "PiServer":
#        server_address = a
#        break

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
data = sock.recv(1024)
print(str(data))

done = False
while not done:
    data_to_send = input()
    sock.send(data_to_send)
    print(sock.recv(1024))
    if int(data_to_send) == 0:
        sock.close()
        done = True

#data = sock.recv(1024)
#print(data)
