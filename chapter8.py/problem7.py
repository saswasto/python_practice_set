def remove(l,new):
    n = []
    for i in l:
        if i not in new:
            n.append(i.strip(new))
    return n
l= ["Harry","Larry","Carry","Marie"]
print(remove(l,"ry"))