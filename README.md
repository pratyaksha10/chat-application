# chat-application

# Socket programming:

Sockets can be thought of as endpoints in a communication channel that is bi-directional, 
and establishes communication between a server and one or more clients. Here, we set up a socket on 
each end and allows a client to interact with other clients via the server. The socket on the server 
side are associated itself with the some hardware port on the server side. Any client that has a socket associated 
with the same port can communicate with the server socket.


# Multi-Threading:

A thread is sub process that runs a set of commands individually of any other thread. So, every time a user 
connects to the server, a separate thread is created for that user and communication from server to client 
takes place along individual threads based on socket objects created for the sake of identity of each client.
We will require two scripts to establish this chat room. One to keep the serving running, and another that every 
client should run in order to connect to the server.

# Server Side Script:

The server side script will attempt to establish a socket and bind it to an IP address and port specified by the user.
The script will then stay open and receive connection requests, and will append respective 
socket objects to a list to keep track of active connections. Every time a user connects,a separate thread will be created 
for that user. In each thread, the server awaits a message, and sends that message to other users currently on the chat. If 
the server encounters an error while trying to receive a message from a particular thread, it will exit that thread.
 
 
A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.A server has a listen() method which puts the server into listen mode. This allows the server to listen to incoming connections. And last a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client.

 # Client side work:
 
The client module is the one that utilizer sends requests to the server. Utilizer utilizes the client as the means to connect to the server. Once he establishes the connection, he can communicate to the connected server.The client side script will simply attempt to access the server socket created at the specified IP address and port. Once it connects, it will continuously check as to whether the input comes from the server or from the client, and accordingly redirects output.If the input is from the server, it displays the message on the terminal. If the input is from the user, it sends the message that the users enters to the server for it to be broadcasted to other users.
