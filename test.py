x = 40
y = x
s = 0

while (x & 1 == 0):
    s = s+1
    x = (x >> 1)   

q = 2 ** s
r = y // q
print(y, x, s, q,  r)

