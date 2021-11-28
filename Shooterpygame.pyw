import pygame
import random
pygame.init()
SCREENWIDTH=800
SCREENHEIGHT = int(SCREENWIDTH*0.8)
shoot=False
icon = pygame.image.load('./img/Icon.png')
pygame.display.set_icon(icon)

wn = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Shooter")

clock=pygame.time.Clock()
fps=60
GRAVITY=0.3

#load sounds
fire = pygame.mixer.Sound("./sounds/fire2.wav")
crate_collect=pygame.mixer.Sound("./sounds/powerup2.wav")
ded = pygame.mixer.Sound("./sounds/ded.wav")
explode = pygame.mixer.Sound("./sounds/explode.wav")


#load images
missile_img=pygame.image.load('img/Missile.png').convert_alpha()
bullet_img=pygame.image.load('img/bullet.png').convert_alpha()
grenade_img=pygame.image.load("img/Grenade.png").convert_alpha()
ground_img=pygame.image.load("img/Ground.png").convert_alpha()
crate_img=pygame.image.load("img/Crate.png").convert_alpha()
block_img=pygame.image.load("./img/Blockade.png")

# ---------------- UI---------------- UI --------------------- UI -------------------- UI
pixelfont = pygame.font.Font("./img/pixkel.ttf", 23)
HpText=pixelfont.render(f"Health: 3", True, "#ffffff", "#000000")
HTrect=HpText.get_rect()
HTrect.center=(100, 20)

losefont = pygame.font.Font("./img/pixkel.ttf", 40)
loseText=losefont.render("You have Lost!", True, "#ffffff", "#000000")
LTrect=loseText.get_rect()
losetextwidth=loseText.get_width()
LTrect.center=(SCREENWIDTH/2, 260)

AmmoText=pixelfont.render(f"Ammo: 20", True, "#ffffff", "#000000")
ATrect=AmmoText.get_rect()
ATrect.center=(91, 46)

GrenadeText=pixelfont.render(f"Grenades: 5", True, "#ffffff", "#000000")
GTrect=GrenadeText.get_rect()
GTrect.center=(119, 72)


wavefont = pygame.font.Font("./img/pixkel.ttf", 32)
WaveText=wavefont.render(f"Wave: 1", True, "#ffffff", "#000000")
WTrect=WaveText.get_rect()
WTrect.center=(SCREENWIDTH/2 + 40, 20)

def draw_bg():
      wn.fill((104, 229, 229))
      if player.isalive== False:
            loseText=losefont.render("You have Lost!", True, "#ffffff", "#68e5e5")
            wn.blit(loseText, LTrect)
            loseText=losefont.render("Press r to restart", True, "#ffffff", "#68e5e5")
            LTTrect=loseText.get_rect()
            LTTrect.center=(SCREENWIDTH/2, 310)
            wn.blit(loseText, LTTrect)
      #pygame.draw.line(wn, (0, 0, 0), (0, 300), (SCREENWIDTH, 300))




class Ground(pygame.sprite.Sprite):
      def __init__(self, x, y, direction):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.transform.scale(ground_img, (int(ground_img.get_width() * 2), int(ground_img.get_height() * 2)))
            self.rect=self.image.get_rect()
            self.rect.center=(x, y)




#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------



blockade_group=pygame.sprite.Group()
enemies_group=pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group=pygame.sprite.Group()
ground_group=pygame.sprite.Group()
crate_group=pygame.sprite.Group()


class Blockade(pygame.sprite.Sprite):
      def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(block_img, (int(block_img.get_width() * 2), int(block_img.get_height() * 2)))
            self.rect=self.image.get_rect()
            self.rect.center=(200, 300)
            self.hp=1
      def updata(self):
            dy=GRAVITY
            for i in ground_group:
                  if self.rect.bottom > i.rect.top:
                        dy=i.rect.top-self.rect.bottom
            self.rect.x -= -dy
      def draw(self):
            wn.blit(self.img, True, False,self.rect)



def gp(x):
      o=48*x-24
      return o


