print("Guess a number between 1 to 10. Your luck is matter .")
print("Welcome to the elimintion game .")
print("Players : Ali, Affaf, Mustafa, Mazz, Dawood .")
print("Players would select anu number between 1 to 10")

def eliminite(players):
    player_name=["Ali", "Affaf", "Mustafa", "Mazz", "Dawood" ]
    player_number=list(range(1,10))
    player_remain=player_name.copy()
    
    while len(player_remain)>1:
        print("\nCurrent players :", player_remain)
        picks={}
        
        for player in player_remain:
            pick=int(input(f"{player} , pick any number between 1 to 10 :"))
            while pick not in player_number:
                print("Invalifd pick. Try Again .")
                pick=int(input(f"{player} , pick any number between 1 to 10 :"))
            picks[player]=pick
         
        print("picks :",picks)
        eliminited=[]
        
        for player,pick in picks.items():
            if pick==player_name.index(player) + 1:
                print(f"{player} picked {pick} and is eliminited ")
                eliminited.append(player)
                
        if not eliminited:
            print("No one is eliminited this round .")
        else:
            for player in eliminited:
                player_remain.remove(player) 
                
    print("\nGame Over: \n")
    print(f"The Winner is : l{player_remain[0]}") 
    
if __name__=="__main__":      
    eliminite(["Ali", "Affaf", "Mustafa", "Mazz", "Dawood"])
                    
                        
        
            