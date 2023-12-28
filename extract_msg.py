from PIL import Image, ImageChops

i = Image.open("o2.png").convert('RGB')

a = ' '
w =639
h =726
for x in range(w):
    for y in range(h):
    
        r,g,b = i.getpixel((x,y))
        if (x % 726 == 0):
            a += chr(g)
print (a) 
    
    
