from superwires import games
import pygame as pg
import math
width, height = 1280,720

games.init(screen_width=width, screen_height=height, fps = 60)

class Trampline(games.Sprite):
    tramline = games.load_image('trampoline.png')
    def __init__(self,x,y):
        super().__init__(image=pg.transform.scale(Trampline.tramline,(300,150)), x = x, y = y)
        self.x = x
        self.y = y


class Player(games.Sprite):
    tail_ship = []
    spins = []
    variels = []



    ROTATION_STEP = 15
    
    image = games.load_image('bike.png')
    tricks = {'UP':'backflip',
              'DOWN':'frontflip',
              1:"360spin"}

    def check_trick(tricks, bottom):
        for key in tricks:
            if key == bottom:
                return tricks[key]


    def __init__(self, x,y):
        super().__init__(image=pg.transform.scale(Player.image, (80,50)),x=x,y=y)
        self.x = x
        self.y = y
        self.angle = 0
        self.gravity = True
        self.is_jumping = False # Флаг прыжка
        self.center = (x+ self.width//2,y + self.height//2)
        self.count = 0

        self.score = games.Text(value=0, size=25, color=(255,255,255),
                                top=5, right=games.screen.width-100)
        games.screen.add(self.score)



    def update(self):   
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 5

        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx


        if self.overlapping_sprites:
            self.angle -= 0.55
            self.y -=1.55


        if games.keyboard.is_pressed(games.K_SPACE):
            self.jump()


        if not self.overlapping_sprites:
            if self.y > 550:
                self.is_jumping = False
                self.y = 550
                self.angle = 0
                if self.y == 550:
                    self.dx = 0
            self.check_jump()

        if games.keyboard.is_pressed(games.K_UP):
            name = Player.check_trick(Player.tricks, "UP")
            trick = Tricks(name, "UP",10)
            if self.x > 300 and self.y <550 and not self.overlapping_sprites:
                trick.perform_trick(self,trick.name)



        if games.keyboard.is_pressed(games.K_DOWN):
            name = Player.check_trick(Player.tricks, "DOWN")
            trick = Tricks(name,"DOWN",10)
            if self.x > 300 and self.y <550 and not self.overlapping_sprites:
                trick.perform_trick(self,trick.name)

        
        
        if games.keyboard.is_pressed(games.K_1):
            name = Player.check_trick(Player.tricks, 1)
            trick = Tricks(name, 1, 25)
            if self.x > 300 and self.y <550 and not self.overlapping_sprites:
                trick.perform_trick(self,trick.name)

        if games.keyboard.is_pressed(games.K_2):
            pass


        if games.keyboard.is_pressed(games.K_3):
            pass

        
        self.restart()
        

            
    def restart(self):
        if self.y >=550 and self.x >300:
            self.destroy()
            self.count = 0
            self.score.destroy()
            self.score.value = 0
            main()


    def frontflip(self,trick):
        if self.gravity == True:
            self.angle += Player.ROTATION_STEP
        self.count +=1
        self.score.value = trick.point ** (self.count//24)

        
   
    def backflip(self,trick):
        if self.gravity == True:
            self.angle -= Player.ROTATION_STEP
        self.count +=1
        self.score.value = trick.point ** (self.count//24)
 

    def spin(self,trick):
        pass

    def tailship(self,trick):
        pass

    def variel(self,trick):
        pass


    def check_jump(self):
        if not self.overlapping_sprites and self.y < 550:
            self.is_jumping = True
        
        if self.is_jumping == True:
            self.gravity = True
            self.gravitron()
        else:
            self.gravity = False

    def gravitron(self):
        if self.gravity == True:
            self.y += 5
            self.angle +=0.8
                 

    def jump(self):
        self.y -= 7
        self.dx += 0.19


class Tricks(games.Sprite):
    def __init__(self, name,key,point):
        self.name = name
        self.key = key
        self.point = point


    def perform_trick(self,player,name_trick):
        if name_trick == "backflip":
            Player.backflip(player,self)           
        if name_trick == "frontflip":
            Player.frontflip(player,self)
        if name_trick == "360spin":
            Player.spin(player,self)


class Explosion_tailship(games.Animation):
    def __init__(self,trickes,pos_x,pos_y):
        super().__init__(images=trickes,
                         x= pos_x, y= pos_y,
                         repeat_interval = 4, n_repeats= 1,
                         is_collideable= False
                         )



            
def main():
    image_back = games.load_image('backgraund.webp')
    
    
    trampline = Trampline(x = 400, y = 510)
    games.screen.add(trampline)
    
    
    player = Player(x = 100,y = 550)
    games.screen.add(player)
    

    games.screen.background = pg.transform.scale(image_back, (1280,720))
    games.screen.mainloop()

if __name__ == '__main__':
    main()