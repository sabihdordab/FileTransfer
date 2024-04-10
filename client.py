import socket 

def tcp_socket(host,port):
	host=host
	port=port
	# defining client socket 
    #AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connecting with Server 
	print(f"Connecting to {host}:{port}")
	sock.connect((host, port)) 
	print("Connected!")
	return sock


def send_data(socket):
	while True: 
		print("Sending data to server? Input filename/path , Exit? Enter exit!")
		inp = input()
		if inp.lower() == "exit":
			exit()
		else:
			filename = inp
			try: 
			# Reading file and sending data to server 
				f = open(filename, "r") 
				data = f.read() 
				if not data: 
					print("no data!")
					break
				while data: 
					sock.send(str(data).encode()) 
					data = f.read() 
				f.close() 

			except IOError: 
				print('Invalid filename/path!') 

if __name__ == '__main__': 
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
	sock = tcp_socket(host,port)
	send_data(socket=sock)
	
