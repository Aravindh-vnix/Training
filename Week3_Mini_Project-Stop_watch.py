# template for "Stopwatch: The Game"

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# define global variables
counter  = 0
interval = 100
n = 0
m = 0
stop = True

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()

def stop():
    global n, m, stop, counter
    if counter % 10 == 0 and counter != 0:
        n += 1
        m += 1
    elif counter != 0 :
        n += 1
    else:
        print ""
    
    timer.stop()

def reset():
    global counter, n, m
    counter = 0
    stop = True
    n = 0
    m = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval

def format(t):
    a = int(t/100) % 6
    b = int(t/600) % 600
    c = int(t/10) % 10
    d = (t) % 10
    string = str(b) + ":" + str(a) + str(c) + "." + str(d)
    return string
    
# define draw handler


def draw(canvas):
    text = format(counter)
    canvas.draw_text( text, [290,400],100, "white")
    canvas.draw_text("Press Stop when you see the whole number", [10,25], 30, "red") 
    canvas.draw_text( "    Total number of win(s):" +str(m), [450, 630], 30, "green")
    canvas.draw_text( "Total number of attempts:" +str(n), [455, 660], 30, "green")
    

# define helper function format that converts time

# in tenths of seconds into formatted string A:BC.D

def timer_handler():
    global counter
    counter += 1

# create frame
frame = simplegui.create_frame("Stop watch", 800, 800)


# register event handlers
frame.set_draw_handler(draw)

button1 = frame.add_button("Start", start, 150)
button2 = frame.add_button("Stop", stop, 150)
button3 = frame.add_button("Reset", reset, 150)

timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()
reset()

# Please remember to review the grading rubric

