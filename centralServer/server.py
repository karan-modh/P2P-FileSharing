import socket
import sys
import threading
import pickle

Files_List = {}
Peers_active = []

def searchFile(msg,clip):
    for x,y in Files_List.items():
        if msg in y:
            if x != clip:
                return x
    return "NOT FOUND"

class client_thread(threading.Thread):
    def __init__(self,clSocket,add):
        threading.Thread.__init__(self)
        self.csocket = clSocket
        self.cadd = add
        print("New Connection added : ",add)

    def run(self):
        msg = ''
        recv_data = self.csocket.recv(4096)
        files = pickle.loads(recv_data)
        Files_List[self.cadd] = files
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == "bye":
                break
            elif msg == "LIST":
                list_data = pickle.dumps(Files_List)
                self.csocket.send(list_data)
            else:
                result = searchFile(msg,self.cadd)
                if result == "NOT FOUND":
                    self.csocket.send(str.encode(result))
                else:
                    ip_cl = pickle.dumps(result)
                    self.csocket.send(ip_cl)
                break
        print("Client at ", self.cadd, " disconnected ... ")
        Files_List.pop(self.cadd)
        Peers_active.remove(self.cadd)

def main():
    f = open("../hostIp.txt")
    IPADD = (f.readline()).split(" ")[0]
    PORT = 2312
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((IPADD,PORT))
    print("server listening on ip : ",IPADD , " port : ",PORT)
    while True:
        serverSocket.listen(1)
        (clientSocket,claddress) = serverSocket.accept()
        print("Got connection from ip : ",claddress)
        newthread = client_thread(clientSocket,claddress)
        Peers_active.append(claddress)
        newthread.start()
        
if __name__ == "__main__":
    main()