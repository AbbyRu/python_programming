stuff = {"food":15, "energy":100,"enemies":3}

#dictionary methods
#print(stuff.get("food"))
#print(stuff.items())
#print(stuff.keys())

#print(stuff.popitem())
#print(stuff)

'''
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends",123))
print(stuff)
'''

new_items = {"rocks":4,"arrows":18}
stuff.update(new_items)
print(stuff)

new_items ={"rocks":13,"arrows":6}
stuff.update(new_items)
print(stuff)

up_new ={"food":3,"webs":2}
stuff.update(up_new)
print(stuff)

stuff.update(food=300, cookies=3)
print(stuff)