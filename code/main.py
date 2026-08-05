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
        


        just_pressed_key = pygame.key.get_just_pressed()
        if just_pressed_key[pygame.K_SPACE] and self.can_shoot:
            Laser(laser ,self.rect.midtop ,(all_sprites ,laser_sprite))
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
        self.lifetime=4000
        self.speed = randint(200,600)
        self.direc=pygame.Vector2(uniform(-0.5,0.5),1).normalize()

        self.word ="meteor"
        self.progress =0




    def  update(self,delta_time):
        self.rect.center += self.direc * self.speed * delta_time
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()    

class Laser(pygame.sprite.Sprite):
    def __init__(self,laser,pos,group):
        super().__init__(group)
        self.image=laser
        self.rect=self.image.get_frect(midbottom = pos)


    def update(self,delta_time):
        self.rect.y -= 500*delta_time
        if self.rect.bottom <0:
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

    


    all_sprites.update(delta_time)
    # player.update()

    window_name.fill('navy blue') 

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
    
    all_sprites.draw(window_name) 
    


    # so basilcy it feels like shimmering stars disaapearig and apearning like blinking someehow
    # window_name.blit(star,(randint(0,1200),randint(0,720))) 
    pygame.display.flip()       
 

     
pygame.quit()