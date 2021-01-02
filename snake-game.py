import pygame, random, sys,time
from pygame.locals import *

class Collide1(object):
        def __init__(self):
               pygame.init()
               self.clock = pygame.time.Clock()
               self.font = pygame.font.SysFont('Courier', 30)
               self.main_surface = pygame.display.set_mode((900,680))
               self.score=0                                         
     	       self.applepos = (random.randint(0, 590), random.randint(0, 590))
     	       self.dirs = 0
 	       self.appleimage = pygame.Surface((20, 20))
 	       self.img = pygame.Surface((20, 20))
	       self.appleimage.fill((255, 0, 0))
 	       self.img.fill((0, 255, 0))
	       self.beg_snake_size_x = [290, 290, 290, 290, 290]
     	       self.beg_snake_size_y = [290, 270, 250, 230, 210]
               pygame.display.set_caption('Snake Game')

	def collide(self,x1, x2, y1, y2, w1, w2, h1, h2):
		if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
	           return True
		else:
	           return False

	def die(self,screen, score):
 	        t=self.font.render('Your score was: '+str(score), True, (255, 255, 255))
	        screen.blit(t, (250, 300))
	        pygame.display.update()
	        pygame.time.wait(5000)
	        sys.exit(0)

	def keys(self):
		self.clock.tick(10)
		for e in pygame.event.get():
			if e.type == QUIT:
				sys.exit(0)
			elif e.type == KEYDOWN:
 				if e.key == K_UP and self.dirs != 0:
 		                           self.dirs = 2
				elif e.key == K_DOWN and self.dirs != 2:
 		                           self.dirs = 0
				elif e.key == K_LEFT and self.dirs != 1:
 		                           self.dirs = 3
				elif e.key == K_RIGHT and self.dirs != 3:
 		                           self.dirs = 1

	def update(self,score):
        	t=self.font.render(str(score), True, (255, 255, 255))
        	self.main_surface.blit(t, (10, 10))
        	pygame.display.update()


	def colide(self,beg_snake_size_x,beg_snake_size_y,i):
		if self.collide(beg_snake_size_x[0], beg_snake_size_x[i], beg_snake_size_y[0], beg_snake_size_y[i], 20, 20, 20, 20):
       	            self.die(self.main_surface, self.score)     


	def rotate(self,beg_snake_size_x,beg_snake_size_y):
		if self.dirs==0:
            		beg_snake_size_y[0]=beg_snake_size_y[0]+20
		elif self.dirs==1:
              		beg_snake_size_x[0]=beg_snake_size_x[0]+20
		elif self.dirs==2:
              		beg_snake_size_y[0]=beg_snake_size_y[0]-20
		elif self.dirs==3:
              		beg_snake_size_x[0]=beg_snake_size_x[0]-20

	def begin_snake(self,beg_snake_size_x,beg_snake_size_y):
 		self.main_surface.fill((0,0,0))	
		for i in range(0, len(beg_snake_size_x)):
			self.main_surface.blit(self.img, (beg_snake_size_x[i], beg_snake_size_y[i]))
		self.main_surface.blit(self.appleimage, self.applepos);

class Level3(Collide1):
        def __init__(self,block):
		super(Level3, self).__init__()
		self.block=block
	def level3(self):
	     beg_snake_size_x=self.beg_snake_size_x
     	     beg_snake_size_y=self.beg_snake_size_y
     	     while True:
		self.keys() 
		i = len(beg_snake_size_x)-1
		while i >= 2:
			self.colide(beg_snake_size_x,beg_snake_size_y,i)  
	               	i=i-1  
		
		if self.collide(beg_snake_size_x[0], self.applepos[0], beg_snake_size_y[0], self.applepos[1], 20, 20, 20, 20):
                      self.score+=1;
                      self.block.append((random.randint(0,670),random.randint(0,670)))
                      beg_snake_size_x.append(700);
                      beg_snake_size_y.append(700);
                      self.applepos=(random.randint(0,670),random.randint(0,670))
                      
		if beg_snake_size_x[0]<0:
         	   beg_snake_size_x[0]=649
      		if beg_snake_size_x[0]>650:
          	   beg_snake_size_x[0]=1
        	if beg_snake_size_y[0]<0:
           	   beg_snake_size_y[0]=649
        	if beg_snake_size_y[0]>650:
                   beg_snake_size_y[0]=1
		i = len(beg_snake_size_x)-1
		while i >= 1:
			beg_snake_size_x[i] = beg_snake_size_x[i-1];
                	beg_snake_size_y[i] = beg_snake_size_y[i-1];
                	i=i-1
		self.rotate(beg_snake_size_x,beg_snake_size_y)
		self.begin_snake(beg_snake_size_x,beg_snake_size_y)

  	        for i in range(0,len(self.block)):
    	                  self.main_surface.fill((255,255,0),(self.block[i][0],self.block[i][1],20,20));
               	          if beg_snake_size_x[0] in range(self.block[i][0]-10,self.block[i][0]+20) and beg_snake_size_y[1] in 					range(self.block[i][1]-10,self.block[i][1]+20):
                                   	self.die(self.main_surface,self.score)
        	self.main_surface.fill((255, 255, 0), (679,0,10,680))
        	self.main_surface.fill((255, 255, 0), (0,675,680,10))
		self.update(self.score)
        	if self.score==10:
			self.die(self.main_surface,self.score)
	

