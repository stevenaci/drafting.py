from PIL import Image
from common import v2

def is_white_pixel(pix):
    high_pass = 150
    return all([
        pix[0] > 255 - high_pass,
        pix[1] > 255 - high_pass,
        pix[2] > 255 - high_pass,]
    )

def convert_to_lines(filename: str, scale_to: v2=None):
    image: Image.Image = Image.open(filename)
    if scale_to:
        image = image.resize(scale_to)

    points: list[v2] = []
    x, y = 0, 0
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            rgb_pixel = pixels[x,y]
            if not is_white_pixel(rgb_pixel):
                points.append(v2(x,y))

    return points
