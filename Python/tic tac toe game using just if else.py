while True:
 print("Welcome to the tic tac toe game\n")
 print("Enter first player name\n")
 X=input()
 print("Enter second player name\n")
 Y=input()

 print("Now you have to toss in order to make the first move\n")

 toss=eval(input("Player 1 choose 0 for heads or 1 for tails\n"))

 if toss==0:
    print("Player 1 has chosen heads and palyer 2 got tails.\n ")
 if toss==1:
    print("Player 1 has chosen tails and player 2  got heads.\n")
#tosss kah code
 import random
 rand_int=random.randint(0,11)
#even for heads and odd for tails
 if rand_int%2==0 and toss==0:
    print( X,"has won the toss\n")
    player1toss=1
    player2toss=0
   
 elif rand_int%2!=0 and toss==1:
    print(X,"has won the toss\n")
    player1toss=1
    player2toss=0
    
 elif rand_int%2==0 and toss==1:
    print(Y,"has won the toss\n")  
    player2toss=1
    player1toss=0

 elif rand_int%2!=0 and toss ==0:
    print(Y,"has won the toss")
    player2toss=1
    player1toss=0

#sign kah codeprint
 print(X,"will use sign \\X and",Y,"will use sign \\O\n")    

#grid printing
 f=1
 g=2
 h=3
 j=4
 k=5
 l=6
 z=7
 x=8
 c=9

 print("_",f,"_|_",g,"_|_",h,"_")
 print("_",j,"_|_",k,"_|_",l,"_")
 print("_",z,"_|_",x,"_|_",c,"_")
 print("     |     |   ")
#proper game start

 player1moves1=int
 player2moves1=int
 player1moves2=int
 player2moves2=int
 player1moves3=int
 player2moves3=int
 player1moves4=int
 player2moves4=int
 player1moves5=int
#MOVE 1
 print("select a number to use that box")

 if  player1toss==1:
     move1=eval(input())
     if move1==1: 
       f='x'
       player1moves1=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==2:
       g="x"
       player1moves1=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==3:
       h="X"
       player1moves1=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==4:
       j="X"
       player1moves1=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==5:
       k="X"
       player1moves1=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move1==6:
       l="X"
       player1moves1=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move1==7:
       z="X"
       player1moves1=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move1==8:
       x="X"
       player1moves1=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==9:
      c="X"
      player1moves1=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     print("now",Y,"will make the move")
     move2=eval(input("select the box"))
     if move2==1 and move1!=move2: 
       f='O'
       player2moves1=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==2 and move1!=move2:
       g="O"
       player2moves1=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==3 and move1!=move2:
       h="O"
       player2moves1=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==4 and  move1!=move2:
       j="O"
       player2moves1=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==5 and move1!=move2:
       k="O"
       player2moves1=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move2==6 and move1!=move2:
       l="O"
       player2moves1=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move2==7 and move1!=move2:
       z="O"
       player2moves1=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move2==8 and  move1!=move2:
       x="O"
       player2moves1=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==9 and  move1!=move2:
      c="O"
      player2moves1=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
  
#2nd move
     print("now",X,"make the second move")
     move3=eval(input())
     if move3==1: 
       f='X'
       player1moves2=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==2 :
       g="X"
       player1moves2=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==3 and move1!=move2:
       h="X"
       player1moves2=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==4 and  move1!=move2:
       j="X"
       player1moves2=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==5 and move1!=move2:
       k="X"
       player1moves2=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move3==6 and move1!=move2:
       l="X"
       player1moves2=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move3==7 and move1!=move2:
       z="X"
       player1moves2=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move3==8 and  move1!=move2:
       x="X"
       player1moves2=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==9 and  move1!=move2:
       c="X"
       player1moves2=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")

     print("Now",Y,"will make the second move")
     move4=eval(input())

     if move4==1:
       f='O'
       player2moves2=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==2 :
       g="O"
       player2moves2=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==3 and move1!=move2:
       h="O"
       player2moves2=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==4 and  move1!=move2:
       j="O"
       player2moves2=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==5 and move1!=move2:
       k="O"
       player2moves2=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move4==6 and move1!=move2:
       l="O"
       player2moves2=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move4==7 and move1!=move2:
       z="O"
       player2moves2=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move4==8 and  move1!=move2:
       x="O"
       player2moves2=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==9 and  move1!=move2:
       c="O"
       player2moves2=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")

