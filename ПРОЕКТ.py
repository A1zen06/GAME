import pygame

pygame.init()

screen_width, screen_height = 720, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('run crab! run!')

#тексты

f1 = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 50)
text1 = f1.render('вы проиграли соси хуй соси хуй хуй соси длинный в спермочке беленькой пенка спермная глотай!', 1,(255, 0, 0))
text2 = f2.render("вы выиграли соси хуй соси хуй!!!",1,(0,0,0))

#переменные

under_y=240
jump_count=30
get_keys=0
count_coin=0
game_run=True
move_right=False
slow=2
slow2=1
move_left=False
make_jump=False
speed=3
number_iter=0
FPS=20
clock=pygame.time.Clock()

# картинки

player_left=[]
player_right=[]
keys=[]
for x in range(6):
    left_img_player= img = pygame.transform.smoothscale(pygame.image.load("Left_run_" + str(x) + '.png').convert_alpha(),(100,70))
    player_left.append(left_img_player)

for x in range(6):
    right_img_player= img = pygame.transform.smoothscale(pygame.image.load("Right_run_" + str(x) + '.png').convert_alpha(),(100,70))
    player_right.append(right_img_player)

stay_img=pygame.transform.smoothscale(pygame.image.load("stay.png").convert_alpha(),(100,70))
bg=pygame.transform.smoothscale(pygame.image.load("bg.jpg").convert_alpha(),(720,480))
player_rect = stay_img.get_rect(topleft=(screen_width // 2, screen_height - 210))
box=pygame.transform.smoothscale(pygame.image.load("box.png").convert_alpha(),(50,50))
floor_img=pygame.transform.smoothscale(pygame.image.load("floor.jpg").convert_alpha(),(150,50))
floor_rect=floor_img.get_rect(topleft=(270,180))
floor_rect2=floor_img.get_rect(topleft=(30,100))
floor_rect3=floor_img.get_rect(topleft=(570,150))
box_rect=box.get_rect(topleft=(120,280))
box_rect2=box.get_rect(topleft=(500,250))
for i in range(0,5):
    key_img=pygame.transform.smoothscale(pygame.image.load("Key_" + str(i) + ".png").convert_alpha(),(50,50))
    keys.append(key_img)
key_rect = key_img.get_rect(topleft=(120,50))
shipi_img=pygame.transform.smoothscale(pygame.image.load("shipi.png").convert_alpha(),(40,30))
shipi_rect=shipi_img.get_rect(topleft=(30,70))
health_img=pygame.transform.smoothscale(pygame.image.load("health.png").convert_alpha(),(150,80))
coin_img=pygame.transform.smoothscale(pygame.image.load("coin.png").convert_alpha(),(30,30))
coin_rect=coin_img.get_rect(topleft=(510,220))
heart_img=pygame.transform.smoothscale(pygame.image.load("heart.png").convert_alpha(),(30,30))
heart_rect1=heart_img.get_rect(topleft=(660,30))
heart_rect2=heart_img.get_rect(topleft=(630,30))
heart_rect3=heart_img.get_rect(topleft=(600,30))
door_img=pygame.transform.smoothscale(pygame.image.load("Door_4.png").convert_alpha(),(60,80))
door_rect = door_img.get_rect(topleft=(620,70))
#музыка
sound1=pygame.mixer.Sound("les.mp3")
sound1.play(-1)
sound2=pygame.mixer.Sound("sound_coin.mp3")

#ФУНКЦИИ

def jump():
    global jump_count,make_jump
    if jump_count>=-30:
        player_rect.y-=jump_count/2.5
        jump_count-=2
    else:
        jump_count=30
        make_jump=False

# логика игры

while game_run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                move_left=True
            elif event.key==pygame.K_d:
                move_right=True
            elif event.key==pygame.K_SPACE:
                make_jump=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                move_left=False
            elif event.key==pygame.K_d:
                move_right=False
            elif event.key==pygame.K_SPACE:
                jumping=False
    if make_jump:
        jump()
    
    player_rect.x+=speed*(move_right-move_left)
    number_iter+=1
    if number_iter>5:
        number_iter=0
    number_frame = number_iter // slow % 6
    number_frame2 = number_iter // slow % 6
    number_frame3=number_iter // slow2 % 5
    number_frame4=number_iter // slow % 5
    screen.blit(bg,(0,0))
    if move_left:
            screen.blit(player_left[number_frame], player_rect)

            
    elif move_right:
            screen.blit(player_right[number_frame2], player_rect)
    else:
        screen.blit(stay_img, player_rect)   
    if make_jump==False and player_rect.y<=260:
        player_rect.y+=10
    if player_rect.x+75>=screen_width:
        move_right=False
        player_rect.x-=5
    elif player_rect.x+30<=0:
        move_left=False
        player_rect.x+=5
    if box_rect.x==player_rect.x:
        jump_size=0
    if player_rect.colliderect(box_rect):
        if player_rect.y+20<=box_rect.y:
            player_rect.bottom=box_rect.top+5
    if player_rect.colliderect(floor_rect):
        if player_rect.y+20<=floor_rect.y:
            player_rect.bottom=floor_rect.top+5    
    if player_rect.colliderect(floor_rect2):
        if player_rect.y+20<=floor_rect2.y:
            player_rect.bottom=floor_rect2.top+5
    if player_rect.colliderect(shipi_rect):
        if player_rect.y+20<=shipi_rect.y:
            screen.blit(text1,(screen_width,screen_height))
    if player_rect.colliderect(key_rect):
        if player_rect.y<=key_rect.y:
            sound2.play()
            get_keys+=1
            key_rect.x+=1000
    if player_rect.colliderect(floor_rect3):
        if player_rect.y+20<=floor_rect3.y:
            player_rect.bottom=floor_rect3.top+5    
    if len(keys)>0:    
        screen.blit(keys[number_frame3],key_rect)
    if player_rect.colliderect(box_rect2):
        if player_rect.y+20<=box_rect2.y:
            player_rect.bottom=box_rect2.top+5    
    
    if player_rect.colliderect(coin_rect):
        if player_rect.y<=coin_rect.y:
            count_coin+=1    
            sound2.play()
            coin_rect.x=1000
            
    screen.blit(box,(box_rect))
    screen.blit(floor_img,floor_rect)
    screen.blit(coin_img,coin_rect)
    screen.blit(shipi_img,shipi_rect)
    screen.blit(floor_img,floor_rect2)

    screen.blit(health_img,(570,5))
    screen.blit(heart_img,heart_rect1)
    screen.blit(heart_img,heart_rect2)
    screen.blit(heart_img,heart_rect3)
    screen.blit(floor_img,floor_rect3)
    screen.blit(box,box_rect2)
    screen.blit(door_img,door_rect)
    if player_rect.colliderect(shipi_rect):
        if player_rect.y+20<=shipi_rect.y: 
            sound1.stop()
            speed=0
            screen.fill((0,0,0))
            screen.blit(text1,(screen_width//2-70,screen_height//2)) 
    if player_rect.colliderect(door_rect) and get_keys>=1:   
                    sound2.stop()
                    speed=0
                    screen.fill((255,255,255))
                    screen.blit(text2,(150,240))
                    pygame.display.flip()
                    screen.blit(text2,(150,240))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

