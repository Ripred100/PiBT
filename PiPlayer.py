import bluetooth, subprocess
from subprocess import STDOUT, PIPE

def decode_data(d):
    code = int(d)
    result = ""
    commands = ["Pause", "Play", "Next Song", "Previous Song", "Shuffle"]
    try:
        result = commands[code]
    except:
        result = "Invalid command"
    
    print(result)
    return result


java = subprocess.Popen('java PlayAudioTest', stdin = PIPE, stdout = PIPE, stderr = STDOUT, shell = True, text = True)

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
uuid = "4abeaf0f-033e-4ab1-acb6-8a087b7ccbff"

port = 1
server_sock.bind(("", port))
server_sock.listen(1)
bluetooth.advertise_service(server_sock, "PiPlayer Service", uuid)

print("Waiting for connection...")
client_sock, address = server_sock.accept()
client_sock.send("Connection accepted")
print("Accepted connection from " + str(address))

done = False


while not done:
    data = client_sock.recv(1024)
    data = str(data, 'utf-8')
    print(data)
    #client_sock.send("Data received")
    print("Data received: " + data)
    data_to_send = decode_data(data)
    
    java.communicate("2")
    
    client_sock.send(data_to_send)
    if int(data) == 0:
        client_sock.close()
        server_sock.close()
        done = True



#client_sock.send("To get to the other side")



#nearby_devices = bluetooth.discover_devices()
#print(nearby_devices)

#for d in nearby_devices:
#    print(bluetooth.lookup_name(d))