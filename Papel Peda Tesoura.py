import random

def play():
    user = input(" 'r' para pedra, 'p' para papel, 't' para tesoura ")
    computador = random.choice(['r','p','t'])

    if user==computador:
        return 'Empate'

    if ganhou(user, computador):
        return 'Você ganhou!'


    return 'Você Perdeu!'

def ganhou(player, oponete):
    if ( player=='r' and oponete=='t') or (player=='t'and oponete=='p') or (player=='p'and oponete=='r'):
        return True

print(play())