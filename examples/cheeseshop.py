from asdef import cheeseshop
while True:
    kinds = ['Baconburger', 'Chips(pomes frites)', 'Hamburger']
    ft = ['cheese', 'bacon', 'potato']
    kind = random.choice(kinds)
    fts = random.choice(ft)
    cheeseshop(kind,
	       fts = 'YES')
     s = input('(no or yes)More ')
     if s == 'no':
	     break
