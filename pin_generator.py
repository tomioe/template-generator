from PIL import Image, ImageFont, ImageDraw, ImageOps

from config import GRID_SIZE

def draw_pin(text: str, color: str):
    size = (GRID_SIZE, GRID_SIZE)
    ellipse_image = Image.new("RGBA", size, (255,255,255))
    dr = ImageDraw.Draw(ellipse_image)

    # Many magic numbers
    diameter=8
    radius=diameter/2
    center = (4,45)
    x0, y0 = center[0]-radius, center[1]-radius
    x1, y1 = center[0]+radius, center[1]+radius
    dr.ellipse([x0, y0, x1, y1], outline="black", fill=color)
    
    # Magic numbers
    # TODO: If we exceed ~8-9 characters, might be worth splitting text into two lines
    text_position = (int(x1)-7, int(y0)-23)

    # make a blank image for the text, initialized to transparent text color
    text_image = Image.new('RGBA', size, (255,255,255,0))
    # get a drawing context
    d = ImageDraw.Draw(text_image)

    # get a font
    fnt = ImageFont.truetype('arial.ttf', 10)
    # draw text, full opacity
    d.text(text_position, text, font=fnt, fill=(0,0,0,255))

    out = Image.alpha_composite(ellipse_image, text_image.rotate(45, expand=False, resample=Image.BICUBIC))
    return out



