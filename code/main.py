import pygame
from os.path import join
from random import randint, uniform

pygame.init()
width=1280
high = 720
window_name = pygame.display.set_mode((width,high))  
pygame.display.set_caption("SACE SHOOTER")
run= True



# plain surfCE , it was just a simple block created you define it dimensions and then add it same as we have done with image 
# plane = pygame.Surface((100,120))
# plane.fill("blue")


#y=10
class player(pygame.sprite.Sprite):
    def __init__(self , groups):
        super().__init__(groups)
        self.image =pygame.image.load(join("Space shooter","space 1 setup","images","player.png")).convert_alpha()
        self.rect =self.image.get_frect(center = (width/2,high/2))
        self.dir =pygame.math.Vector2()
        self.speed =300

        self.target= None 
        self.target_radius = 450


        #cooldown
        self.can_shoot = True
        self.laser_shoot_time=0
        self.cooldown_duration = 200

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            print(current_time) 
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot =True   

    def find_target(self):
        self.target = None 

        closest_distance = self.target_radius 

        for meteor in meteor_sprite:
            distance =pygame.Vector2(self.rect.center).distance_to(meteor.rect.center)

            if distance < closest_distance:
                closest_distance = distance
                self.target = meteor


    def update(self,delta_time):
        # print("Ship is being updated")
        key = pygame.key.get_pressed()
        self.dir.y = int(key[pygame.K_DOWN]) - int(key[pygame.K_UP])
        self.dir.x = int(key[pygame.K_RIGHT]) - int(key[pygame.K_LEFT])
    # dir=dir.normalize()  if dir else dir
        if self.dir:
            self.dir=self.dir.normalize()
        else:
            self.dir =self.dir    
        self.rect.center += self.dir*self.speed *delta_time

        self.find_target()
        


        just_pressed_key = pygame.key.get_just_pressed()
        if just_pressed_key[pygame.K_SPACE] and self.can_shoot:
            Laser(laser ,player.rect.midtop ,(all_sprites ,laser_sprite))
            self.can_shoot =False
            self.laser_shoot_time =pygame.time.get_ticks()

        self.laser_timer()    

class Star(pygame.sprite.Sprite):
    def __init__(self,group,star):
        super().__init__(group)

        self.image=star
        self.rect=self.image.get_frect(center = (randint(0,width),randint(0,high)))
        #center here basically we are taking image cenrter
        
        # for i in range(20):
        #     self.rect.append((randint(0,width), randint(0,high)))

class Meteor(pygame.sprite.Sprite):
    def __init__(self,meteor,pos,group):
        super().__init__(group) 

        self.image=meteor
        self.rect= meteor.get_frect(center = pos) 

        self.start_time =pygame.time.get_ticks()
        self.lifetime=9000
        self.speed = randint(50,100)
        self.direc=pygame.Vector2(uniform(-0.5,0.5),1).normalize()

        self.word ="meteor"
        self.progress =0



    def receive_letter(self,letter):
        if self.progress < len(self.word):

            if letter == self.word[self.progress]:
                self.progress +=1  
                if self.progress == len(self.word):
                    return True 

        return False    
    def draw_word(self,window_name):
        text =""
        for i in range(len(self.word)):
            if i < self.progress:
                text += self.word[i]
            else:
                text +="_"

        word_font=pygame.font.Font(join("Space shooter","space 1 setup","images","Oxanium-Bold.ttf"),20)        

        progress_text=word_font.render(text,True,(240,255,200))

        box_rect = pygame.Rect(self.rect.centerx - 50, self.rect.top - 45, 100, 50)


        pygame.draw.rect(window_name,"black",box_rect,border_radius = 5)

        pygame.draw.rect(window_name,"blue",box_rect,2,border_radius = 5)

        # word_text=font.render(self.word,True,(255,255,200))

        # word_rect = word_text.get_frect(
        #     center=(box_rect.centerx,box_rect.top + 15)
        #     )
        progress_rect = progress_text.get_frect(
            center=(box_rect.centerx,box_rect.bottom - 15)
        )

        
                               





        # word_text = font.render(text,True , (240,255,200))
        # word_rect = word_text.get_frect(midbottom = (self.rect.centerx,self.rect.top-10))

        # window_name.blit(word_text, word_rect)
        # lets not show the progress word only the word that is being typed
        

        window_name.blit(progress_text , progress_rect)


    def  update(self,delta_time):
        self.rect.center += self.direc * self.speed * delta_time
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()    

