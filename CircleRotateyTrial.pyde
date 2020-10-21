g_NumBalls = 20
g_OuterRadius = 250
g_InnerRadius = 150
g_Freq1 = 2
g_Freq2 = 1.5

def setup():
    size(850, 850)
    #frameRate(0.2)
    
def draw():
    colorMode(RGB, 250)
    #background(80)
    println("###################")
    println("Drawing new frame")
    fill(80, 20)
    rect(0, 0, width, height)
    pushMatrix()
    colorMode(HSB, g_NumBalls)
    noStroke()
    translate(width/2, height/2)
    t = millis()/50000.0
    for iter in range(g_NumBalls):
        phase = 2 * iter
        p = getp(o(phase, 0.25 * phase, g_Freq2, 0.0, t), t)
        println(str(iter) + " " + str(p.x) + " " + str(p.y))
        fill(iter, g_NumBalls, g_NumBalls)
        ball_size = o(20.0, 10.0, 5.0, 0.0, 3 * t)
        ellipse(p.x, p.y, ball_size, ball_size)
    popMatrix();
    
def getp(phase, t):
    #freq = map(mouseX, 0, width, 0.01, 3)
    #phase = map(mouseY, 0, height, 0.01, 3)
    #p = r
    t1 = t
    p1 = r(g_Freq1, g_OuterRadius, phase, t1)
    t2 = t * 18
    p2 = r(g_Freq2, g_InnerRadius, phase, t2)
    return PVector.add(p1, p2)

def o(val, dev, freq, phase, s):
    return val + (dev * sin(((freq * s) + phase)))
    
def r(freq, amp, phase, s):
    return c((phase + (freq * s)), amp)
    
def c(phi, radius):
    return PVector(radius * cos(phi), radius * sin(phi))
