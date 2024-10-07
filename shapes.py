import pgzrun
def draw():
    screen.clear()
    screen.fill('green')   
    screen.draw.line((50,50), (300,50),'black')
    screen.draw.filled_circle((200,200),50, 'purple')
    rect=Rect((300,300), (100,200))
    screen.draw.rect(rect, 'red')
    screen.draw.text("e=mc²",(500,200),color='red')
pgzrun.go()
