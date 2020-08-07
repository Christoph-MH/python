import pygame,random
pygame.init() 
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Show Text') 
font = pygame.font.Font('freesansbold.ttf', 32) 
text1 = font.render('Test texT', True, green) 
text2 = font.render('Text', True, blue) 
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()

var1=0
var2=200
text1Rect.center = (X // 2, Y // 2) 
while True:
    pygame.time.delay(5)
    display_surface.fill(white)
    display_surface.blit(text1, text1Rect)
    display_surface.blit(text2, text2Rect) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    var1+=1
    var2+=1
    if var2==300:
        var2=200
    text1Rect.center=(X//2,var2)
    text2Rect.center=(var2,Y//2)
    text1 = font.render(str(var1), True, green)
    pygame.display.update()