#3rdmove
     print("now",X,"make the 3rd move")   
     move5=eval(input())
     if move5==1: 
       f='x'
       player1moves3=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==2:
       g="x"
       player1moves3=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==3:
       h="X"
       player1moves3=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==4:
       j="X"
       player1moves3=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==5:
       k="X"
       player1moves3=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move5==6:
       l="X"
       player1moves3=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move5==7:
       z="X"
       player1moves3=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move5==8:
       x="X"
       player1moves3=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==9:
       c="X"
       player1moves3=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
    # Assuming player1moves1, player1moves2, and player1moves3 are the positions chosen by Player 1 in each row
     if (((player1moves1==1 or player1moves1== 2 or player1moves1== 3)  and (player1moves2==2 or player1moves2== 1 or player1moves2==3) and (player1moves3==3 or player1moves3== 2 or player1moves3== 1)) or ((player1moves1==2 or player1moves1== 5 or player1moves1== 8) and (player1moves2==5 or player1moves2== 2 or player1moves2== 8) and (player1moves3==8 or player1moves3== 5 or player1moves3== 2)) or ((player1moves1==3 or player1moves1== 6 or player1moves1== 9) and (player1moves2==6 or player1moves2== 3 or player1moves2== 9) and (player1moves3==9 or player1moves3== 6 or player1moves3== 3)) or ((player1moves1==1 or player1moves1== 4 or player1moves1== 7) and (player1moves2==4 or player1moves2== 1 or player1moves2== 7) and (player1moves3==7 or player1moves3== 1 or player1moves3== 4)) or ((player1moves1==1 or player1moves1== 5 or player1moves1== 9) and (player1moves2==5 or player1moves2== 1 or player1moves2== 9) and (player1moves3==9 or player1moves3== 1 or player1moves3== 5)) or ((player1moves1==4 or player1moves1== 5 or player1moves1== 6) and (player1moves2==5 or player1moves2== 4 or player1moves2== 6) and (player1moves3==4 or player1moves3== 5 or player1moves3== 6)) or ((player1moves1==7 or player1moves1== 5 or player1moves1== 3) and (player1moves2==7 or player1moves2== 5 or player1moves2== 3) and (player1moves3==7 or player1moves3== 5 or player1moves3== 3)) or ((player1moves1==7 or player1moves1== 8 or player1moves1== 9) and (player1moves2==7 or player1moves2== 8 or player1moves2== 9) and (player1moves3==7 or player1moves3== 8 or player1moves3== 9))) :
       print("***congratulations***\nYou have won the game")
       break
     print("now",Y,"will make the 3rd move")
     move6=eval(input())
     
     if move6==1 and move1!=move2: 
       f='O'
       player2moves3=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==2 and move1!=move2:
       g="O"
       player2moves3=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==3 and move1!=move2:
       h="O"
       player2moves3=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==4 and  move1!=move2:
       j="O"
       player2moves3=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==5 and move1!=move2:
       k="O"
       player2moves3=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move6==6 and move1!=move2:
       l="O"
       player2moves3=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move6==7 and move1!=move2:
       z="O"
       player2moves3=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move6==8 and  move1!=move2:
       x="O"
       player2moves3=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==9 and  move1!=move2:
       c="O"
       player2moves3=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player2moves1==1 or player2moves1== 2 or player2moves1== 3)  and (player2moves2==2 or player2moves2== 1 or player2moves2==3) and (player2moves3==3 or player2moves3== 2 or player2moves3== 1)) or ((player2moves1==2 or player2moves1== 5 or player2moves1== 8) and (player2moves2==5 or player2moves2== 2 or player2moves2== 8) and (player2moves3==8 or player2moves3== 5 or player2moves3== 2)) or ((player2moves1==3 or player2moves1== 6 or player2moves1== 9) and (player2moves2==6 or player2moves2== 3 or player2moves2== 9) and (player2moves3==9 or player2moves3== 6 or player2moves3== 3)) or ((player2moves1==1 or player2moves1== 4 or player2moves1== 7) and (player2moves2==4 or player2moves2== 1 or player2moves2== 7) and (player2moves3==7 or player2moves3== 1 or player2moves3== 4)) or ((player2moves1==1 or player2moves1== 5 or player2moves1== 9) and (player2moves2==5 or player2moves2== 1 or player2moves2== 9) and (player2moves3==9 or player2moves3== 1 or player2moves3== 5)) or ((player2moves1==4 or player2moves1== 5 or player2moves1== 6) and (player2moves2==5 or player2moves2== 4 or player2moves2== 6) and (player2moves3==4 or player2moves3== 5 or player2moves3== 6)) or ((player2moves1==7 or player2moves1== 5 or player2moves1== 3) and (player2moves2==7 or player2moves2== 5 or player2moves2== 3) and (player2moves3==7 or player2moves3== 5 or player2moves3== 3)) or ((player2moves1==7 or player2moves1== 8 or player2moves1== 9) and (player2moves2==7 or player2moves2== 8 or player2moves2== 9) and (player2moves3==7 or player2moves3== 8 or player2moves3== 9))) :
       print("*** CONGRATULATIONS YOU HAVE WON THE GAME ***")
       break
