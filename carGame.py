import pygame, random
pygame.init()

LENGTH, WIDTH, FPS = 500, 500, 60
window = pygame.display.set_mode((LENGTH, WIDTH))
caption = pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

class car(object):
    def __init__(self,):
        self.player = pygame.Rect(50, LENGTH - 40, 20, 40)
        self.speed = 5
    
    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.player.left > 10:
            self.player.x -= self.speed
        
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.player.right < LENGTH - 10:
            self.player.x += self.speed
    
    def draw(self):
        pygame.draw.rect(window, (0, 255, 0), self.player)

class obstacle(object):
    def __init__(self):
        self.ground = [pygame.Rect(random.randint(0, LENGTH - 40), y, 20, 40) for y in range (0, LENGTH * 2, 100)]
        self.speed = 5
    
    def update_rectangle(self):
        for rect in self.ground:
            rect.y += self.speed
        
        if self.ground and self.ground[0].y > LENGTH:
            self.ground.pop(0)
            self.ground.append(pygame.Rect(random.randint(0, LENGTH - 40), self.ground[-1].y - 100, 20, 40))
    
    def draw(self):
        for rect in self.ground:
            pygame.draw.rect(window, (0, 0, 255), rect)
   
run = True
game_over = False
car_object = car()
obstacles_for_collision = obstacle()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill((0, 0, 0))
    
    if not(game_over):
        keys = pygame.key.get_pressed()
        car_object.move(keys)
        obstacles_for_collision.update_rectangle()
        car_object.draw()
        obstacles_for_collision.draw()
    
    else:
        run = False
    
    #Needed help with this
    for object in obstacles_for_collision.ground:
        if object.colliderect(car_object.player):
            game_over = True
    
    pygame.display.update()

pygame.quit()