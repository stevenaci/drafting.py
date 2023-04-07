import argparse
from artist import Artist
from image import convert_to_lines
from common import v2


def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--filename", help="Width of the final drawing", default="test.jpg")
    parser.add_argument("--width", help="Width of the final drawing", default=710, type=int)
    parser.add_argument("--height", help="Height of the final drawing", default=710, type=int)
    parser.add_argument("--scaling", help="Spreads out the points by a factor, useful if you're drawing with a big brush for example", default=2, type=int)
    parser.add_argument('--draw-delay', help="Delay between mouse actions", default=0.0000, type=int)

    artist = Artist()
    args = parser.parse_args()
    filename, height, width, scaling, draw_delay = (
        args.filename, args.height, args.width, args.scaling, args.draw_delay
    )
    points = convert_to_lines(
        filename=filename, 
        scale_to=(
            int(height/scaling), int(width/scaling)
        )
    )
    artist.draw_points(points, v2(scaling,scaling), draw_delay=draw_delay)


if __name__ == '__main__':
    main()