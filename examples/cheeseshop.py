from random import choice
from asdef import cheeseshop
while True:
	kinds = ['Baconburger', 'Chips(pomes frites)', 'Hamburger']
	fill = ['cheese', 'bacon', 'potato']
	kind = choice(kinds)
	fts = choice(fill)
	cheeseshop(kind)
	s = input('(yes or no) More ')
	if s == 'no':
		break
