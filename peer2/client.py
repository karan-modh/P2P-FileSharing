import socket
import os
import pickle
from settings import SERVERIP,PORT

def list_files(conn):
    request = "LIST"
    conn.send(str.encode(request))
    data = conn.recv(4096)
    print(pickle.loads(data))

def fetch_by_name(conn):
    request = input("Enter filename to fetch : ")
    conn.send(str.encode(request))
    result = conn.recv(2048)
    if str.encode("NOT FOUND") == result:
        print("File not present")
    else:
        ip = pickle.loads(result)
        return ip

def central_server_func(conn):
    filepath = "./files"
    files = os.listdir(filepath)
    data = pickle.dumps(files)
    conn.send(data)
    while True:
        print("Functions available : 1)View list of available files 2)Fetch file by name 3)Quit Connection")
        choice = int(input())
        if choice == 1:
            print(list_files(conn))
        elif choice == 2:
            return fetch_by_name(conn)
        else:
            conn.send(str.encode("bye"))
            break
    
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((SERVERIP,PORT))
    ip = central_server_func(s)
    s.close()
    if ip:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip[0],5678))
        print("Connected to peer with ip : ",ip[0])
        File_Request = input("Enter File Name again : ")
        s.send(str.encode(File_Request))
        File_Request = "./files/" + File_Request
        with open(File_Request,'wb') as f:
            while True:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)
        f.close()
        print("File Transferred Successgully")
        s.close()

if __name__ == "__main__":
    main()