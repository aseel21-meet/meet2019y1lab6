import turtle
turtle.goto(0,0)
turtle.direction= None
def up():
    turtle.direction= 'Up'
    print('you pressed the up key')
    on_move()
def down():
    turtle.direction= 'Down'
    print('you pressed the down key')
    on_move()
def left():
    turtle.direction= 'Left'
    print('you pressed the left key')
    on_move()
def right():
    turtle.direction= 'Right'
    print('you pressed the right key')
    on_move()
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,"Left")
turtle.onkey(right,'Right')
turtle.listen()
def on_move():
   pos1=turtle.pos()
   x_cor=pos1[0]
   y_cor=pos1[1]
   if turtle.direction=='Up':
              turtle.goto(x_cor,y_cor+20)
   elif turtle.direction=='Down':
              turtle.goto(x_cor,y_cor-20)
   elif turtle.direction=='Left':
              turtle.goto(x_cor-20,y_cor)
   elif turtle.direction=='Right':
              turtle.goto(x_cor+20,y_cor)
def space():
    turtle.isdown()
    turtle.up()
    turtle.down()
turtle.onkey(space,'Space')


    
turtle.mainloop()

       