class Level2(Collide1):
        def __init__(self):
		super(Level2, self).__init__()
 
	def level2(self):
	     	   beg_snake_size_x=self.beg_snake_size_x
     		   beg_snake_size_y=self.beg_snake_size_y
		   print(beg_snake_size_x,beg_snake_size_y)
		   while True:
			self.keys()
 			i = len(beg_snake_size_x)-1
			while i >= 2:
				self.colide(beg_snake_size_x,beg_snake_size_y,i)
        	        	if (beg_snake_size_x[0]<15 and beg_snake_size_y[0] not in range(300,400)) or (beg_snake_size_x[0]>640 and 						beg_snake_size_y[0] not in range(300,400)):   
                      		    	self.die(self.main_surface,self.score)
                		if (beg_snake_size_y[0]<15 and beg_snake_size_x[0] not in range(300,390)) or (beg_snake_size_y[0]>640 and 						beg_snake_size_x[0] not in range(300,390)):
                       	    		self.die(self.main_surface, self.score)
                		if (beg_snake_size_x[0]<0):
                            		beg_snake_size_x[0]=659
                		if (beg_snake_size_x[0]>660):
                            		beg_snake_size_x[0]=1
                		if (beg_snake_size_y[0]<0):
                            		beg_snake_size_y[0]=659
                		if (beg_snake_size_y[0]>660):
                        		beg_snake_size_y[0]=1                 
				i-= 1
			if self.collide(beg_snake_size_x[0], self.applepos[0], self.beg_snake_size_y[0], self.applepos[1], 20, 20, 20, 20):
                        	 self.score+=1
                        	 beg_snake_size_x.append(700)
                        	 beg_snake_size_y.append(700)
                        	 self.applepos=(random.randint(30,640),random.randint(30,64)) 
                        	 if self.applepos[0]<20:
                        	    self.applepos[0]=self.applepos[0]+20
                 		 if self.applepos[1]<20:
                        	     self.applepos[1]=self.applepos[1]+20
                        	 if self.applepos[0]>670:
                        	     self.applepos[0]=self.applepos[0]-20
                        	 if self.applepos[1]>670:
                        	     self.applepos[1]=self.applepos[1]-20                             
 			i = len(beg_snake_size_x)-1
			while i >= 1:
				beg_snake_size_x[i] = beg_snake_size_x[i-1]
                		beg_snake_size_y[i] = beg_snake_size_y[i-1]
                 		i=i-1
        		if self.score==10:
				g=Level3([])
				g.level3()
				self.score=0	   	  
			self.rotate(beg_snake_size_x,beg_snake_size_y)  
			self.begin_snake(beg_snake_size_x,beg_snake_size_y)	
          		self.main_surface.fill((255, 200, 0),(0,0,20,300))
        		self.main_surface.fill((255, 200, 0),(0,400,20,680))           
        		self.main_surface.fill((255, 200, 0),(0,0,300,20))             
        		self.main_surface.fill((255, 200, 0),(400,0,260,20))        
        		self.main_surface.fill((255, 200, 0),(660,0,20,300))           
        		self.main_surface.fill((255, 200, 0),(660,400,20,680))         
	       		self.main_surface.fill((255, 200, 0),(0,660,300,20))
        		self.main_surface.fill((255, 200, 0),(400,660,260,20))
			self.update(self.score)


class Level1(Collide1):
        def __init__(self):
		super(Level1, self).__init__()

	def level1(self):					
     	   beg_snake_size_x=self.beg_snake_size_x
     	   beg_snake_size_y=self.beg_snake_size_y
     	   while True:
 		self.keys()
		i = len(beg_snake_size_x)-1
		while i >= 2:
			self.colide(beg_snake_size_x,beg_snake_size_y,i)
 			i-= 1
		if self.collide(beg_snake_size_x[0], self.applepos[0], beg_snake_size_y[0], self.applepos[1], 20, 20, 20, 20):
        	              self.score+=1;
        	              beg_snake_size_x.append(900);
        	              beg_snake_size_y.append(900);
         	              self.applepos=(random.randint(0,670),random.randint(0,670))

 		if beg_snake_size_x[0]<0:
 	          beg_snake_size_x[0]=649
                if beg_snake_size_x[0]>650:
 	          beg_snake_size_x[0]=1
        	if beg_snake_size_y[0]<0:
           	  beg_snake_size_y[0]=649
        	if beg_snake_size_y[0]>650:
           	  beg_snake_size_y[0]=1

        	if self.score==10:
			g=Level2()
			g.level2()
			self.score=0	   	  
 		i = len(beg_snake_size_x)-1

		while i >= 1:
		       beg_snake_size_x[i] = beg_snake_size_x[i-1];
 	               beg_snake_size_y[i] = beg_snake_size_y[i-1];
  	               i=i-1

		self.rotate(beg_snake_size_x,beg_snake_size_y)
		self.begin_snake(beg_snake_size_x,beg_snake_size_y)
         	self.main_surface.fill((255, 255, 0), (679,0,10,680))
        	self.main_surface.fill((255, 255, 0), (0,675,680,10))
		self.update(self.score)


x=Level1()
x.level1()