class Laser(pygame.sprite.Sprite):
    def __init__(self,laser,pos,target_pos,group):
        super().__init__(group)
        self.image=laser
        self.rect=self.image.get_frect(midbottom = pos)

        self.direction = pygame.Vector2(target_pos) - pygame.Vector2(pos)

        if self.direction:
            self.direction = self.direction.normalize()

        self.speed = 600        

    def update(self,delta_time):
        self.rect.y -= 500*delta_time
        if(self.rect.bottom <0 or self.rect.top > high or self.rect.right < 0 or self.rect.left > width):
            self.kill()   

def score():
    current_time = pygame.time.get_ticks()//100
    text=font.render(str(current_time),True , (240,255,200))
    text_rect = text.get_frect(midbottom =(width/2 , high-100))
    #text_rect =pygame.Rect(width/2,high -100,100,80)
    # text_rect.center =(width/2,high -100)   
    pygame.draw.rect(window_name , "#f8ac1e",text_rect.inflate(30,30).move(0,-6),5,10,15,15,15) 
    window_name.blit(text,text_rect)
   


star_image = pygame.image.load(join("Space shooter","space 1 setup","images","star.png")).convert_alpha()
meteor = pygame.image.load(join("Space shooter","space 1 setup","images","meteor.png")).convert_alpha()
laser = pygame.image.load(join("Space shooter","space 1 setup","images","laser.png")).convert_alpha()

font =pygame.font.Font(join("Space shooter","space 1 setup","images","Oxanium-Bold.ttf"),30)
# text = font.render('LOVE',True,'red')


all_sprites = pygame.sprite.Group()


for i in range(20):
     Star(all_sprites ,star_image)

meteor_sprite =pygame.sprite.Group()
laser_sprite = pygame.sprite.Group()
player=player(all_sprites)     



clock =pygame.time.Clock()


#custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event , 1200)

while run==True:
    delta_time =clock.tick()/1000
    # print(delta_time)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False 
        if i.type == meteor_event:
           x,y = randint(100,width-100),randint(-200,-100)
           Meteor(meteor,(x,y),(all_sprites ,meteor_sprite))

        if i.type == pygame.KEYDOWN:
            if player.target:
                if player.target.receive_letter(i.unicode):
                    Laser(laser, player.rect.midtop ,player.target.rect.center, (all_sprites , laser_sprite))
                    player.target.kill()
                    player.target = None
            

    



    all_sprites.update(delta_time)

    window_name.fill('navy blue') 
    all_sprites.draw(window_name) 
 

    if player.target:
        pygame.draw.circle(window_name ,"blue" , player.target.rect.center, 35,3)
        player.target.draw_word(window_name)



    # player.update()


    pygame.sprite.groupcollide(laser_sprite,meteor_sprite,True,True)


    # for i in laser_sprite:

    #     if pygame.sprite.spritecollide(i,meteor_sprite,True):
    #         i.kill()
    
    player.radius =20
    meteor_sprite.radius =20

    for i in meteor_sprite:
        if pygame.sprite.collide_circle(player ,i):
            run =False
    score()
    # pygame.draw.rect(window_name ,'red',player , 10, 10)

    # pygame.draw.rect(window_name , "#f8ac1e",text.rect,5,10)       





    # for i in range(40):
    #     window_name.blit(star,i) 
    
    # all_sprites.draw(window_name) 
    


    # so basilcy it feels like shimmering stars disaapearig and apearning like blinking someehow
    # window_name.blit(star,(randint(0,1200),randint(0,720))) 
    pygame.display.flip()       
 

     
pygame.quit()