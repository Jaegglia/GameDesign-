import pygame, time, sys

 
pygame.init() 
  
   
win = pygame.display.set_mode((500, 500)) 
  
# set the pygame window name  
pygame.display.set_caption("All there is") 
  
# object current co ordinates  
x = 200
y = 200

x2=200
y2=200

# dimensions of the object  
width = 20
height = 20


#object 2 dimensions
width2=20
height2=20



vel = 10
  
run = True
  
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
     
    for event in pygame.event.get(): 
          
          
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    # stores keys pressed  
    keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x>0: 
          
        # decrement in x co-ordinate 
        x -= vel 
          
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<500-width: 
          
        
        x += vel 
         
        
    if keys[pygame.K_UP] and y>0: 
          
         
        y -= vel 
          
    # if left arrow key is pressed    
    if keys[pygame.K_DOWN] and y<500-height: 
       
        y += vel 



    if keys[pygame.K_a] and x2>0:
        x2 -= vel

    if keys[pygame.K_d] and x2<500-width2:
        x2 += vel

    if keys[pygame.K_w] and y2>0:
        y2 -= vel

    if keys[pygame.K_s] and y2<500-height2:
        y2 += vel


    
              
    # completely fill the surface object   
    # with black colour   
    win.fill((0, 0, 0)) 
      
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 

    pygame.draw.rect(win, (0, 0, 255), (x2, y2, width2, height2))
    # it refreshes the window 
    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() 
