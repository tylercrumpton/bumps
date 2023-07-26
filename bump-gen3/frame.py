from PIL import Image, ImageDraw, ImageFont

appearance = "GenericBump"
#message = "Dear DCTV,\nI heard some rumors about the Dragon Con\nmemberships and badges that feel strange and I\nwant you to help me suss out if they're fact or fiction.\nThanks!\n[ Andrew ]\n\nDear Andrew,\nSure, let's have at em."
message = "Generic Bump - start at top of safe area\n\nSkip a line between paragraphs\n\nMove to new page as necessary and avoid putting\ntext that overlaps the bug in the corner\n\nPage cuts should be in sync with music\nto make transitions 'smooth'"
W,H = 1920,1080

#img = Image.open("sample_in.jpg")
#img = Image.new('RGB', (W,H), 'black')
img = Image.open('Generic Template 16x9 - black and bug.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("HelveticaNeue-CondensedBold-05.ttf", 72)

#multiline shit
lines = message.splitlines();
print(len(lines), "lines")

_,_,_,lineheight = draw.textbbox((0,0), lines[0], font=font)
print("Line height is", lineheight)

if appearance == "GenericBump":
    #draw.text((W/2, H/2), message, anchor="mm", align="left", font=font, fill='white', spacing=20)
    draw.text((192,89), message, anchor="la", align="left", font=font, fill='white', spacing=16)
else:
    draw.text((W/2, H/2), message, anchor="mm", align="center", font=font, fill='white')


img.save('sample-out.png')
