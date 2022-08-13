
def pointinrect(x, y):
	if x >= 124 and x <= 174 and y >= -123 and y <= -86:
		return True
	return False

res = 0
worked = []
for iy in range(-500, 800):
	for ix in range(-200, 200):
		velx = ix
		vely = iy
		x = 0
		y = 0
		highest = 0
		for i in range(300):
			if y > highest:
				highest = y
			if pointinrect(x, y):
				worked.append((ix, iy))
				if highest > res:
					res = highest
				break
			x += velx
			y += vely
			if velx < 0:
				velx += 1
			elif velx > 0:
				velx -= 1
			vely -= 1

print(res)
print(len(worked))
