# Muhammed Yasinhan Yaşar 200201010
# referance: https://docs.python.org/3/howto/sockets.html
# server
import socket
from threading import Thread
import time

from data import question_next

MAX_MSG_LEN = 1024

class Server:
    def __init__(self, HOST, PORT):
        # create an INET, STREAMing socket (TCP connection)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.clients = []
        self.port = PORT
        self.host = HOST
        self.id_counter = 0
        self.minimum_client_count = 2
        self.next_question = False
        self.minimum_client_count = 1
        self.current_question = None


    def listen(self): # main thread
        self.sock.listen(5)
        print(f"Listening port: {self.port}")

        while True:
            client_sock, addr = self.sock.accept()
            print(f"Connection from: {addr}")

            # first ask for client to say his name on the client side
            client_name = client_sock.recv(MAX_MSG_LEN).decode() # we need to decode it because it is raw bytes
            client = {'id': self.id_counter, 'name': client_name, 'socket': client_sock, 'score': 0}
            self.id_counter += 1

            print(f"{client_name} joined to game!")
            # self.brodcast_message(f"{client_name} joined to game! waiting for {self.minimum_client_count - len(self.clients)} other players to join...")

            self.clients.append(client)

            Thread(target=self.handle_new_client, args=(client,)).start()


            if len(self.clients) >= self.minimum_client_count:
                print("GAME_STATE")
                break
        
        # wait for 3 secs and then start to send questions!!!
        time.sleep(3)
        self.next_question = True

        # GAME_STATE_GAME
        while True:
            if (self.next_question):
                try:
                    qd = next(question_next)
                    self.current_question = qd
                    question = qd['content'] + "\n"
                    A = "A) " + qd['choices'][0]['A'] + "\n"
                    B = "B) " + qd['choices'][1]['B'] + "\n"
                    C = "C) " + qd['choices'][2]['C'] + "\n"
                    D = "D) " + qd['choices'][3]['D'] + "\n"
                    self.brodcast_message(question)
                    self.brodcast_message(A)
                    self.brodcast_message(B)
                    self.brodcast_message(C)
                    self.brodcast_message(D)

                    self.next_question = False
                except StopIteration:
                    print("No more questions.")
                    self.brodcast_message("XEND")
                    break
        
        # GAME_STATE_END



    def handle_new_client(self, client):
        client_name: str = client['name']
        client_sock: socket.socket = client['socket']

        client_answer = client_sock.recv(MAX_MSG_LEN).decode()
        if not client_answer:
            # self.brodcast_message(f"{client_name} left the game.")
            self.clients.remove(client)
            client_sock.close()
        elif client_answer == "READY":
            print(f"{client_name}: {client_answer}")

        while True:
            if len(self.clients) >= self.minimum_client_count:
                print(len(self.clients))
                client_sock.send(u"OKOK".encode())
                break
        

        # GAME_STATE_GAME
        client_sock.settimeout(10)  # Set a timeout for recv()
        
        while True:
            try:
                start = time.time()
                client_answer = client_sock.recv(MAX_MSG_LEN).decode()
                end = time.time()
                print("Client answered:", client_answer)
                if self.current_question:
                    if client_answer == self.current_question['answer']:
                        client['score'] += 10
            except socket.timeout:
                end = time.time()
                print("No answer received in time.")
            finally:
                print("elapsed time: ", end - start)
                self.next_question = True


    def brodcast_message(self, message: str):
        for client in self.clients:
            client_sock = client['socket']
            client_sock.send(message.encode())



def main():
    s = Server("localhost", 7777)
    s.listen()



if __name__ == '__main__':
    main()

