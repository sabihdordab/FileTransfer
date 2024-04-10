import socket 

if __name__ == '__main__': 
	host = socket.gethostbyname(socket.gethostname())
	#host = '127.0.0.1' # local host
	port = 8080 # test port
	FORMAT = "utf-8"
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
	# defining client socket 
    #AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connecting with Server 
	print(f"Connecting to {host}:{port}")
	sock.connect((host, port))
	print("[SERVER]",sock.recv(BUFFER_SIZE).decode(FORMAT)) 
	# Reading file and sending data to server 
	while 1:
		inp = input("filepath or exit?:))))\n")
		if inp.lower() == "exit":
			sock.send("exit".encode(FORMAT))
			break
		filepath = inp
		try: 
			file = open(filepath, "r") 
			data = file.read() 
			sock.send(data.encode(FORMAT))
			file.close() 
		except IOError: 
			print('Invalid filename/path!')
	# Receive confirmation message from the server
	msg = sock.recv(BUFFER_SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
	sock.close()
	