#4thmove
     print("now",X,"wil make the 4th move")
     move7=eval(input())       
     if move7==1: 
       f='x'
       player1moves4=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==2:
       g="x"
       player1moves4=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==3:
       h="X"
       player1moves4=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==4:
       j="X"
       player1moves4=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==5:
       k="X"
       player1moves4=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move7==6:
       l="X"
       player1moves4=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move7==7:
       z="X"
       player1moves4=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move7==8:
       x="X"
       player1moves4=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==9:
      c="X"
      player1moves4=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player1moves1==1 or player1moves1== 2 or player1moves1== 3)  and (player1moves2==2 or player1moves2== 1 or player1moves2==3) and (player1moves3==3 or player1moves3== 2 or player1moves3== 1)) or ((player1moves1==2 or player1moves1== 5 or player1moves1== 8) and (player1moves2==5 or player1moves2== 2 or player1moves2== 8) and (player1moves3==8 or player1moves3== 5 or player1moves3== 2)) or ((player1moves1==3 or player1moves1== 6 or player1moves1== 9) and (player1moves2==6 or player1moves2== 3 or player1moves2== 9) and (player1moves3==9 or player1moves3== 6 or player1moves3== 3)) or ((player1moves1==1 or player1moves1== 4 or player1moves1== 7) and (player1moves2==4 or player1moves2== 1 or player1moves2== 7) and (player1moves3==7 or player1moves3== 1 or player1moves3== 4)) or ((player1moves1==1 or player1moves1== 5 or player1moves1== 9) and (player1moves2==5 or player1moves2== 1 or player1moves2== 9) and (player1moves3==9 or player1moves3== 1 or player1moves3== 5)) or ((player1moves1==4 or player1moves1== 5 or player1moves1== 6) and (player1moves2==5 or player1moves2== 4 or player1moves2== 6) and (player1moves3==4 or player1moves3== 5 or player1moves3== 6)) or ((player1moves1==7 or player1moves1== 5 or player1moves1== 3) and (player1moves2==7 or player1moves2== 5 or player1moves2== 3) and (player1moves3==7 or player1moves3== 5 or player1moves3== 3)) or ((player1moves1==7 or player1moves1== 8 or player1moves1== 9) and (player1moves2==7 or player1moves2== 8 or player1moves2== 9) and (player1moves3==7 or player1moves3== 8 or player1moves3== 9))) :
       print("***congratulations***\nYou have won the game")
       break  

     print("now",Y,"will make the next move")
     move8=eval(input())
     if move8==1 and move1!=move2: 
       f='O'
       player2moves4=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==2 and move1!=move2:
       g="O"
       player2moves4=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==3 and move1!=move2:
       h="O"
       player2moves4=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==4 and  move1!=move2:
       j="O"
       player2moves4=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==5 and move1!=move2:
       k="O"
       player2moves4=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move8==6 and move1!=move2:
       l="O"
       player2moves4=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move8==7 and move1!=move2:
       z="O"
       player2moves4=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move8==8 and  move1!=move2:
       x="O"
       player2moves4=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==9 and  move1!=move2:
      c="O"
      player2moves4=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player2moves1==1 or player2moves1== 2 or player2moves1== 3)  and (player2moves2==2 or player2moves2== 1 or player2moves2==3) and (player2moves3==3 or player2moves3== 2 or player2moves3== 1)) or ((player2moves1==2 or player2moves1== 5 or player2moves1== 8) and (player2moves2==5 or player2moves2== 2 or player2moves2== 8) and (player2moves3==8 or player2moves3== 5 or player2moves3== 2)) or ((player2moves1==3 or player2moves1== 6 or player2moves1== 9) and (player2moves2==6 or player2moves2== 3 or player2moves2== 9) and (player2moves3==9 or player2moves3== 6 or player2moves3== 3)) or ((player2moves1==1 or player2moves1== 4 or player2moves1== 7) and (player2moves2==4 or player2moves2== 1 or player2moves2== 7) and (player2moves3==7 or player2moves3== 1 or player2moves3== 4)) or ((player2moves1==1 or player2moves1== 5 or player2moves1== 9) and (player2moves2==5 or player2moves2== 1 or player2moves2== 9) and (player2moves3==9 or player2moves3== 1 or player2moves3== 5)) or ((player2moves1==4 or player2moves1== 5 or player2moves1== 6) and (player2moves2==5 or player2moves2== 4 or player2moves2== 6) and (player2moves3==4 or player2moves3== 5 or player2moves3== 6)) or ((player2moves1==7 or player2moves1== 5 or player2moves1== 3) and (player2moves2==7 or player2moves2== 5 or player2moves2== 3) and (player2moves3==7 or player2moves3== 5 or player2moves3== 3)) or ((player2moves1==7 or player2moves1== 8 or player2moves1== 9) and (player2moves2==7 or player2moves2== 8 or player2moves2== 9) and (player2moves3==7 or player2moves3== 8 or player2moves3== 9))) :
       print("*** CONGRATULATIONS YOU HAVE WON THE GAME ***")
       break
