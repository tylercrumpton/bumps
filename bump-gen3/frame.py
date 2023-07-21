from PIL import Image, ImageDraw, ImageFont

message = "Testing one\ntwo three."
W,H = 1920,1080

#img = Image.open("sample_in.jpg")
img = Image.new('RGB', (W,H), 'black')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("HelveticaNeue-CondensedBlack-10.ttf", 16)

_, _, w, h = draw.textbbox((0, 0), message, font=font)
#draw.text((0, 0),"Sample Text",(255,255,255),font=font)
draw.text(((W-w)/2, (H-h)/2), message, font=font, fill='white')

img.save('sample-out.jpg')
