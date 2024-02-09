import golly as g
o = g.getrect()[:2]
for y in range(0, 100, 20):
    x = 0
    while 1:
        cells = g.getcells([o[0]-5+x, o[1]-5+y, 20, 20])
        if not cells: break
        g.select([o[0]-5+x, o[1]-5+y, 20, 20])
        g.advance(0, 1)
        cells2 = g.getcells(g.getselrect())
        g.clear(0)
        g.putcells(cells, 0, 0)
        g.putcells(cells2, 0, 20) 
        x += 20
