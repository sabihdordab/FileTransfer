import socket

if __name__ == '__main__' : 
    
    host = '127.0.0.1' # local host
    port = 8080 # test port
    BUFFER_SIZE = 1024
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

    sock.listen(number_of_clients) # enabling server to accept connections
    connections = [] # storing clients
    print('Initiating clients...') 
    for i in range(number_of_clients): 

        client = sock.accept() 
        connections.append(client) 
        print('Connected with client', i+1) 

        # Receiving File Data 
        print('Receiving file from client',i) 
        data = client[0].recv(BUFFER_SIZE).decode() 
        if not data: 
                    print('no data! from client',i) 
                    client[0].close()  
                    continue
        
        file_path = 'serverfiles/file'+str(i)+'.txt'
        with open(file_path, "w") as f:
            while data: 
                if not data: 
                    break
                else: 
                    f.write(data) 
                    data = client[0].recv(BUFFER_SIZE).decode() 
  
        print('Received successfully! File path is:', file_path)
        client[0].close() 
