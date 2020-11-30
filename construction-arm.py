from glife.base import *
import golly as g
import random

vacuum = pattern("")
g.setalgo("HashLife")
g.autoupdate(True)

def dfs(depth, current):
	if depth == 15:
		current.display("Single-Channel Recipe Search")
		(block (g.getrect()[0]-11, g.getrect()[1]-10) + current).display("Single-Channel Recipe Search")
		if int(g.getpop()) == 9:
			return
		bread = g.getrect()[0]
		sinkship = g.getrect()[1]
		g.setstep(5)
		g.step()
		if int(g.getpop()) == 4:
			bruh = str(g.getrect()[0]-bread) + str(g.getrect()[1]-sinkship) + ".rle"
			g.reset()
			g.save(bruh, "rle")
		return
	dfs(depth+1, glider + current[44])
	dfs(depth+1, vacuum + current[44])
dfs(0, glider)
