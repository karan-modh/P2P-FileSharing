# P2P-FileSharing
A Computer Networks Assignment - Implementation of P2P-FileSharing based on TCP.

## General Idea
Implemented `Central-Directory Model` (Napster Model) which involves a central server and the peers connected to it.

Implementation involves running a central server as well as running the client and server programs for each peer.

## Steps to test
Run the Central Server to allow connections.
```
cd centralSever
python3 server.py
```

Now set the IP adresses for peer.
```
cd peer1
./ip.sh
```
Run Both the client and server program for Peers in different Terminals(tabs)
```
python3 client.py
python3 server.py
```

## Mode of Working : A Detailed Explaination
- All peers gets connected to Central Server (in different threads) and sends the names of the files allowed to share.
- Central Server stores the file-names along with the ip-address of the peer.
- Client can request the server to see the list of available files
- Client then requests the server for the specific file.
- Server searches for the filename and returns the ip-address of the peer that contains the file with the same name.
- Client now requests the Peer with the filename and finally, it returns the file in response to the request.

Here Peer's server is used to transfer the file and connection is established between the two peers.