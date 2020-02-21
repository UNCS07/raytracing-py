from image import Image
from color import Color

def main():
    WIDTH = 3
    HEIGHT = 2
    im = Image(WIDTH, HEIGHT)
    im.set_pixel(0, 0, 'r')
    im.set_pixel(0, 1, 'g')
    im.set_pixel(0, 2, 'b')
    im.set_pixel(1, 0, 'y')
    im.set_pixel(1, 1, 'k')
    im.set_pixel(1, 2, Color((0.01, 0, 0)))

    with open('test.ppm', 'w') as img_file:
        im.write_ppm(img_file)

if __name__ == '__main__':
    main()