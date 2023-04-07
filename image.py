from PIL import Image
from common import v2

pixel_scale = 255
high_pass = int(pixel_scale/2)
gamma = 1.2
def is_white_pixel(pix):
    return all([
        pix[0] > high_pass * gamma,
        pix[1] > high_pass * gamma,
        pix[2] > high_pass * gamma,]
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