groundL1=Ground(gp(1), 620, 1)
groundH2L1=Ground(gp(1), 595, 2)
groundH2L2=Ground(gp(2), 595, 2)
groundH3L1=Ground(gp(1), 570, 2)
groundH3L2=Ground(gp(2), 570, 2)
groundL2=Ground(gp(2), 620, 1)
groundL3=Ground(gp(3), 620, 1)
groundL4=Ground(gp(4), 620, 1)
groundL5=Ground(gp(5), 620, 1)
groundL6=Ground(gp(6), 620, 1)
groundL7=Ground(gp(7), 620, 1)
groundL8=Ground(gp(8), 620, 1)
groundH2L8=Ground(gp(8), 595, 2)

groundL9=Ground(gp(9), 620, 1)
groundH2L9=Ground(gp(9), 595, 1)
groundL10=Ground(gp(10), 620, 1)
groundL11=Ground(gp(11), 620, 1)
groundL12=Ground(gp(12), 620, 1)
groundL13=Ground(gp(13), 620, 1)
groundL14=Ground(gp(14), 620, 1)
groundL15=Ground(gp(15), 620, 1)
groundL16=Ground(gp(16), 620, 1)
groundL17=Ground(gp(17), 620, 1)
groundH2L15=Ground(gp(16)-16, 595, 2)
groundH2L16=Ground(gp(17)-16, 595, 2)
groundH3L15=Ground(gp(16)-16, 570, 2)
groundH3L16=Ground(gp(17)-16, 570, 2)
ground_group.add(groundL1)
ground_group.add(groundL2)
ground_group.add(groundL3)
ground_group.add(groundL4)
ground_group.add(groundL5)
ground_group.add(groundL6)
ground_group.add(groundL7)
ground_group.add(groundL8)
ground_group.add(groundH2L8)

ground_group.add(groundL9)
ground_group.add(groundH2L9)
ground_group.add(groundL10)
ground_group.add(groundL11)
ground_group.add(groundL12)
ground_group.add(groundL13)
ground_group.add(groundL14)
ground_group.add(groundL15)
ground_group.add(groundL16)
ground_group.add(groundL17)
ground_group.add(groundH2L1)
ground_group.add(groundH2L2)
ground_group.add(groundH3L1)
ground_group.add(groundH3L2)
ground_group.add(groundH2L16)
ground_group.add(groundH2L15)
ground_group.add(groundH3L16)
ground_group.add(groundH3L15)



class Manager():
      def __init__(self):
            self.Wave=1

manager=Manager()

class Bullet(pygame.sprite.Sprite):
      def __init__(self, x, y, direction):
            pygame.sprite.Sprite.__init__(self)
            fire.play(0)
            self.speed=14
            self.image=pygame.transform.scale(bullet_img, (int(bullet_img.get_width() * 0.09), int(bullet_img.get_height() * 0.09)))
            self.rect=self.image.get_rect()
            self.rect.center=(x, y)
            self.direction=direction
      def update(self):
            self.rect.x += (self.direction * self.speed)
            if self.rect.left > SCREENWIDTH + 50 or self.rect.right < -50:
                  self.kill()

            if pygame.sprite.spritecollide(player, bullet_group, False):
                  if player.health >0:
                        player.health-=1
                  self.kill()

            for i in enemies_group:
                  if i != player:
                        if pygame.sprite.spritecollide(i, bullet_group, False):
                              if i.health >0:
                                    i.health-=1
                                    self.kill()





class Grenade(pygame.sprite.Sprite):
      def __init__(self, x, y, direction, me):
            pygame.sprite.Sprite.__init__(self)
            self.GM=1
            self.timer=100
            self.starticks=pygame.time.get_ticks()
            self.velY=-5
            self.changevelY=-20
            self.speed=8
            self.image=grenade_img
            self.rect=self.image.get_rect()
            self.rect.center=(x, y)
            self.direction=direction
      
      def update(self):
            self.velY += (GRAVITY * self.GM)
            dx = (self.direction * self.speed)
            dy=self.velY

            for Ground in ground_group:

                        if Ground.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                              if self.rect.right -2 > Ground.rect.left and self.rect.left + 3 < Ground.rect.right:
                                    dy=Ground.rect.top - self.rect.bottom
                                    self.speed /= 1.55
                                    if self.changevelY < -1 and self.speed>1:
                                          self.changevelY/=2.1
                                          self.GM += 0.2
                                          self.velY -= GRAVITY * 45
                                          if self.velY < -5:
                                                self.velY = -5
                                          dy=self.changevelY
                                    else:
                                          self.velY=0
            
            


            if self.rect.left + dx < 0 or self.rect.right +dx> SCREENWIDTH:
                  self.direction*=-1
                  self.dx = self.speed*self.direction
            
            seconds=(pygame.time.get_ticks()-self.starticks)/1000
            if seconds > 5:
                  self.rect.x=10000
                  explode.play(0)
                  self.rect.y = -100
                  self.kill()
                  grenade_group.remove(self)

            for i in enemies_group:
                  if i != player:
                        #if pygame.sprite.spritecollide(i, grenade_group, False):
                        if (i.rect.left < self.rect.right and i.rect.right > self.rect.left) and (i.rect.bottom > self.rect.top and i.rect.top < self.rect.bottom):
                              if i.health >0:
                                    i.health-=2
                                    explode.play(0)
                                    self.kill()

            #update grende pos
            try:
                  self.rect.x+=dx
                  self.rect.y+=dy
            except:
                  p=1




