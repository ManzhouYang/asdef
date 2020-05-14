import asdef, random
while True:
	name = input('Name: (type EXITs to leave)')
	if name == 'EXITs':
		break
	print()
	kinds = ['Baconburger', 'Hamburger', 'chips(fries)', 'ice cream', 'bacon fries']
	kind = random.choice(kinds)
	if kind == 'Baconburger':
		fills = 'bacon'
		fills2 = 'cucumber'
		fill3 = True
		fills3 = 'meat'
	elif kind == 'bacon fries':
		fills = 'bacon'
		fills2 = 'potato'
		fill3 = True
		fills3 = 'ketchup'
	elif kind == 'chips(fries)':
		fills = 'potato'
		fills2 = 'ketchup'
		fill3 = False
	elif kind == 'ice cream':
		fills = 'chocolate'
		fills2 = 'cream'
		fill3 = False
	elif kind == 'Hamburger':
		fills = 'meat'
		fills2 = 'cucumber'
		fill3 = False
	asdef.cheeseshop(kind)
	print('Name: ', name)
	print(fills, 'needs: YES')
	print(fills2, 'needs: YES')
	if fill3 == True:
		print(fills3, 'needs: YES')
	print()
	s = input('(yes or no) More ')
	if s == 'no':
		break
