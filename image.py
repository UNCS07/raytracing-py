from color import Color


class Image:

    def __init__(self, w, h, mcol=255):
        self.w = w
        self.h = h
        self.pixels = [[None for _ in range(w)] for _ in range(h)]
        self.max_color = mcol

    def set_pixel(self, x, y, color):
        if type(color) not in (Color, str):
            raise TypeError
        if type(color) is str:
            c = Color()
            color = c.set_as(color)
        if y is None:
            for i in range(self.w):
                self.pixels[x][i] = color
        elif x is None:
            for i in range(self.h):
                self.pixels[i][y] = color
        else:
            self.pixels[x][y] = color

    def write_ppm(self, img_file):
        def to_byte(c):
            return round(c * self.max_color)
        img_file.write('P3 {} {}\n255\n'.format(self.w, self.h))
        for row in self.pixels:
            for color in row:
                img_file.write('{} {} {} '.format(
                    to_byte(color.d[0]), to_byte(color.d[1]), to_byte(color.d[2])
                    )
                )
            img_file.write('\n')


