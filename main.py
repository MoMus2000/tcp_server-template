import socket
import threading

class TcpServer:
  def __init__(self, PORT=8080, IP="localhost"):
    self.port = PORT
    self.ip = IP

  def handle_request(self, connection, client_address):
    print(f"Connected to {client_address[0]}:{client_address[1]}")
    while True:
      data = connection.recv(1024)
      if not data:
        break
      print(f"{data.decode()}")
      response = b"Hello from the TCP server\n"
      connection.sendall(response)
  
  def listen_and_serve(self):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((self.ip, self.port))
    server_socket.listen()
    print(f"Server bound and listening @ : {self.ip}:{self.port}")
    while True:
      connection, client_address = server_socket.accept()
      # self.handle_request(connection, client_address)
      thread = threading.Thread(target=self.handle_request, args=(connection, client_address,))
      thread.start()

def main():
  server = TcpServer()
  server.listen_and_serve()

if __name__ == "__main__":
  main()
