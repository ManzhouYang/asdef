from random import choice
from asdef import cheeseshop
while True:
	kinds = ['Baconburger', 'Chips(pomes frites)', 'Hamburger']
	fill = ['cheese', 'bacon', 'potato']
	kind = choice(kinds)
	fts = choice(fill)
	cheeseshop(kind,
		   fts='YES')
	s = input('(yes or no) More ')
	if s == 'no':
		break
