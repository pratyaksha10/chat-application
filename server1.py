import socket
import select
import sys
from _thread import *
def generateKey(string,keyS):
        key=list(keyS)
        if len(string)==len(key):
                 return(keyS)
        else:
               for  i in range(len(string)-len(key)):
                       key.append(key(key[i%len(key)]))
        return("".join(key))
def encrypt(string,key):
        cipher_text=[]
        for i in range(len(string)):    
                if string[i]== " ":
                    cipher_text.append(" ")
                elif string[i].isalpha()==True:
                       x=(ord(string[i])+ord(key[i]))%26
                       x+=ord('A')
                       cipher_text.append(chr(x))
                else:
                     cipher_text.append(string[i])
        return("".join(cipher_text))
def decrypt(cipher_text,key):
        orig_text=[]
        for i in range(len(cipher_text)):
                    if cipher_text==" ":
                                    orig_text.append(" ")
                    elif cipher_text[i].isalpha()==True:
                                    x=(ord(cipher_text[i])-ord(key[i])+26)%26
                                    x+=ord('A')
                                    orig_text.append(chr(x))
                    else:
                                orig_text.append(cipher_text[i])
        return("".join(orig_text))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
        print ("Correct usage: script, IP address, port number")
        exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients=[]
keyword="VELLORE"
def clientthread(conn, addr):
    key=generateKey("WELCOME TO THIS CHATROOM", keyword)
    conn.send(encrypt("WELCOME TO THIS CHATROOM",key))
    while True:
            try:
                message=conn.recv(2048)
                message=message.upper()
                key=generateKey(message,keyword)
                message = decrypt(message,key)
                if message:
                       print ("<"+ addr[0] + ">" + message)
                       message_to_send= "<"+ addr[0] + ">" + message
                       broadcast(message_to_send, conn)
                else:
                       remove(conn)
            except:
                 continue
def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.upper())
            except:
                clients.close()  
                remove(clients)
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
        
while True:
      conn,addr=server.accept()
      list_of_clients.append(conn)
      print(addr[0]+"connected")
      start_new_thread(clientthread,(conn,addr))
conn.close()
server.close()
