import pygame
pygame.init()

#import time  module
import time

#importing random module
import random

# display screen
width = 800
height = 600
screen = pygame.display.set_mode((width , height))


# for title 
pygame.display.set_caption("RACER")

#loading car image
carimg =pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car.jpg")

#loading all the images
grass = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\grass.jpg")
yellow_strip = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\yellow_strip.jpg")
strip = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\strip.jpg")



# car image appearing function 
def car (x,y):
    screen.blit(carimg, (x,y))

# car width
car_width = 56

#crashed message
myfont = pygame.font.SysFont("None", 100)
render_text = myfont.render("CAR CRASHED",1, (0,0,0))

#function for the obstacle 
 
def obstacle(obs_x, obs_y , obs):
    if obs == 0:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car1.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car4.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car5.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car6.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\car7.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load(r"C:\Users\DELL\.vscode\Python VS Programs\.vscode\carpink.jpg")
    screen.blit (obs_pic, (obs_x,obs_y))   

# function to create a new random obstacle
def new_obstacle ():
    obs_x = random.randrange(75, 650)
    obs = random.randrange(0, 6)  # Adjust the range based on the number of obstacles you have
    return obs_x, obs

# function for adding background images
def background():
    screen.blit (grass,(0,0))
    screen.blit (grass,(700,0))
    screen.blit (yellow_strip,(400,0))
    screen.blit (yellow_strip,(400,100))
    screen.blit (yellow_strip,(400,200))
    screen.blit (yellow_strip,(400,300))
    screen.blit (yellow_strip,(400,400))
    screen.blit (yellow_strip,(400,500))
    screen.blit (yellow_strip,(400,600))
    screen.blit (strip,(120,0))
    screen.blit (strip,(680,0))



    
#for background color
#screen.fill((119,119,119))

#time module
clock =pygame.time.Clock()
clock.tick(100)


#the game loop, close button
def game_loop():
   bumped = False
   x_change = 0
   x = 400
   y = 470
   obstacle_speed = 10
   obs = 0
   y_change = 0
   obs_x = random.randrange(200, 650)
   obs_y = -750
   enemy_width = 56
   enemy_hieght = 125

   while not bumped:
       for event in pygame.event.get():
           if event.type == pygame.QUIT :
            
               bumped = True 
               

    

             # moving in x-y coordinates
           if event.type == pygame.KEYDOWN :
              if event.key == pygame.K_LEFT:
                  x_change = -5
              if event.key == pygame.K_RIGHT:
                  x_change = 5
           if event.type == pygame.KEYUP :
               if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                   x_change = 0
           
       x += x_change

       obs_y -= (obstacle_speed/4)
       obstacle(obs_x, obs_y, obs)

        # Check if the obstacle has reached the bottom of the screen
       if obs_y > height:
         obs_x, obs = new_obstacle()
         obs_y = -750

       obs_y += obstacle_speed

       # filling the bgc with each frame
       screen.fill((119,119,119))
       background()
       obs_y -= (obstacle_speed/4)
       obstacle(obs_x, obs_y, obs)
       obs_y += obstacle_speed

       # calling car function   
       car(x,y)
       if x >680 - car_width or x<110:
           screen.blit(render_text,(150,200))
           pygame.display.update()
           time.sleep(5)
           game_loop()
           bumped = True

       if y <obs_y + enemy_hieght:
           #right side
           if x> obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x+car_width < obs_x + enemy_width:
               screen.blit(render_text, (100,200))
               pygame.display.update()
               time.sleep(5)
               game_loop()
           
         
# update screen       
       pygame.display.update()
       clock.tick(100)

       if bumped :
        break

   pygame.quit()
   quit()    
game_loop() 