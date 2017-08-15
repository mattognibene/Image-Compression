from PIL import Image
#tree method?
file = input("Enter file name: ")
im = Image.open(file)
pix=im.load()

def find_average(a):
    return int(a/4)

compressed = []

for x in range(0,im.size[0],2):
    for y in range(0,im.size[1],2):
        r = 0
        g = 0
        b = 0
        for v in range(0,2):
            for c in range(0,2):
                r += pix[x+v, y+c][0]
                g += pix[x+v, y+c][1]
                b += pix[x+v, y+c][2]
        rgb = (find_average(r), find_average(g), find_average(b))
        compressed.append(rgb)
        for v in range(0,2):
            for c in range(0,2):
                im.putpixel((x+v,y+c),rgb)
    if(x%100 == 0):
        print(int(100*x/im.size[0]) , " percent complete")

print("complete")

im.save("new.png")
print(compressed)