class Crate(pygame.sprite.Sprite):
      def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.isalive=True
            self.img = crate_img
            self.img= pygame.transform.scale(self.img, (int(self.img.get_width() * 0.6), int(self.img.get_height() * 0.6)))
            self.rect=self.img.get_rect()
            self.x = x
            self.y = y
            self.rect.x=self.x
            self.rect.y=self.y
            self.velY=5
      
      def collision(self):
           # if pygame.sprite.spritecollide(player, self, False):
                #  p=1
            if (player.rect.left < self.rect.right and player.rect.right > self.rect.left) and (player.rect.bottom > self.rect.top and player.rect.top < self.rect.bottom):
                  pop=random.randint(1, 3)
                  if pop != 1:
                        playerammo=int((random.randint(2, 6)) * (manager.Wave / 1.8))
                        if playerammo > 50:
                              playerammo=50
                        playergrenades=int((random.randint(1, 4)) * (manager.Wave / 1.8))
                        if playergrenades > 30:
                              playergrenades=30

                        player.ammo += playerammo
                        player.grenades+=playergrenades
                  else:
                        player.health += int((random.randint(1, 3)) * (manager.Wave / 1.2))
                  self.isalive=False
                  crate_collect.play(0)
                  self.kill()

      def movement(self):
            dy=self.velY
            for Ground in ground_group:
                  if Ground.rect.colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                        dy=0

            self.rect.y+=dy
      
      def draw(self):
            wn.blit(pygame.transform.flip(self.img, True, False),self.rect)



LOC=[]











