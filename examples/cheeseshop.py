import asdef, random
while True:
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
    asdef.cheeseshop(kind)
    print(fills, ': YES')
