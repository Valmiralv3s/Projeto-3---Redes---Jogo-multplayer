from _typeshed import Self
import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket, socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port)
        self.P = self.connect()

    def getP(self):
        return self.P

    def connect():
        try:
            Self.client.connect(Self.addr)
            return pickle.loads(self.client.recv(2048)).decode()
        except:
            pass

    def send(self):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


# n = Network() print(n.send("Olá"))print(n.send("Trabalhando"))