#final move
     print("now",X,"will make the final move")
     move9=eval(input())

     if move9==1: 
       f='x'
       player1moves5=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==2:
       g="x"
       player1moves5=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==3:
       h="X"
       player1moves5=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==4:
       j="X"
       player1moves5=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==5:
       k="X"
       player1moves5=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move9==6:
       l="X"
       player1moves5=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move9==7:
       z="X"
       player1moves5=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move9==8:
       x="X"
       player1moves5=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==9:
      c="X"
      player1moves5=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
  
     if (((player1moves1==1 or player1moves1== 2 or player1moves1== 3)  and (player1moves2==2 or player1moves2== 1 or player1moves2==3) and (player1moves3==3 or player1moves3== 2 or player1moves3== 1)) or ((player1moves1==2 or player1moves1== 5 or player1moves1== 8) and (player1moves2==5 or player1moves2== 2 or player1moves2== 8) and (player1moves3==8 or player1moves3== 5 or player1moves3== 2)) or ((player1moves1==3 or player1moves1== 6 or player1moves1== 9) and (player1moves2==6 or player1moves2== 3 or player1moves2== 9) and (player1moves3==9 or player1moves3== 6 or player1moves3== 3)) or ((player1moves1==1 or player1moves1== 4 or player1moves1== 7) and (player1moves2==4 or player1moves2== 1 or player1moves2== 7) and (player1moves3==7 or player1moves3== 1 or player1moves3== 4)) or ((player1moves1==1 or player1moves1== 5 or player1moves1== 9) and (player1moves2==5 or player1moves2== 1 or player1moves2== 9) and (player1moves3==9 or player1moves3== 1 or player1moves3== 5)) or ((player1moves1==4 or player1moves1== 5 or player1moves1== 6) and (player1moves2==5 or player1moves2== 4 or player1moves2== 6) and (player1moves3==4 or player1moves3== 5 or player1moves3== 6)) or ((player1moves1==7 or player1moves1== 5 or player1moves1== 3) and (player1moves2==7 or player1moves2== 5 or player1moves2== 3) and (player1moves3==7 or player1moves3== 5 or player1moves3== 3)) or ((player1moves1==7 or player1moves1== 8 or player1moves1== 9) and (player1moves2==7 or player1moves2== 8 or player1moves2== 9) and (player1moves3==7 or player1moves3== 8 or player1moves3== 9))) :
       print("***congratulations***\nYou have won the game")
       break  
     else:
       print("oops. Both players have played well. But the match was a Draw.It was a good game.")
  #player 2 conditions     
 if player2toss==1:
     move1=eval(input()) 
     if move1==1: 
       f='O'
       player2moves1=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==2:
       g="O"
       player2moves1=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==3:
       h="O"
       player2moves1=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==4:
       j="O"
       player2moves1=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==5:
       k="O"
       player2moves1=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move1==6:
       l="O"
       player2moves1=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move1==7:
       z="O"
       player2moves1=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move1==8:
       x="O"
       player2moves1=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move1==9:
      c="O"
      player2moves1=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
      
     print("now",X,"will make the next move")
     move2=eval(input())
     if move2==1 and move1!=move2: 
       f='X'
       player1moves1=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==2 and move1!=move2:
       g="X"
       player1moves1=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==3 and move1!=move2:
       h="X"
       player1moves1=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==4 and  move1!=move2:
       j="X"
       player1moves1=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==5 and move1!=move2:
       k="X"
       player1moves1=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move2==6 and move1!=move2:
       l="X"
       player1moves1=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move2==7 and move1!=move2:
       z="X"
       player1moves1=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move2==8 and  move1!=move2:
       x="X"
       player1moves1=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move2==9 and  move1!=move2:
      c="X"
      player1moves1=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
  
