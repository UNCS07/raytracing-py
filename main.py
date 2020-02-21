from image import Image
from color import Color, ctable


def test():
    WIDTH = 3
    HEIGHT = 2
    im = Image(WIDTH, HEIGHT)
    im.set_pixel(0, 0, 'r')
    im.set_pixel(0, 1, 'g')
    im.set_pixel(0, 2, 'b')
    im.set_pixel(1, 0, 'y')
    im.set_pixel(1, 1, 'k')
    im.set_pixel(1, 2, Color((0.01, 0, 0)))
    return im

def test_bonus():
    WIDTH = 256
    HEIGHT = 256
    im = Image(WIDTH, HEIGHT)
    for i in range(HEIGHT):
        ii = i/256
        im.set_pixel(i, None, Color((ii,ii,1)))
    return im

def main():
    im = test_bonus()

    with open('test2.ppm', 'w') as img_file:
        im.write_ppm(img_file)

if __name__ == '__main__':
    main()