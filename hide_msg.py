from PIL import Image
i=Image.open('d.png').convert('RGBA')
w,h = i.size

he = 133,72,143,1
ll = 133,69,143,1
o = 133,76,143,1
lo = 133,76,143,1
ol = 133,79,143,1
x=0
y=0

z=0
f=1

a=0
n=2

b=0
c=3

g=0
h=4
     
i.putpixel((x,y),he)
i.putpixel((z,f),ll)
i.putpixel((a,n),o)
i.putpixel((b,c),lo)
i.putpixel((g,h),ol)

i.save('o2.png')
