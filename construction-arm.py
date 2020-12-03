from glife.base import *
import golly as g

vacuum = pattern("")
g.setalgo("HashLife")
g.autoupdate(True)

def dfs(depth, current):
	current.display("Single-Channel Recipe Search")
	# Place block at the appropiate place
	(block (g.getrect()[0]-11, g.getrect()[1]-10) + current).display("Single-Channel Recipe Search")
	# Filter boring one-glider solutions out
	if int(g.getpop()) == 9:
		return
	bread = g.getrect()[0] # old block x coordinate
	sinkship = g.getrect()[1] # old block y coordinate
	g.run(44)
	if g.empty():
		# Use g.empty not g.getpop
		# Big speedup
		return
	g.setstep(5)
	g.step()
	if g.getrect()[0] - bread > 100 or g.getrect()[1] - sinkship > 100:
		return # Sorry
	if depth == 22:
		if int(g.getpop()) == 4:
			bruh = str(g.getrect()[0]-bread) + str(g.getrect()[1]-sinkship) + ".rle" # The offset
			g.reset()
			g.save(bruh, "rle")
		return
	dfs(depth+1, glider + current[44]) # Assume the next glider is present
	dfs(depth+1, vacuum + current[44]) # Assume the next glider is absent
# dfs(0, glider)
dfs(0, pattern("b2o$2o$2bo9$12b2o$11b2o$13bo9$23b2o$22b2o$24bo9$34b2o$33b2o$35bo!"))

# I suspect p44 is a deadend