#2nd move
     print("now",Y,"make the second move")
     move3=eval(input())

     if move3==1: 
       f='O'
       player2moves2=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==2 :
       g="O"
       player2moves2=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==3 and move1!=move2:
       h="O"
       player2moves2=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==4 and  move1!=move2:
       j="O"
       player2moves2=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==5 and move1!=move2:
       k="O"
       player2moves2=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move3==6 and move1!=move2:
       l="O"
       player2moves2=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move3==7 and move1!=move2:
       z="O"
       player2moves2=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move3==8 and  move1!=move2:
       x="O"
       player2moves2=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move3==9 and  move1!=move2:
      c="O"
      player2moves2=9
      print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
  
     print("Now",X,"will make the move")
     move4=eval(input())

     if move4==1: 
       f='X'
       player1moves2=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==2 :
       g="X"
       player1moves2=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==3 and move1!=move2:
       h="X"
       player1moves2=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==4 and  move1!=move2:
       j="X"
       player1moves2=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==5 and move1!=move2:
       k="X"
       player1moves2=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move4==6 and move1!=move2:
       l="X"
       player1moves2=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move4==7 and move1!=move2:
       z="X"
       player1moves2=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move4==8 and  move1!=move2:
       x="X"
       player1moves2=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move4==9 and  move1!=move2:
       c="X"
       player1moves2=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")

