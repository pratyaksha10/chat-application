# chat-application
*Socket programming*:

Sockets can be thought of as endpoints in a communication channel that is bi-directional, 
and establishes communication between a server and one or more clients. Here, we set up a socket on 
each end and allows a client to interact with other clients via the server. The socket on the server 
side are associated itself with the some hardware port on the server side. Any client that has a socket associated 
with the same port can communicate with the server socket.


Multi-Threading

A thread is sub process that runs a set of commands individually of any other thread. So, every time a user 
connects to the server, a separate thread is created for that user and communication from server to client 
takes place along individual threads based on socket objects created for the sake of identity of each client.
We will require two scripts to establish this chat room. One to keep the serving running, and another that every 
client should run in order to connect to the server.
