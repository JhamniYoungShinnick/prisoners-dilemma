####
#Jhamni Young-Shinnick
#9.26.17
#P_D_Wolf.py
#The Wolf strategy for the prisoners dilemma game
####

team_name = 'Jhamni'
strategy_name = 'Wolf'
strategy_description = 'Bite before bitten.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: 
        return 'c'    #It's the first round: Collude!
        
    if(their_history.count('b')% 2  == 0):
        return 'b'          # I've been betrayed more than once
                            #Get revenge for betrayal!
    if((my_history.count('b') - 1) % 3 == 0 and my_history.count('b') != 1):
        return 'c'              #I've regained Alpha Status, Collude.
    else:
        return 'b' #They've continued to betray me. Betray!
    return 'c'      #Collude default
    
 