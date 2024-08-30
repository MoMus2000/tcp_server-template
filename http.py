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
          
          body = (
              b"<!DOCTYPE html>\r\n"
              b"<html lang=\"en\">\r\n"
              b"<head>\r\n"
              b"    <meta charset=\"UTF-8\">\r\n"
              b"    <title>Sample Page</title>\r\n"
              b"</head>\r\n"
              b"<body>\r\n"
              b"    <h1>Hello, World!</h1>\r\n"
              b"    <p>This is a sample response from the server.</p>\r\n"
              b"</body>\r\n"
              b"</html>\r\n"
          )

          content_length = f"Content-Length: {len(body)}\r\n".encode()
          
          response = (
              b"HTTP/1.1 200 OK\r\n"
              b"Content-Type: text/html; charset=UTF-8\r\n"
              + content_length+
              b"\r\n" +
              body
          )
          
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
