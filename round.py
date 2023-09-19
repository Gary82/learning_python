a = 3.5
print(round(a))

# Will take the closer even number
b = 2.5
print(round(b))

c = 35
print(round(c,-1))

d = 25
print(round(d,-1))

print('-----------------------------------')

e = 0.35
print(round(e,1))
print(format(e,".20f"))

f = 0.45
print(round(f,1))
print(format(f,".20f"))

print('-----------------------------------')

import decimal
g = decimal.Decimal('0.15')
print(format(g,".20f"))
print(round(g,1))

h = decimal.Decimal(0.15)
print(format(h,".20f"))
print(round(h,1))

