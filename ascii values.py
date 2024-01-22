'''
ASCII:

To get ascii codes of characters, use ord('character').
To get character by giving ascii code, use chr(code).

'''

L={}
for i in range(12):
    L.update({i:chr(i)})
print(L)

print(ord('a'))
