import pygame, sys, btools, brandom, math, random
pygame.init()
screen=pygame.display.set_mode([800, 500])

class Disc:
    
    def __init__(self, location, color, size, moving=[0, 0]):
        self.location=location
        self.color=color
        self.size=size
        self.moving=moving
        
    def move(self):
        self.location[0]+=self.moving[0]
        self.location[1]+=self.moving[1]
        
    def bounceOffCircle(self, location, radius):
        self.magnitude=float(math.sqrt(float(self.moving[0]**2+self.moving[1]**2)))
        if self.moving[0]==0:
            self.moving[0]=0.0000001
        self.angle=float(math.atan((self.moving[1]/self.moving[0])))
        
        self.location=[location[0]+(self.size+radius)*-(location[0]-self.location[0])/btools.distance(self.location, location),
        location[1]+(self.size+radius)*-(location[1]-self.location[1])/btools.distance(self.location, location)]
        
        if self.moving[0]<0:
            self.angle+=math.pi
        b=math.atan(float(location[1]-self.location[1])/float(location[0]-self.location[0]))
        
        self.angle=b-self.angle+b
        self.angle+=math.pi
        
        self.moving[0]=self.magnitude*math.cos(self.angle)
        self.moving[1]=self.magnitude*math.sin(self.angle)
        
    def draw(self):
        pygame.draw.circle(screen, self.color, btools.intAll(self.location), self.size)

ball=Disc([400, 0], [0, 0, 0], 5)

bouncers=[]
for i in range(50):
    bouncers.append(Disc([random.randint(0, 800), random.randint(13, 500)], brandom.color(), 10))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
    ball.moving[1]+=0.5
    ball.move()
    for b in bouncers:
        if btools.distance(ball.location, b.location)<ball.size+b.size:
            ball.bounceOffCircle(b.location, b.size)
            b.size+=1
            
    
    if ball.location[1]>505:
        ball.location[1]=-5
    if ball.location[0]<5:
        ball.location[0]=5
        ball.moving[0]=-ball.moving[0]
    if ball.location[0]>795:
        ball.location[0]=795
        ball.moving[0]=-ball.moving[0]
    
    ball.moving[0]=ball.moving[0]*0.98
    ball.moving[1]=ball.moving[1]*0.98
    screen.fill([255, 255, 255])
    for b in bouncers:
        b.draw()
    ball.draw()
    pygame.display.flip()
    pygame.time.Clock().tick(30)
