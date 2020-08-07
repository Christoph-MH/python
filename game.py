import pygame, random
pygame.init()
BREITE=800
HOEHE=600
win=pygame.display.set_mode((BREITE,HOEHE))

feld_size=50
player_size=6

outline=5

color_bg_invis=(0,30,0)
color_bg_vis=(20,200,20)
color_home=(160,100,70)
color_home_outline=(120,60,30)
color_stone=(100,100,100)
color_stone_outline=(60,60,60)

cam_x=BREITE//2
cam_y=HOEHE//2

visible=[]

figuren=[]
anzahl_start_figuren=5
loop=False
for nr in range(anzahl_start_figuren):
    x=0
    y=0
    while (x>=0-(outline) and x<(1*feld_size)+outline and y>=0-(outline) and y<(1*feld_size)+outline) or loop:
        loop=False
        x=random.randint(-1*feld_size,2*feld_size)
        y=random.randint(-1*feld_size,2*feld_size)
        for figur in figuren:
            if x+player_size>figur[0]-player_size and x-player_size<figur[0]+player_size:
                if y+player_size>figur[1]-player_size and y-player_size<figur[1]+player_size:
                    loop=True
        if loop:
            continue
    figuren.append([x,y,False])

home=[0,0]
things=[]
things.append(home)

stone_w=40


print(figuren)
def draw():
    win.fill(color_bg_invis)  # füllen nicht endeckt
    for feld in visible:      # füllen endeckt
        if feld[2]==stone_w:
            pygame.draw.rect(win,color_stone_outline,(feld[0]*feld_size+cam_x,feld[1]*feld_size+cam_y,feld_size,feld_size))
            pygame.draw.rect(win,color_stone,(feld[0]*feld_size+cam_x+outline,feld[1]*feld_size+cam_y+outline,feld_size-2*outline,feld_size-2*outline))
        else:
            pygame.draw.rect(win,color_bg_vis,(feld[0]*feld_size+cam_x,feld[1]*feld_size+cam_y,feld_size,feld_size))
    
    # alles was überm hintergrund ist
    
    pygame.draw.rect(win,color_home_outline,(home[0]*feld_size+cam_x,home[1]*feld_size+cam_y,feld_size,feld_size))
    pygame.draw.rect(win,color_home,(home[0]*feld_size+cam_x+outline,home[1]*feld_size+cam_y+outline,feld_size-2*outline,feld_size-2*outline))
    
    for figur in figuren:
        if figur[2]:
            pass
        else:
            pygame.draw.circle(win,(100,100,100),(figur[0]+cam_x,figur[1]+cam_y),player_size)
            pygame.draw.circle(win,(200,200,200),(figur[0]+cam_x,figur[1]+cam_y),player_size-2)
    



mouse_pos=pygame.mouse.get_pos()
while True:
    mouse_pos_old=mouse_pos
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys=pygame.key.get_pressed()
    mouse_pos=pygame.mouse.get_pos()
    mouse_click=pygame.mouse.get_pressed()
    
    
    visible_copy=visible[:]
    visible=[]
    for thing in things:
        for rel_y in range(-3,4,1):
            for rel_x in range(-3,4,1):
                visible.append([thing[0]+rel_x,thing[1]+rel_y,0])
    for listpos in range(len(visible)):
        for copylistpos in range(len(visible_copy)):
            if visible[listpos][0]==visible_copy[copylistpos][0] and visible[listpos][1]==visible_copy[copylistpos][1]:
                visible[listpos][2]=visible_copy[copylistpos][2]
    for listpos in range(len(visible)):
        if visible[listpos][2]==0:
            visible[listpos][2]=random.randint(1,stone_w)
    
    
    
    if mouse_click[1]:
        cam_x-=mouse_pos_old[0]-mouse_pos[0]
        cam_y-=mouse_pos_old[1]-mouse_pos[1]
    if mouse_click[0]:
        pass
    
    
    draw()
    pygame.display.update()