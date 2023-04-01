from pygame import*

main_win= display.set_mode((700,500))
main_win.fill((200,200,200))

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,image_name,speed,w,h):
        super().__init__()
        self.image= transform.scale(image.load(image_name),(w,h))
        self.rect =self.image.get_rect()
        self.rect.x= x
        self.rect.y = y
    def reset(self):
        main_win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys [K_UP]:
            self.rect.y -= self.speed
        if keys [K_DOWN]:
            self.rect.y += self.speed

player1= Player('desk.png',20,200,50,200,5)
player2= Player('desk.png',20,200,50,200,5)
ball = GameSprite('pixelball.png',200,200,50,200,5)


