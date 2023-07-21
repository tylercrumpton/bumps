from PIL import Image, ImageDraw, ImageFont

message = "Testing one\ntwo three.\nfour five\nsix seven\neight nine\nten"
message = "This is\ntwo lines"
W,H = 1920,1080

#img = Image.open("sample_in.jpg")
img = Image.new('RGB', (W,H), 'black')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("HelveticaNeue-CondensedBold-05.ttf", 72)

#multiline shit
lines = message.splitlines();
print(len(lines), "lines")

_,_,_,lineheight = draw.textbbox((0,0), lines[0], font=font)
print("Line height is", lineheight)

draw.text((W/2, H/2), message, anchor="mm", align="center", font=font, fill='white')


#_, _, w, h = draw.textbbox((0, 0), message, font=font)
#print("bbox:", w,h)
#
#for i, line in enumerate(lines):
#    print("Rendering line", i, ":", line)
#    _, _, w, h = draw.textbbox((0, 0), line, font=font)
#
#    if len(lines)%2 == 0:
#        #even number of lines
#        offset = (lineheight*i) - (lineheight*(len(lines)-1))/2
#    else:
#        #odd number of lines
#        offset = 0 #TODO
#    draw.text(((W-w)/2, (H-h)/2 + offset), line, font=font, fill='white')

img.save('sample-out.jpg')
