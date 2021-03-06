import pygame, random, time
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

color_text=(200,200,200)
color_text_bg=(50,50,50)

color_circle_outline=(100,100,100)
color_circle=(175,175,175)
color_circle_outline_mouse=(70,70,255)
color_circle_mouse=(135,135,255)

color_tree1=(160,100,70)
color_tree2=(20,100,20)

cam_x=BREITE//2
cam_y=HOEHE//2

res_stone=5
res_wood=5

text_size=24
font = pygame.font.Font('freesansbold.ttf', text_size) 
text_stone = font.render(str(res_stone), True, color_text,color_text_bg) 
text_wood = font.render(str(res_wood), True, color_text,color_text_bg) 
text_stone_rect = text_stone.get_rect()
text_wood_rect = text_wood.get_rect()
text_wood_rect.center=(BREITE-300,20)
text_stone_rect.center=(BREITE-100,20)


wood_img=pygame.image.load("wood.png")
stone_img=pygame.image.load("stone.png")

es_gibt_einen_stein=False
es_gibt_einen_baum=False

visible=[]

figuren=[]

home=[0,0]
things=[]
things.append(home)
stone_w=40
wood_w=[38,39]
anzahl_start_figuren=5





loop=False
def create_start():
    for nr in range(anzahl_start_figuren):
        x=0
        y=0
        loop=True
        while loop:
            loop=False
            x=random.randint(-1*feld_size,2*feld_size)
            y=random.randint(-1*feld_size,2*feld_size)
            for figur in figuren:
                if x+player_size>figur[0]-player_size and x-player_size<figur[0]+player_size:
                    if y+player_size>figur[1]-player_size and y-player_size<figur[1]+player_size:
                        loop=True
            for stone in stones:
                if x+player_size>stone[0] and x-player_size<stone[0]+feld_size:
                    if y+player_size>stone[1] and y-player_size<stone[1]+feld_size:
                        loop=True
            for tree in trees:
                if x+player_size>tree[0] and x-player_size<tree[0]+feld_size:
                    if y+player_size>tree[1] and y-player_size<tree[1]+feld_size:
                        loop=True
            if x+player_size>home[0] and x-player_size<home[0]+feld_size:
                if y+player_size>home[1] and y-player_size<home[1]+feld_size:
                    loop=True
            
            
            
            if loop:
                continue
            figuren.append([x,y,0,10,["",0]])
