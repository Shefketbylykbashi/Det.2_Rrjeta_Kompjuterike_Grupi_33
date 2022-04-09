import os
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Mire se erdhet ne server!.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "LIST":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "Folderi server_data eshte i zbraset"
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd == "UPLOAD":
            name, text = data[1], data[2]
            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)

            send_data = "OK@File eshte bere upload me sukses!."
            conn.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"
            filename = data[1]

            if len(files) == 0:
                send_data += "Folderi server_data eshte i zbraset"
            else:
                if filename in files:
                    os.remove(f'{SERVER_DATA_PATH}/{filename}')
                    send_data += "File eshte fshire me sukses."
                else:
                    send_data += "File nuk u gjet."

            conn.send(send_data.encode(FORMAT))

        elif cmd == "LOGOUT":
            break
        elif cmd == "CL_R":
            data = "OK@"
            data += "Ju nuk e keni kete privilegj!\n"
            conn.send(data.encode(FORMAT))
            
        elif cmd == "HELP":
            data = "OK@"
            data += "LIST: Listoje file qe jane ne server.\n"
            data += "UPLOAD: Beje Upload nje file.\n"
            data += "DELETE: Fshije nje file nga serveri.\n"
            data += "LOGOUT: Shkyqu nga serveri.\n"
            data += "HELP: Listo  te gjitha komandat."

            conn.send(data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

