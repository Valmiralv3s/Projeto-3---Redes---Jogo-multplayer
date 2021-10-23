import socket
from _thread import *
#from player import Player
import pickle
from game import Game

server = ""
port = 5555

s = socket, socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen()
print("Esperando conexão com o servidor!")

connected = set()
games = []
idCount = 0


#players = [Player(0,0,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]


def threading_client(conn, p, gameid):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    reply = game

                    conn.sendall(pickle.dumps(reply))
            else:
                break

        except:
            break
    print("Conexão perdida")
    print("Fechando Jogo", gameId)
    try:
        del games[gameId]
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    connected, addr = s.accept()
    print("Conectado em")

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Criando um novo jogo...")
    else:
        games[gameId], ready = True
        p = 1

start_new_threading(threading_client(conn, p, gameId))


# def threading_client(conn, player):

#   conn.send(pickle.dumps(players[player]))

# reply = ""
# while True:
#     try:
#         data = pickle.loads(conn.recv(2048)
#          players[player) = data

#         if not data:
#              print("Desconectado")
#             break
#        else:
#             if player == 1:
#                  reply = players[0]
#            else:
#                 reply =  players[1]
#
#               print("Recebido:", data)
#              print("Enviando", reply)

#         conn.sendall(pickle.dumps(reply)))
#    except:
#       break

#currentPlayer = 0
# while True:
#   conn, addr = s.accept()
#  print("Conectado com:", addr)

# start_new_threading(threading_client(conn, currentPlayer))
# currentPlayer += 1
