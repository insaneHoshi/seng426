from math import *
import curses, time

def main():
	global stdscr
	print "Welcome to my convex hull algorithm implementation using python and curses.  To set points click on the the terminal, to unset points click near a set point."
	
	raw_input("Press Enter to continue...")
	
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	curses.mousemask(1)
	"""
	while 1:
		c = stdscr.getch()
		if c == curses.KEY_MOUSE:
			screen.addstr("worked") 
		if c == ord('s'): break  # Exit the while()
		elif c == ord('r'): break  # Exit the while()
		elif c == ord('q'): break  # Exit the while()
	"""
	while True:
		event = stdscr.getch() 
		if event == ord("q"): break 
		if event == curses.KEY_MOUSE:
			_, mx, my, _, _ = curses.getmouse()
			y, x = stdscr.getyx()
			stdscr.addstr(y, x, str(x))
			stdscr.addstr(y, x, str(y))
	    
	curses.nocbreak(); stdscr.keypad(0); curses.echo()
	curses.endwin()

if __name__ == "__main__":
	main();