#3rdmove
     print("now",Y,"make the 3rd move")   
     move5=eval(input())
     if move5==1: 
       f='O'
       player2moves3=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==2:
       g="O"
       player2moves3=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==3:
       h="O"
       player2moves3=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==4:
       j="O"
       player2moves3=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==5:
       k="O"
       player2moves3=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move5==6:
       l="O"
       player2moves3=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move5==7:
       z="O"
       player2moves3=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move5==8:
       x="O"
       player2moves3=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move5==9:
       c="O"
       player2moves3=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player2moves1==1 or player2moves1== 2 or player2moves1== 3)  and (player2moves2==2 or player2moves2== 1 or player2moves2==3) and (player2moves3==3 or player2moves3== 2 or player2moves3== 1)) or ((player2moves1==2 or player2moves1== 5 or player2moves1== 8) and (player2moves2==5 or player2moves2== 2 or player2moves2== 8) and (player2moves3==8 or player2moves3== 5 or player2moves3== 2)) or ((player2moves1==3 or player2moves1== 6 or player2moves1== 9) and (player2moves2==6 or player2moves2== 3 or player2moves2== 9) and (player2moves3==9 or player2moves3== 6 or player2moves3== 3)) or ((player2moves1==1 or player2moves1== 4 or player2moves1== 7) and (player2moves2==4 or player2moves2== 1 or player2moves2== 7) and (player2moves3==7 or player2moves3== 1 or player2moves3== 4)) or ((player2moves1==1 or player2moves1== 5 or player2moves1== 9) and (player2moves2==5 or player2moves2== 1 or player2moves2== 9) and (player2moves3==9 or player2moves3== 1 or player2moves3== 5)) or ((player2moves1==4 or player2moves1== 5 or player2moves1== 6) and (player2moves2==5 or player2moves2== 4 or player2moves2== 6) and (player2moves3==4 or player2moves3== 5 or player2moves3== 6)) or ((player2moves1==7 or player2moves1== 5 or player2moves1== 3) and (player2moves2==7 or player2moves2== 5 or player2moves2== 3) and (player2moves3==7 or player2moves3== 5 or player2moves3== 3)) or ((player2moves1==7 or player2moves1== 8 or player2moves1== 9) and (player2moves2==7 or player2moves2== 8 or player2moves2== 9) and (player2moves3==7 or player2moves3== 8 or player2moves3== 9))) :
       print("*** CONGRATULATIONS YOU HAVE WON THE GAME ***")  
       break
     print("now",X,"will make the move")
     move6=eval(input())
     if move6==1 : 
       f='X'
       player1moves3=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==2 :
       g="X"
       player1moves3=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==3 :
       h="X"
       player1moves3=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==4 :
       j="X"
       player1moves3=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==5 :
       k="X"
       player1moves3=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move6==6 :
       l="X"
       player1moves3=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move6==7 :
       z="X"
       player1moves3=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move6==8 :
       x="X"
       player1moves3=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move6==9 :
       c="X"
       player1moves3=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player1moves1==1 or player1moves1== 2 or player1moves1== 3)  and (player1moves2==2 or player1moves2== 1 or player1moves2==3) and (player1moves3==3 or player1moves3== 2 or player1moves3== 1)) or ((player1moves1==2 or player1moves1== 5 or player1moves1== 8) and (player1moves2==5 or player1moves2== 2 or player1moves2== 8) and (player1moves3==8 or player1moves3== 5 or player1moves3== 2)) or ((player1moves1==3 or player1moves1== 6 or player1moves1== 9) and (player1moves2==6 or player1moves2== 3 or player1moves2== 9) and (player1moves3==9 or player1moves3== 6 or player1moves3== 3)) or ((player1moves1==1 or player1moves1== 4 or player1moves1== 7) and (player1moves2==4 or player1moves2== 1 or player1moves2== 7) and (player1moves3==7 or player1moves3== 1 or player1moves3== 4)) or ((player1moves1==1 or player1moves1== 5 or player1moves1== 9) and (player1moves2==5 or player1moves2== 1 or player1moves2== 9) and (player1moves3==9 or player1moves3== 1 or player1moves3== 5)) or ((player1moves1==4 or player1moves1== 5 or player1moves1== 6) and (player1moves2==5 or player1moves2== 4 or player1moves2== 6) and (player1moves3==4 or player1moves3== 5 or player1moves3== 6)) or ((player1moves1==7 or player1moves1== 5 or player1moves1== 3) and (player1moves2==7 or player1moves2== 5 or player1moves2== 3) and (player1moves3==7 or player1moves3== 5 or player1moves3== 3)) or ((player1moves1==7 or player1moves1== 8 or player1moves1== 9) and (player1moves2==7 or player1moves2== 8 or player1moves2== 9) and (player1moves3==7 or player1moves3== 8 or player1moves3== 9))) :
       print("***congratulations***\nYou have won the game")
       break     