class soldier(pygame.sprite.Sprite):
      def __init__(self, x, y, scale, speed, ammo, health):
            pygame.sprite.Sprite.__init__(self)
            self.isalive=True
            self.candropcrates=True
            self.shoottime=0
            self.ammo = ammo
            self.start_ammo=ammo
            self.hasjumped=False
            self.health=health
            self.changeindex=0
            self.scale=scale
            self.direction=1
            self.jump=False
            self.velY=0
            self.grenades = 5
            self.flip=False
            self.speed=speed

            self.animationL=[]
            self.index=0
            for i in range(7):
                  img =pygame.image.load(f'img/{i+1}.png').convert_alpha()
                  img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                  self.animationL.append(img)
            self.img=self.animationL[self.index]
            
            self.rect = self.img.get_rect()
            self.rect.center = (x, y)


      def enemy(self):
            #GRAVITY
            if self.hasjumped==False and player.rect.bottom -10 < self.rect.top:
                  self.velY=-5.5
                  self.jump=False
                  self.hasjumped=True

            if self.velY < 6:
                  self.velY+=GRAVITY

            dy=self.velY

            if player.rect.right > self.rect.right:
                  self.direction = 1
                  self.flip=False
            if player.rect.left < self.rect.left:
                  self.direction=-1
                  self.flip=True

            img =pygame.image.load('img/BadGuy.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
            self.img=img
            dy=self.velY
            
            for Ground in ground_group:
                        if Ground.rect.colliderect(self.rect.x, self.rect.y - 3 + dy, self.rect.width, self.rect.height):
                              dy=Ground.rect.top-self.rect.bottom + 3
                              self.hasjumped=False

            if player.rect.bottom > self.rect.top + 15 and player.rect.top < self.rect.bottom - 15:
                  if self.isalive==True:
                        self.shootbulletAI()
            self.rect.y += dy



      def playerUI(self):
            HpText=pixelfont.render(f"Health: {self.health}", True, "#ffffff", "#68e5e5")
            wn.blit(HpText, HTrect)
            AmmoText=pixelfont.render(f"Ammo: {self.ammo}", True, "#ffffff", "#68e5e5")
            wn.blit(AmmoText, ATrect)
            GrenadeText=pixelfont.render(f"Grenades: {self.grenades}", True, "#ffffff", "#68e5e5")
            wn.blit(GrenadeText, GTrect)
            WaveText=wavefont.render(f"Wave {int(manager.Wave)}", True, "#000000", "#68e5e5")
            wn.blit(WaveText, WTrect)


      def update(self):
            if self.shoottime > 0:
                  self.shoottime-=1
            
            
            if self.health <= 0:
                  poiu=random.randint(1, 3)
                  if poiu != 1 and self.candropcrates:
                        
                        ncrate=Crate(random.randint(40,SCREENWIDTH-40), 10)
                        LOC.append(ncrate)
                        crate_group.add(ncrate)
                  self.img=pygame.image.load("img/ded.png")
            
                  manager.Wave += 0.2
                  self.isalive=False
                  ded.play(0)
                  self.kill()
                  self.shoottime = 100000000000000
                


      def move(self, ml, mr):

            dx=0
            dy=0
            
            if self.isalive:
                  if ml:
                        dx-=self.speed
                        self.flip=True
                        self.changeindex+=0.2
                        self.index=int(self.changeindex)
                        self.direction=-1
                  if mr:
                        self.flip=False
                        self.direction=1
                        self.changeindex+=0.2
                        self.index=int(self.changeindex)
                        dx+=self.speed




                  #GRAVITY
                  if self.jump==True and self.hasjumped==False:
                        self.velY=-7.5
                        self.jump=False
                        self.hasjumped=True
                  if self.velY < 6:
                        self.velY+=GRAVITY
                  
                  dy=self.velY
                  if self.jump==True:
                        self.jump=False
                  #COLLSION
                  for Ground in ground_group:
                        if Ground.rect.colliderect(self.rect.x + dx, self.rect.y - 4, self.rect.width, self.rect.height):
                              dx=0


                        if Ground.rect.colliderect(self.rect.x, self.rect.y - 3 + dy, self.rect.width, self.rect.height):
                              dy=Ground.rect.top-self.rect.bottom + 3
                              self.hasjumped=False





                  if self.rect.left + dx <= 0:
                        dx=0
                  if self.rect.right + dx >= SCREENWIDTH:
                        dx=0
                  #decapretated method of ground check
                 # if self.rect.bottom+ dy > 300:
                        #dy=300 - self.rect.bottom
                        #self.hasjumped=False

                  #ANIMATIONS
                  if self.index >6:
                        self.index=0
                        self.changeindex=0
                  
                  if dx == 0 or self.hasjumped==True:
                        self.index=0
                  if self.hasjumped == False:
                        self.img=self.animationL[self.index]
                  else:

                        self.img=pygame.image.load("img/Jump.png")
                        self.img = pygame.transform.scale(self.img, (int(self.img.get_width() * self.scale), int(self.img.get_height() * self.scale)))

                  
                  self.rect.x += dx
                  self.rect.y += dy



      def shootbullet(self):
            if self.shoottime == 0 and self.ammo > 0 and self.isalive:
                  bullet = Bullet(self.rect.centerx + int(0.6 * self.rect.size[0]) * self.direction, self.rect.centery - 4.5, self.direction)
                  bullet_group.add(bullet)
                  self.shoottime=int(30/(manager.Wave/2.1))
                  if self.shoottime < 1.1:
                        self.shoottime=1.1
                  self.ammo-=1


      def shootbulletAI(self):
            if self.shoottime == 0 and self.ammo > 0:
                  bullet = Bullet(self.rect.centerx + int(0.6 * self.rect.size[0]) * self.direction, self.rect.centery - 4.5, self.direction)
                  bullet_group.add(bullet)
                  self.shoottime=int(50/(manager.Wave/3))
                  if self.shoottime < 0.3:
                        self.shoottime=0.3
                  self.ammo-=1
      


      def draw(self):
            wn.blit(pygame.transform.flip(self.img, self.flip, False),self.rect)
            
#-----------------------------------------------------------------------------------------------------------
#before the run
#before the run
#before thr run
#before the run
#before the run
#before thr run
#before the run
#before the run
#before thr run
LOE=[]
StartTime=pygame.time.get_ticks()
Timer=(pygame.time.get_ticks()-StartTime)/1000
SecToPass=0

def spawn(name):
      if player.isalive:
            if manager.Wave < 5:
                  name = soldier(random.randint(50, SCREENWIDTH-50), 200, 1.4, 4, 20, 3)
            else:
                  if manager.Wave < 12:
                        name = soldier(random.randint(50, SCREENWIDTH-50), 200, 1.4, 4, 20, 5)
                  else:
                        name = soldier(random.randint(50, SCREENWIDTH-50), 200, 1.4, 4, 20, int(manager.Wave/1.8))
            enemies_group.add(name)
            LOE.append(name)

player = soldier(30, 500, 1.4, 3, 20, 5)
#enemy = soldier(400, 200, 1.4, 4, 20)
#enemy1 = soldier(500, 200, 1.4, 4, 20)
#enemies_group.add(enemy)
#enemies_group.add(enemy1)

def throwGrenade():
      Ngrenadde=Grenade(player.rect.centerx + (0.6 * player.direction * player.rect.size[0]),\
                        player.rect.top, player.direction, 1)
      grenade_group.add(Ngrenadde)
      grenade_thrown=True
      player.grenades-=1
 #     newGame()

def newGame():
      global SecToPass
      
      for i in LOE:
            i.candropcrates=False
            i.health=-2
      for i in grenade_group:
            i.starticks-=5000
      for i in bullet_group:
            i.rect.left = -20
            i.kill()
      SecToPass=-1
      manager.Wave=1
      global player
      player = soldier(30, 500, 1.4, 4, 30, 5)
      for i in LOC:
            i.isalive=False
      
                  
LOS = []
LOS.append(player)
#LOS.append(enemy)
#LOS.append(enemy1)
LOG=[]
ml=False
mr=False
grenade=False
grenade_thrown=False
grenadeTime=0
run=True
while run:
      Timer=(pygame.time.get_ticks()-StartTime)/1000
      clock.tick(fps)


      
      draw_bg()
      bullet_group.update()
      bullet_group.draw(wn)
      grenade_group.update()
      grenade_group.draw(wn)
      ground_group.draw(wn)
      

      for i in LOE:
            if i.isalive == True and player.isalive:
                  i.draw()
                  i.update()
                  i.enemy()

      if player.isalive:
            player.update()
            player.move(ml, mr)
            player.playerUI()
            player.draw()

      for i in LOC:
            if i.isalive:
                  i.collision()
                  i.movement()
                  i.draw()
      #crate_group.draw(wn)


      if Timer > SecToPass:
            spawn(str(random.randint(10, 3000)))
            Sec = Timer + int(10 * 1.3 / manager.Wave)
            if Sec < Timer + 1:
                  Sec = Timer+1
            SecToPass=Sec

      if shoot:
            player.shootbullet()
      if grenade==True and grenade_thrown==False and player.grenades > 0 and Timer > grenadeTime:
            throwGrenade()
            grenadeTime=Timer+10-manager.Wave
            if grenadeTime < Timer + 0.1:
                  grenadeTime=Timer+0.1

      pygame.display.update()




      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run=False

            

            if event.type == pygame.KEYDOWN:

                  if player.isalive == False:
                        if event.key == pygame.K_r:
                              newGame()

                  if event.key == pygame.K_ESCAPE:
                        run=False
                  if event.key == pygame.K_a:
                        ml=True
                  if event.key == pygame.K_d:
                        mr=True
                  if event.key == pygame.K_w:
                        player.jump=True

                  if event.key == pygame.K_SPACE or event.key == pygame.K_RSHIFT:
                        shoot=True
                  if event.key == pygame.K_LSHIFT or event.key == 13:
                        grenade=True


            if event.type == pygame.KEYUP:
                  if event.key == pygame.K_a:
                        ml=False
                  if event.key == pygame.K_d:
                        mr=False
                  if event.key == pygame.K_SPACE or event.key == pygame.K_RSHIFT:
                        shoot=False
                  if event.key == pygame.K_LSHIFT or event.key == 13:
                        grenade=False
                        grenade_thrown=False
            
pygame.quit()
