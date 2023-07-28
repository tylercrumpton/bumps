import sys, os
from PIL import Image, ImageDraw, ImageFont

#appearance = "GenericBump"
appearance = "DearDCTV"
W,H = 1920,1080 #HACK - hardcoding ( we should consume it from the file)

with open(sys.argv[1], 'r') as f:
    message = f.read()

#img = Image.new('RGB', (W,H), 'black')
img = Image.open('Generic Template 16x9 - black and bug.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("HelveticaNeue-CondensedBold-05.ttf", 72)

#needed for some types of render where we need to go line by line.
_,_,_,lineheight = draw.textbbox((0,0), "test Text 123", font=font)
print("Line height is", lineheight)

if appearance == "GenericBump":
    sections = message.split(2*os.linesep)
    print(len(sections), "sections")

    section_message = ""
    for i in range(len(sections)):
        print("Section", i)
        section_message = section_message + sections[i] + "\n\n"
        draw.text((192,89), section_message, anchor="la", align="left", font=font, fill='white', spacing=16)
        
        filename = sys.argv[1] + " - IMG" + str(i+1).zfill(4) + ".png"
        print("WRITING:", filename)
        img.save(filename)
if appearance == "DearDCTV":
    sections = []
    this_section = ""
    for line in message.splitlines():
        if line == "":
            #this was a double newline, time to finish the section, but preload the next newline to keep spacing
            if len(this_section) > 0: sections.append(this_section)
            this_section = "\n"
        elif line.startswith("Dear ") or line.endswith("]"):
            #Dear DCTV
            if len(this_section) > 0: sections.append(this_section)
            sections.append(line)
            this_section = ""
        else:
            this_section += line
            this_section += "\n"
    if len(this_section) > 0: sections.append(this_section)

    sections = [section.removesuffix("\n") for section in sections]

    #do the damn thing
    offset = 0
    for i in range(len(sections)):
        lines = sections[i].splitlines()
        print("Section", i, "(" + str(len(lines)) + ")", sections[i])
        if len(lines) == 0:
            print("This section is just a blank line, so we will just increment the offset and move on without writing anything")
            offset += lineheight + 16
            continue

        for line in lines:
            #defaults
            anchor = "la" #reference points. x=leftmost point, y=top of ascenders of top line
            align = "left"
            fill = "white"
            xanchor = 192
            yanchor = 89

            #overrides
            if len(sections) == 1:
                print("There is exactly one section so I am centering everything")
                xanchor = W/2
                yanchor = H/2
                anchor = "mm"
                align = "center"
            elif line.startswith("Dear "):
                fill = "#ffff90" #yellow
            elif line.endswith("]"):
                align = "right"
                anchor = "ra"
                xanchor = W - xanchor

            draw.text((xanchor,yanchor+offset), line, anchor=anchor, align=align, font=font, fill=fill, spacing=16)
            offset += lineheight + 16
        
        filename = sys.argv[1] + " - IMG" + str(i+1).zfill(4) + ".png"
        print("WRITING:", filename)
        img.save(filename)



