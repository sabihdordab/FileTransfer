import socket

if __name__ == '__main__' : 
    
    host = '127.0.0.1' # local host
    port = 8080 # test port
    '''
    8000 vs 8080:
    Port 8000 is commonly used for local development servers 
    and applications running locally on a machine during development. 
    For example, when you are developing a web application on your local machine, 
    you might run the development server on port 8000.
    Port 8080, on the other hand, 
    is a common port used for web servers like Apache Tomcat or network administration tools. 
    It is a popular choice for deploying network services.
    '''

    number_of_clients = int(input('Enter number of clients: ')) 

    # defining socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.

    sock.bind((host, port)) 
    sock.listen(number_of_clients)
    connections = [] # storing clients
    print('Initiating clients...') 
    for i in range(number_of_clients): 
        c = sock.accept() 
        connections.append(c) 
        print('Connected with client', i+1) 


    file_i = 0
    client_i = 0
    for c in connections: 
        # Receiving File Data 
        client_i += 1
        data = c[0].recv(1024).decode() 
        filename = 'file'+str(file_i)+'.txt'
        file_i = file_i+1
        f = open(filename, "w") 
        while data: 
            if not data: 
                break
            else: 
                f.write(data) 
                data = c[0].recv(1024).decode() 
  
        print('Receiving file from client', client_i) 
        print('Received successfully! New filename is:', filename)
        f.close() 
 
    for c in connections: 
        c[0].close() 
