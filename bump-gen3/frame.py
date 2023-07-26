import sys, os
from PIL import Image, ImageDraw, ImageFont

appearance = "GenericBump"
W,H = 1920,1080 #HACK - hardcoding ( we should consume it from the file)

with open(sys.argv[1], 'r') as f:
    message = f.read()

#img = Image.new('RGB', (W,H), 'black')
img = Image.open('Generic Template 16x9 - black and bug.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("HelveticaNeue-CondensedBold-05.ttf", 72)

if appearance == "GenericBump":
    sections = message.split(2*os.linesep)
    print(len(sections), "sections")

    section_message = ""
    for i in range(len(sections)):
        print("Section", i)
        section_message = section_message + sections[i] + "\n\n"
        print("Drawing text:", section_message)
        draw.text((192,89), section_message, anchor="la", align="left", font=font, fill='white', spacing=16)
        
        filename = sys.argv[1] + " - IMG" + str(i+1).zfill(4) + ".png"
        print("WRITING:", filename)
        img.save(filename)

else:
    draw.text((W/2, H/2), message, anchor="mm", align="center", font=font, fill='white')


