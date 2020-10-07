import turtle
def ydenzo (t, h, p):
    assert type(t) is turtle.Turtle
    assert type(p) is int and p >= 0
    
    t.forward(h)
    if p != 0:
        t.left(45)
        t.forward(h)
        t.right(90)
        t.forward(h)
        t.right(90)
        ydenzo(t,h,p-1)
    

t= turtle.Turtle()
t.setheading(90)
ydenzo(t,50,8) 
    
    