#4thmove
      
     print("now",Y,"wil make the 4th move")
     move7=eval(input())   
     if move7==1: 
       f='O'
       player2moves4=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==2:
       g="O"
       player2moves4=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==3:
       h="O"
       player2moves4=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==4:
       j="O"
       player2moves4=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==5:
       k="O"
       player2moves4=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move7==6:
       l="O"
       player2moves4=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move7==7:
       z="O"
       player2moves4=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move7==8:
       x="O"
       player2moves4=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move7==9:
       c="O"
       player2moves4=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player2moves1==1 or player2moves1== 2 or player2moves1== 3)  and (player2moves2==2 or player2moves2== 1 or player2moves2==3) and (player2moves3==3 or player2moves3== 2 or player2moves3== 1)) or ((player2moves1==2 or player2moves1== 5 or player2moves1== 8) and (player2moves2==5 or player2moves2== 2 or player2moves2== 8) and (player2moves3==8 or player2moves3== 5 or player2moves3== 2)) or ((player2moves1==3 or player2moves1== 6 or player2moves1== 9) and (player2moves2==6 or player2moves2== 3 or player2moves2== 9) and (player2moves3==9 or player2moves3== 6 or player2moves3== 3)) or ((player2moves1==1 or player2moves1== 4 or player2moves1== 7) and (player2moves2==4 or player2moves2== 1 or player2moves2== 7) and (player2moves3==7 or player2moves3== 1 or player2moves3== 4)) or ((player2moves1==1 or player2moves1== 5 or player2moves1== 9) and (player2moves2==5 or player2moves2== 1 or player2moves2== 9) and (player2moves3==9 or player2moves3== 1 or player2moves3== 5)) or ((player2moves1==4 or player2moves1== 5 or player2moves1== 6) and (player2moves2==5 or player2moves2== 4 or player2moves2== 6) and (player2moves3==4 or player2moves3== 5 or player2moves3== 6)) or ((player2moves1==7 or player2moves1== 5 or player2moves1== 3) and (player2moves2==7 or player2moves2== 5 or player2moves2== 3) and (player2moves3==7 or player2moves3== 5 or player2moves3== 3)) or ((player2moves1==7 or player2moves1== 8 or player2moves1== 9) and (player2moves2==7 or player2moves2== 8 or player2moves2== 9) and (player2moves3==7 or player2moves3== 8 or player2moves3== 9))) :
       print("*** CONGRATULATIONS YOU HAVE WON THE GAME ***")  
       break
     print("now",X,"will make the next move")
     move8=eval(input())
     if move8==1 and move1!=move2: 
       f='X'
       player1moves4=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==2 and move1!=move2:
       g="X"
       player1moves4=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==3 and move1!=move2:
       h="X"
       player1moves4=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==4 and  move1!=move2:
       j="X"
       player1moves4=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==5 and move1!=move2:
       k="X"
       player1moves4=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move8==6 and move1!=move2:
       l="X"
       player1moves4=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move8==7 and move1!=move2:
       z="X"
       player1moves4=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move8==8 and  move1!=move2:
       x="X"
       player1moves4=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move8==9 and  move1!=move2:
       c="X"
       player1moves4=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player1moves1==1 or player1moves1== 2 or player1moves1== 3)  and (player1moves2==1 or player1moves2== 2 or player1moves2==3) and (player1moves3==1 or player1moves3== 2 or player1moves3== 3)) or ((player1moves1==2 or player1moves1== 5 or player1moves1== 8) and (player1moves2==2 or player1moves2== 5 or player1moves2== 8) and (player1moves3==2 or player1moves3== 5 or player1moves3== 8)) or ((player1moves1==3 or player1moves1== 6 or player1moves1== 9) and (player1moves2==3 or player1moves2==6 or player1moves2== 9) and (player1moves3==3 or player1moves3== 6 or player1moves3==9)) or ((player1moves1==1 or player1moves1== 4 or player1moves1== 7) and (player1moves2==4 or player1moves2== 1 or player1moves2== 7) and (player1moves3==7 or player1moves3== 1 or player1moves3== 4)) or ((player1moves1==1 or player1moves1== 5 or player1moves1== 9) and (player1moves2==5 or player1moves2== 1 or player1moves2== 9) and (player1moves3==9 or player1moves3== 1 or player1moves3== 5)) or ((player1moves1==4 or player1moves1== 5 or player1moves1== 6) and (player1moves2==5 or player1moves2== 4 or player1moves2== 6) and (player1moves3==4 or player1moves3== 5 or player1moves3== 6)) or ((player1moves1==7 or player1moves1== 5 or player1moves1== 3) and (player1moves2==7 or player1moves2== 5 or player1moves2== 3) and (player1moves3==7 or player1moves3== 5 or player1moves3== 3)) or ((player1moves1==7 or player1moves1== 8 or player1moves1== 9) and (player1moves2==7 or player1moves2== 8 or player1moves2== 9) and (player1moves3==7 or player1moves3== 8 or player1moves3== 9))) :
       print("***congratulations***\nYou have won the game")
       break    
