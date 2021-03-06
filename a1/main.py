from math import *
import curses, time

#plot function to rearrange the xy coords

def sign(x):
    if x < 0: return -1
    return 1
    
def plot(x, y, col):
    stdscr.addch(y, x, col)

def dline(p1,p2, ch):

    from_x = p1[0] 
    from_y = p1[1] 
    x2 = p2[0]
    y2 = p2[1]
    dx = x2 - from_x
    dy = y2 - from_y

    ax = abs(dx * 2)
    ay = abs(dy * 2)

    sx = sign(dx)
    sy = sign(dy)

    x = from_x
    y = from_y

    if ax > ay:
        d = ay - ax // 2

        while True:
            plot(x, y, ch)
            if x == x2:
                return

            if d >= 0:
                y += sy
                d -= ax
            x += sx
            d += ay
    else:
        d = ax - ay // 2

        while True:
            plot(x, y, ch)
            if y == y2:
                return

            if d >= 0:
                x += sx
                d -= ay
            y += sy
            d += ax

#Use the Z computation of the cross product to determine which way things turn
def isRightTurn(a,b,c):
	i = [b[0]-a[0],b[1]-a[1]]
	j = [c[0]-b[0],c[1]-b[1]]
	k = i[0]*j[1] - i[1]*j[0]
	if(k<0):
		return True
	else:
		return False

def doConvexHull(p):
	lUpper = []
	lLower = []
	n=len(p)
	p.sort()
	p = sorted(p,key=lambda x:x[1])
	
	
	
	lUpper.append(p[0])
	lUpper.append(p[1])
	
	i=2;
	while i<n:
		lUpper.append(p[i])
		while len(lUpper)>2 and not isRightTurn(lUpper[-3],lUpper[-2],lUpper[-1]):
			lUpper.pop(-2)
		i+=1
	
	p.reverse()
	
	
	lLower.append(p[0])
	lLower.append(p[1])
	
	i=2;
	while i<n:
		lLower.append(p[i])
		while len(lLower)>2 and not isRightTurn(lLower[-3],lLower[-2],lLower[-1]):
			lLower.pop(-2)
		i+=1
	
	lLower.pop(0)
	
	return lUpper+lLower
	

def main():
	global stdscr
	pointList = []
	print "Welcome to my convex hull algorithm implementation using python and curses.  To set points click on the the terminal, to unset points click near a set point.\n"
	print "This application is only stable with linux terminals and python 2.x\n"
	print "Note the resolution is dependent on your Unix terminal, increase it for greater resolution\n"
	
	raw_input("Press Enter to continue...")
	
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	curses.mousemask(1)
	windowYSize = stdscr.getmaxyx()[0]
	stdscr.addstr(windowYSize-1,0,"Press (s) to start the Convex Hull Alg, (r) to reset or (q) to quit")
	while True:
		event = stdscr.getch() 
		if event == ord("q"): break
		elif event == ord("r"): 
			stdscr.clear()
			pointList = []
			stdscr.addstr(windowYSize-1,0,"Press (s) to start the Convex Hull Alg, (r) to reset or (q) to quit")
		elif event == ord("s"):
			stdscr.clear()
			stdscr.addstr(windowYSize-1,0,"Press (s) to start the Convex Hull Alg, (r) to reset or (q) to quit")
			if(len(pointList)>1):
				convexHull = doConvexHull(pointList)
				i = 0
				while i<len(convexHull)-1:
					dline(convexHull[i],convexHull[i+1],".")
					i+=1
					
			for point in pointList:
				plot(point[0],point[1],"o")
			
		if event == curses.KEY_MOUSE:
			_, mx, my, _, _ = curses.getmouse()
			if(my<windowYSize-1):
				testPoint = [mx,my]
				if(testPoint in pointList):
					pointList.remove(testPoint)
					plot(mx,my," ")
				else:
					pointList.append([mx,my])
					plot(mx,my,"o")
	    
	curses.nocbreak(); stdscr.keypad(0); curses.echo()
	curses.endwin()
	
	

if __name__ == "__main__":
	main();
