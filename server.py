import socket
import random
if __name__ == '__main__' : 
    
    #host = '127.0.0.1' # local host
    host = socket.gethostbyname(socket.gethostname())
    port = 8080 # test port
    BUFFER_SIZE = 1024
    FORMAT = "utf-8"
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
    # defining socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
    TIMEOUT = 60
    sock.settimeout(TIMEOUT)  # Set a timeout for accepting connections
    sock.bind((host, port)) 
    sock.listen() # enabling server to accept connections
    #connections = [] # storing clients
    print('Initiating clients...') 
    while 1 : 
        try:
            client,address = sock.accept()
            client.send("Connected^^.".encode(FORMAT))
            #connections.append(client)
            print('Connected by', address) 
            
        except socket.timeout:
            print(f'{TIMEOUT} seconds,No connection.')
            continue

        # Receiving File Data 
        print('Receiving file from client',address) 
        data = client.recv(BUFFER_SIZE).decode(FORMAT) 
        if data != "exit": 
            file_path = 'serverfiles/file'+str(random.randint(1,1000))+'.txt'
            with open(file_path, "w") as f:
                while data!= "exit":
                    f.write(data)
                    f.write('\n')
                    data = client.recv(BUFFER_SIZE).decode(FORMAT) 

            print('Received successfully! File path is:', file_path)
            client.send("Done.".encode(FORMAT))

        client.send("Bye.".encode(FORMAT))    
        print(f"{address} disconnected.")
        client.close() 
