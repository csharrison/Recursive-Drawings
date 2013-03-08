

"""From Wikipedia: In mathematics, the term chaos game, as coined by Michael Barnsley,[1] originally referred to a method of creating a fractal, using a polygon and an initial point selected at random inside it.[2] The fractal is created by iteratively creating a sequence of points, starting with the initial random point, in which each point in the sequence is a given fraction of the distance between the previous point and one of the vertices of the polygon; the vertex is chosen at random in each iteration. Repeating this iterative process a large number of times, selecting the vertex at random on each iteration, and throwing out the first few points in the sequence, will often (but not always) produce a fractal shape. Using a regular triangle and the factor 1/2 will result in the Sierpinski triangle.

Controls:
Q and A control the x-component factor for all vertices
W and S control the y-component factor for all vertices

R and F control the x factor for a highlighted vertex
T and G control the y factor for a highlighted vertex"""

#basic template
import pygame,sys,os
from pygame.locals import *
from time import *
import random

class Vertex(object):
    def __init__(self,x,y,fractionx,fractiony, font):
        self.ren = font.render(str(fractionx),1,(200,200,200))
        self.fractionx = fractionx
        self.fractiony = fractiony
        self.r = pygame.Rect(x,y,20,20)
    def draw(self, screen, font):
        pygame.draw.rect(screen,(200,0,0),self.r,1)
        self.ren = font.render(str(self.fractionx)+' '+str(self.fractiony),1,(200,200,200))
        screen.blit(self.ren,(self.r[0],self.r[1]))
        
def main(dim):
    pygame.init()
    pygame.display.set_caption('The Chaos Game')
    screen = pygame.display.set_mode((dim[0], dim[1]))
    screen.fill((0,0,0))
    black=pygame.Surface(dim)
    black.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont("Courier New",12)
    
    a = Vertex(100,100,.5,.5,font)

    Vs = [a]
    movingv = None
    
    point = (random.randint(1,dim[0]),random.randint(1,dim[1]))
    pause = False
    clock = pygame.time.Clock()
    while True:
        clock.tick(90)
            
        for e in pygame.event.get(): #processes key/mouse inputs
            mx = float(pygame.mouse.get_pos()[0]); my = float(pygame.mouse.get_pos()[1])
            if e.type == QUIT: pygame.quit(); sys.exit()
            elif e.type == KEYDOWN:
                pygame.draw.rect(screen,(0,0,0),(0,0,dim[0],dim[1]))
                if e.key == K_ESCAPE: pygame.quit();  sys.exit()
                elif e.key == K_SPACE:
                    v = Vertex(mx-10,my-10,Vs[0].fractionx,Vs[0].fractiony,font)
                    Vs.append(v)
                elif e.key == K_f:
                    for v in Vs:
                        if v.r.collidepoint(mx,my)==True:
                            v.fractionx -= .1
                elif e.key == K_r:
                    for v in Vs:
                        if v.r.collidepoint(mx,my)==True:
                            v.fractionx += .1
                elif e.key == K_g:
                    for v in Vs:
                        if v.r.collidepoint(mx,my)==True:
                            v.fractiony -= .1
                elif e.key == K_t:
                    for v in Vs:
                        if v.r.collidepoint(mx,my)==True:
                            v.fractiony += .1
                elif e.key == K_q:
                    for v in Vs:
                        v.fractionx += .1
                elif e.key == K_a:
                    for v in Vs:
                        v.fractionx -= .1
                elif e.key == K_w:
                    for v in Vs:
                        v.fractiony += .1
                elif e.key == K_s:
                    for v in Vs:
                        v.fractiony -= .1
                elif e.key == K_d:
                    for vert in Vs:
                        if vert.r.collidepoint(mx,my)==True:
                            pygame.draw.rect(screen,(0,0,0),vert.r)
                            Vs.remove(vert)
                elif e.key == K_p:
                    pause = not pause

            elif e.type == MOUSEBUTTONDOWN:
                for vert in Vs:
                    if vert.r.collidepoint(mx,my)==True:
                        movingv = vert
                        break
            elif e.type == MOUSEBUTTONUP:
                if movingv != None: movingv = None

        if pause == False:
            for i in xrange(100):

                
                v = Vs[random.randint(0,len(Vs)-1)]
                x = v.r[0]+10
                y = v.r[1]+10
                point = (point[0]+(x-point[0])*v.fractionx, point[1]+(y-point[1])*v.fractiony)
                pygame.draw.circle(screen, (0,200,0),(int(point[0]),int(point[1])),0)


            if movingv != None:
                movingv.r[0] = mx-10
                movingv.r[1] = my-10
                pygame.draw.rect(screen,(0,0,0),(0,0,dim[0],dim[1]))
        for vert in Vs:
            vert.draw(screen, font)

        pygame.display.update()
        
if __name__ == "__main__":
    main((1000,700))

