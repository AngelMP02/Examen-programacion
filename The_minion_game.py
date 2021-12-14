def minion_game(string):
    player1=0
    player2=0
    str_len=len(string)  #vemos la longitud de la cadena
    for i in range(str_len): 
        if s[i] in "AEIOU":
            player1+=(str_len)-1
            player2+=(str_len)-1
        
#Comparo los jugadores para ver quien gana
    if player1>player2:
        print("Kevin", player1)
    elif player1<player2:
        print("Stuart", player2)
    elif player1==player2:
        print("Draw")
#
if __name__ == "__main__":
    s=input()
    minion_game(s)

    