#final move
      
     print("now",Y,"will make the final move")
     move9=eval(input())
     if move9==1: 
       f='O'
       player2moves5=1
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==2:
       g="O"
       player2moves5=2
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==3:
       h="O"
       player2moves5=3
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==4:
       j="O"
       player2moves5=4
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==5:
       k="O"
       player2moves5=5
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")     
     if move9==6:
       l="O"
       player2moves5=6
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")  
     if move9==7:
       z="O"
       player2moves5=7
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ") 
     if move9==8:
       x="O"
       player2moves5=8 
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if move9==9:
       c="O"
       player2moves5=9
       print("_",f,"_|_",g,"_|_",h,"_\n_",j,"_|_",k,"_|_",l,"_\n_",z,"_|_",x,"_|_",c,"_\n     |     |   ")
     if (((player2moves1==1 or player2moves1== 2 or player2moves1== 3)  and (player2moves2==2 or player2moves2== 1 or player2moves2==3) and (player2moves3==3 or player2moves3== 2 or player2moves3== 1)) or ((player2moves1==2 or player2moves1== 5 or player2moves1== 8) and (player2moves2==5 or player2moves2== 2 or player2moves2== 8) and (player2moves3==8 or player2moves3== 5 or player2moves3== 2)) or ((player2moves1==3 or player2moves1== 6 or player2moves1== 9) and (player2moves2==6 or player2moves2== 3 or player2moves2== 9) and (player2moves3==9 or player2moves3== 6 or player2moves3== 3)) or ((player2moves1==1 or player2moves1== 4 or player2moves1== 7) and (player2moves2==4 or player2moves2== 1 or player2moves2== 7) and (player2moves3==7 or player2moves3== 1 or player2moves3== 4)) or ((player2moves1==1 or player2moves1== 5 or player2moves1== 9) and (player2moves2==5 or player2moves2== 1 or player2moves2== 9) and (player2moves3==9 or player2moves3== 1 or player2moves3== 5)) or ((player2moves1==4 or player2moves1== 5 or player2moves1== 6) and (player2moves2==5 or player2moves2== 4 or player2moves2== 6) and (player2moves3==4 or player2moves3== 5 or player2moves3== 6)) or ((player2moves1==7 or player2moves1== 5 or player2moves1== 3) and (player2moves2==7 or player2moves2== 5 or player2moves2== 3) and (player2moves3==7 or player2moves3== 5 or player2moves3== 3)) or ((player2moves1==7 or player2moves1== 8 or player2moves1== 9) and (player2moves2==7 or player2moves2== 8 or player2moves2== 9) and (player2moves3==7 or player2moves3== 8 or player2moves3== 9))) :
       print("*** CONGRATULATIONS YOU HAVE WON THE GAME ***")
     else:
       print("oops. Both players have played well. But the match was a Draw.It was a good game.")     

 





