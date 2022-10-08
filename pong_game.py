# turtleبتساعد انى ارسم اشكال  وتتحرك وكدان
#انها بتعمل الشاشة اللى بتطلع عل بايثون
import turtle
wind = turtle.Screen()
wind.title(" ping pong by Ali Abdelmoaty") #العنوان
wind.bgcolor("black")#بنحدد لون الشاشة اللى هتطلع
wind.setup(width=800 , height=600) #بنعمل الطول والعرض
wind.tracer(0)#stop update 
#___________________________________________________

#madrab1
madrab1= turtle.Turtle()
madrab1.speed(0)#تحديد سرعة عمل المضرب عل الشاشة
madrab1.shape("square")#شكل المضرب
madrab1.color("white")#لون المضرب
madrab1.shapesize(stretch_wid=6 , stretch_len=1)#طول وعرض المضرب
madrab1.penup()#تمنع اي خطوط تظهر
madrab1.goto(350 , 0)#مكان ظهور المضرب عل الشاشة
#--------------------------------------------

#madrad2
madrab2 = turtle.Turtle()
madrab2.speed(0)  # تحديد سرعة عمل المضرب عل الشاشة
madrab2.shape("square")  # شكل المضرب
madrab2.color("red")  # لون المضرب
madrab2.shapesize(stretch_wid=6, stretch_len=1)  # طول وعرض المضرب
madrab2.penup()  # تمنع اي خطوط تظهر
madrab2.goto(-350, 0)
#----------------------------------

#ball
ball = turtle.Turtle()
ball.speed(0)  # تحديد سرعة عمل المضرب عل الشاشة
ball.shape("circle")  # شكل المضرب
ball.color("blue")  #لون المضرب
ball.penup()  # تمنع اي خطوط تظهر
ball.goto(0, 0)
ball.dx = .1 #بنحدد سرعة الكورة وهتطلع لفوق ولا تحت 
ball.dy = .1
#-----------------------------------------------------
 
#functions
def madrab1_up():
    y= madrab1.ycor()#بنحدد مكان المضرب
    y+=20 #بنزود مقدار تحرك المضرب
    madrab1.sety(y) #بخليها تجدد مكان الضرب
    
#-----------------------------------------------
def madrab1_down():
    x= madrab1.ycor()
    x -=20
    madrab1.sety(x)
    

#--------------------------------------------------
def madrab2_up():
    z= madrab2.ycor()
    z += 20
    madrab2.sety(z)

#-----------------------------------------------------
def madrab2_down():
    q = madrab2.ycor()
    q -= 20
    madrab2.sety(q)

#--------------------------------------------------------
#نربط الكيبورد بالعبة

wind.listen() #بقول للبرنامج تتوقع ان في كيبورد

wind.onkeypress(madrab1_up , "w")
wind.onkeypress(madrab1_down, "s")

wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

while True:
    wind.update()
    #كل ما الشاشة هتشتغل تحدث من نفسها ويخلي الشاشة تفضل شغالة
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) #كل ما اللعبة تشتغل بتكون ف النص وبنزود عليه 
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
  
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        
    #------------------------------------------------------
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2. ycor - 40):
        ball.setx(340)
        ball.dx *=-1
    
    if (ball.xcor() < -340 and ball.xcor() < 350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1. ycor - 40):
        ball.setx(-340)
        ball.dx *= -1
