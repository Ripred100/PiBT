import socket, subprocess
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

MAC = "DC:A6:32:6E:28:5B"
port = 4

print(f"Binding socket to MAC adress: {MAC} and port {port}")


java = subprocess.Popen('java PlayAudioTest', stdin = PIPE, stdout = PIPE, stderr = STDOUT, shell = True, text = True)


### heyyyyyyyyyy this is what has changed right hereeeeee ##
server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_sock.bind((MAC,port))
server_sock.listen(1)

try:
    #accepts the client
    client, adress = server_sock.accept()
    print(f"connection accepted from {adress}")
    
    #loop for printing data recieved 
    while 1:
        data = client.recv(1024)
        if data:
            print(data.decode("utf-8")
                  client.send(data)
 except:
    print("closing socket")
    client.close()
    server_sock.close()


    
    java.communicate("2") #play command, only thing that currently works lol
    

