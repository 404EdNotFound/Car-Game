#Imported the pygame and random module
import pygame, random
pygame.init() #Initialised the module

#Defined the constant length, width and FPS as well as the initial X position
LENGTH, HEIGHT, FPS = 400, 600, 60
INITIAL_X_POS = LENGTH - 40

#Creates the windows with captions and clock
window = pygame.display.set_mode((LENGTH, HEIGHT))
caption = pygame.display.set_caption("Car Game with Images")
clock = pygame.time.Clock()

#Class that is used for the player to run across and prevent themselves from hitting the car
class Player():
    def __init__(self, x):
        self.x = x
        self.speed = 10
        self.hitbox = pygame.Rect(self.x, HEIGHT - carImage.get_height(), carImage.get_width(), carImage.get_height())
    
    #Moves the players
    def move(self, keys):
        if(keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > 40:
            self.x -= self.speed
        
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x <= INITIAL_X_POS - carImage.get_width():
            self.x += self.speed
            
        self.hitbox.update(self.x, HEIGHT - carImage.get_height(), carImage.get_width(), carImage.get_height()) #Used so that the hitbox values can be updated

#Class used for obstacles that can collide with the user
class Cars():
    CARS = ["C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\Red.png", "C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\Black.png", "C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\White.png", "C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\Yellow.png"]
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-HEIGHT, 0)
        self.speed = 5
        self.enemyCarImage = None
        self.hitbox = pygame.Rect((self.x, self.y, 50, 50))
    
    #Randomises the selection
    def carSelection(self):
        self.car = random.choice(self.CARS)
        self.enemyCarImage = pygame.image.load(self.car).convert_alpha()
        self.enemyCarImage = pygame.transform.scale(self.enemyCarImage, (75, 75))
        
    def update_car(self):
        self.y += self.speed
        
        if self.enemyCarImage:
            self.hitbox.update(self.x, self.y, self.enemyCarImage.get_width(), self.enemyCarImage.get_height()) #Used so that the hitbox values can be updated
        
    def draw(self):
        window.blit(self.enemyCarImage, (self.x, self.y))

#Function that is used for displaying contents on the screen
def draw():
    window.fill((0, 0, 0))
    window.blit(roadImage, (0, nooby_y_pos))
    window.blit(roadImage, (0, yPosition))
    window.blit(carImage, (playerCar.x, HEIGHT - carImage.get_width()))
    obstacleCars.draw()
    pygame.display.update()

#Function that is used to ensure that such images move
def image_move():
    global nooby_y_pos, yPosition
    nooby_y_pos += 1.5
    yPosition += 1.5
    
    obstacleCars.update_car()
    
    #Needed assistance with how to ensure that the road moves
    if nooby_y_pos >= roadImage.get_height():
        nooby_y_pos = yPosition - roadImage.get_height()
    
    if yPosition >= roadImage.get_height():
        yPosition = nooby_y_pos - roadImage.get_height()

#Used to define images
carImage = pygame.image.load("C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\Red.png").convert_alpha()
carImage = pygame.transform.rotate(pygame.transform.scale(carImage, (75, 75)), 180) #Rotates to fit the image in the bottom
roadImage = pygame.image.load("C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Car Running Game\\Road.png").convert_alpha()
roadImage = pygame.transform.scale(roadImage, (LENGTH, HEIGHT + 100))

nooby_y_pos = 0
yPosition = roadImage.get_height()

playerCar = Player(LENGTH // 2)
obstacleCars = Cars((random.randint(40, INITIAL_X_POS - carImage.get_width())))

run = True
obstacleCars.carSelection()

#Runs such events within the pygame event listener (event driven paradigm)
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    image_move()
    keys = pygame.key.get_pressed()
    draw()
    playerCar.move(keys)
    
    if obstacleCars.y >= HEIGHT:
        obstacleCars.carSelection()
        obstacleCars.y = -carImage.get_height()
        obstacleCars.x = random.randint(40, INITIAL_X_POS - carImage.get_width())
        
    if playerCar.hitbox.colliderect(obstacleCars.hitbox):
        run = False

pygame.quit()