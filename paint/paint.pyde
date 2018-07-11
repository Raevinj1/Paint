redY = 160
redYE = 0
boxB = 700
boxE = 800
yellowY = 320
greenY = 480
blueY =640
pinkY = 800


def setup():
    size(800, 800)
    background (0)
    stroke(255,255,255) #box color
    
    
def draw():
    rect(700, 0, 100, 800) #color pallete box
    fill(0)
    rect(650, 0, 50, 800) #option box
    
    
    ellipse(675, 100, 45,45) 
    
    fill (255,0,0) # red color
    rect(700, 0, 100, 160) #red filled box
    fill(255,255,0) #yellow color
    rect(700, 160, 100, 160) #yellow filled box
    fill(0, 255, 0) #green color
    rect(700, 320, 100, 160) # green filled box
    fill(0, 0, 255) # blue color
    rect(700, 480, 100, 160) #blue filled box
    fill(255,0, 255) #pink color
    rect(700, 640, 100, 160) #pink fill box
    
    if mousePressed and mouseX < 650:
        line(pmouseX, pmouseY, mouseX, mouseY)
        
        
        
def mouseClicked():
    global redY, redYE, boxB, boxE, yellowY
    if mouseY <= redY and mouseY >= redYE and mouseX >= boxB and mouseX <= boxE:
        stroke (255,0,0)
        
    if mouseY <= yellowY and mouseY >= redY and mouseX >= boxB and mouseX <= boxE:
        stroke (255,255,0)
        
    if mouseY <= greenY and mouseY >= yellowY and mouseX >= boxB and mouseX <= boxE:
        stroke (0, 255, 0)
        
    if mouseY <= blueY and mouseY >= greenY and mouseX >= boxB and mouseX <= boxE:
        stroke (0, 0, 255)
        
    if mouseY <= pinkY and mouseY >= blueY and mouseX >= boxB and mouseX <= boxE:
        stroke (255,0, 255)