def draw_tree(x,y):
    stamm_breite=10
    pygame.draw.rect(win,color_tree2,(x*feld_size+cam_x,y*feld_size+cam_y,feld_size,feld_size))
    pygame.draw.rect(win,color_bg_vis,(x*feld_size+cam_x+outline,y*feld_size+cam_y+outline,feld_size-2*outline,feld_size-2*outline))
    pygame.draw.rect(win,color_tree1,(x*feld_size+(feld_size-stamm_breite)//2+cam_x,y*feld_size+30+cam_y,stamm_breite,feld_size//4))
    pygame.draw.polygon(win,color_tree2,((x*feld_size+cam_x+feld_size//4,y*feld_size+cam_y+30),(x*feld_size+cam_x+feld_size-feld_size//4,y*feld_size+cam_y+30),(x*feld_size+cam_x+feld_size//2,y*feld_size+cam_y+outline+5)))
def draw():
    win.fill(color_bg_invis)  # füllen nicht endeckt
    for feld in visible:      # füllen endeckt
        if feld[2]==stone_w:
            pygame.draw.rect(win,color_stone_outline,(feld[0]*feld_size+cam_x,feld[1]*feld_size+cam_y,feld_size,feld_size))
            pygame.draw.rect(win,color_stone,(feld[0]*feld_size+cam_x+outline,feld[1]*feld_size+cam_y+outline,feld_size-2*outline,feld_size-2*outline))
        elif feld[2]==wood_w[0] or feld[2]==wood_w[1]:
            draw_tree(feld[0],feld[1])
        else:
            pygame.draw.rect(win,color_bg_vis,(feld[0]*feld_size+cam_x,feld[1]*feld_size+cam_y,feld_size,feld_size))
    
    # alles was überm hintergrund ist
    
    pygame.draw.rect(win,color_home_outline,(home[0]*feld_size+cam_x,home[1]*feld_size+cam_y,feld_size,feld_size))
    pygame.draw.rect(win,color_home,(home[0]*feld_size+cam_x+outline,home[1]*feld_size+cam_y+outline,feld_size-2*outline,feld_size-2*outline))
    
    for figur in figuren:
        if figur[2]==1:
            pygame.draw.circle(win,color_circle_outline_mouse,(figur[0]+cam_x,figur[1]+cam_y),player_size)
            pygame.draw.circle(win,color_circle,(figur[0]+cam_x,figur[1]+cam_y),player_size-2)
        if figur[2]==2:
            pygame.draw.circle(win,color_circle_outline_mouse,(figur[0]+cam_x,figur[1]+cam_y),player_size)
            pygame.draw.circle(win,color_circle_mouse,(figur[0]+cam_x,figur[1]+cam_y),player_size-2)
        if figur[2]==0:
            pygame.draw.circle(win,color_circle_outline,(figur[0]+cam_x,figur[1]+cam_y),player_size)
            pygame.draw.circle(win,color_circle,(figur[0]+cam_x,figur[1]+cam_y),player_size-2)
    win.blit(text_stone,text_stone_rect)
    win.blit(text_wood,text_wood_rect)
    win.blit(wood_img,(BREITE-400,10))
    win.blit(stone_img,(BREITE-150,5))
        
    
    
stones=[]
trees=[]
done=False
mouse_pos=pygame.mouse.get_pos()
start_time=time.perf_counter()
while True:
    start_time2=time.perf_counter()
    mouse_pos_old=mouse_pos
    pygame.time.delay(round(20+0.5-((time.perf_counter()-start_time)*1000)))
    start_time=time.perf_counter()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys=pygame.key.get_pressed()
    mouse_pos=pygame.mouse.get_pos()
    mouse_click=pygame.mouse.get_pressed()
    rel_mouse_pos=(mouse_pos[0]-cam_x,mouse_pos[1]-cam_y)
    
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
            if visible[listpos][2]==stone_w:
                es_gibt_einen_stein=True
    if not(es_gibt_einen_stein):
        visible[random.randint(0,len(visible)-1)][2]=stone_w
        es_gibt_einen_stein=True
    
    
    
    for listpos in range(len(visible)):
        if visible[listpos][2]==wood_w[0] or visible[listpos][2]==wood_w[1]:
            es_gibt_einen_baum=True
    if not(es_gibt_einen_baum):
        visible[random.randint(0,len(visible)-1)][2]=wood_w[1]
        es_gibt_einen_baum=True
    
    
    
    stones=[]
    trees=[]
    for feld in visible:
        if feld[2]==stone_w:
            stones.append([feld[0]*feld_size,feld[1]*feld_size])
        if feld[2]==wood_w[0] or feld[2]==wood_w[1]:
            trees.append([feld[0]*feld_size,feld[1]*feld_size])
    
    if not(done):
        done=True
        create_start()
    
    
    
    if mouse_click[1]:
        cam_x-=mouse_pos_old[0]-mouse_pos[0]
        cam_y-=mouse_pos_old[1]-mouse_pos[1]
    
    for figurenpos in range(len(figuren)):
        if figuren[figurenpos][2]==2:
            figuren[figurenpos][0]-=mouse_pos_old[0]-mouse_pos[0]
            figuren[figurenpos][1]-=mouse_pos_old[1]-mouse_pos[1]
    for figurenpos in range(len(figuren)):
        if rel_mouse_pos[0]>figuren[figurenpos][0]-player_size and rel_mouse_pos[0]<figuren[figurenpos][0]+player_size:
            if rel_mouse_pos[1]>figuren[figurenpos][1]-player_size and rel_mouse_pos[1]<figuren[figurenpos][1]+player_size:
                figuren[figurenpos][2]=1
                figuren[figurenpos][3]=10
                if mouse_click[0]:
                    figuren[figurenpos][2]=2
    for figurenpos in range(len(figuren)):
        if figuren[figurenpos][3]==0:
            figuren[figurenpos][2]=0
        else:
            figuren[figurenpos][3]-=1
    
    
    
    
    for figurenpos in range(len(figuren)):
        check_on_stone=False
        for stonepos in range(len(stones)):
            if figuren[figurenpos][0]>stones[stonepos][0] and figuren[figurenpos][0]<stones[stonepos][0]+feld_size:
                if figuren[figurenpos][1]>stones[stonepos][1] and figuren[figurenpos][1]<stones[stonepos][1]+feld_size:
                    check_on_stone=True
                    if figuren[figurenpos][4][0]!="stone":
                        figuren[figurenpos][4]=["stone",500]
                else:
                    if stonepos==len(stones)-1:
                        if not(check_on_stone):
                            if figuren[figurenpos][4][0]=="stone":
                                figuren[figurenpos][4]=["",0]
            else:
                if stonepos==len(stones)-1:
                    if not(check_on_stone):
                        if figuren[figurenpos][4][0]=="stone":
                            figuren[figurenpos][4]=["",0]
    for figurenpos in range(len(figuren)):
        check_on_wood=False
        for woodpos in range(len(trees)):
            if figuren[figurenpos][0]>trees[woodpos][0] and figuren[figurenpos][0]<trees[woodpos][0]+feld_size:
                if figuren[figurenpos][1]>trees[woodpos][1] and figuren[figurenpos][1]<trees[woodpos][1]+feld_size:
                    check_on_wood=True
                    if figuren[figurenpos][4][0]!="wood":
                        figuren[figurenpos][4]=["wood",500]
                else:
                    if woodpos==len(trees)-1:
                        if not(check_on_wood):
                            if figuren[figurenpos][4][0]=="wood":
                                figuren[figurenpos][4]=["",0]
            else:
                if woodpos==len(trees)-1:
                    if not(check_on_wood):
                        if figuren[figurenpos][4][0]=="wood":
                            figuren[figurenpos][4]=["",0]
        
    
    
    
    
    
    
    for figurenpos in range(len(figuren)):
        if figuren[figurenpos][4][0]=="stone":
            figuren[figurenpos][4][1]-=1
            if figuren[figurenpos][4][1]==0:
                res_stone+=1
                figuren[figurenpos][4][1]=500
    for figurenpos in range(len(figuren)):
        if figuren[figurenpos][4][0]=="wood":
            figuren[figurenpos][4][1]-=1
            if figuren[figurenpos][4][1]==0:
                res_wood+=1
                figuren[figurenpos][4][1]=500
                
    
    if not(mouse_click[0]):
        for figurenpos in range(len(figuren)):
            for figurenpos2 in range(len(figuren)):
                if figurenpos!=figurenpos2:
                    if figuren[figurenpos2][0]+4>figuren[figurenpos][0]-4 and figuren[figurenpos2][0]-4<figuren[figurenpos][0]+player_size//2:
                        if figuren[figurenpos2][1]+player_size//2>figuren[figurenpos][1]-player_size//2 and figuren[figurenpos2][1]-player_size//2<figuren[figurenpos][1]+player_size//2:
                            if figuren[figurenpos][0]>figuren[figurenpos2][0]:
                                figuren[figurenpos][0]+=2
                            elif figuren[figurenpos][0]<figuren[figurenpos2][0]:
                                figuren[figurenpos][0]-=2
                            else:
                                figuren[figurenpos][0]+=1
                                
    text_stone = font.render(str(res_stone), True, color_text,color_text_bg) 
    text_wood = font.render(str(res_wood), True, color_text,color_text_bg)
    draw()
    pygame.display.update()
    #print(time.perf_counter()-start_time2)