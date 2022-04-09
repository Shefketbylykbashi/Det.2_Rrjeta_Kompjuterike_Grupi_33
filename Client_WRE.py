import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

   

    print("Shkyqja nga serveri.")
    client.close()

if __name__ == "__main__":
    main()
