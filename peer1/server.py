import socket

def client_func(clientSock,ip):
    data = clientSock.recv(2048).decode()
    fp = "./files/" + data
    f = open(fp,'rb')
    l = f.read(1024)
    while l:
        clientSock.send(l)
        l=f.read(1024)
    f.close()

    print("Sent Successfully")
    clientSock.close()    

def main():
    f = open("hostIp.txt")
    ip = f.readline().split(" ")[0]
    port = 5678
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip,port))
    print("Peer Server started on ip : ",ip ," port : ",port)
    server.listen(5)
    while True:
        client,clip = server.accept()
        print("Connected to ",ip)
        client_func(client,clip)

if __name__ == "__main__":
    main()