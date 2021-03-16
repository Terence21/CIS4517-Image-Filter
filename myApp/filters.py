from PIL import Image, ImageOps, ImageFilter


def imageFilter(path, filter_type):
    filter_type = filter_type.toLowerCase()
    im = Image.open('uploads/' + path)
    if filter_type == 'gray':
        im = ImageOps.grayscale(im)
    if filter_type == 'sepia':
        im = convertSepia(path)
    if filter_type == 'poster':
        im = ImageOps.posterize(im, 4)
    if filter_type == 'blur':
        im = im.filter(ImageFilter.BLUR)
    if filter_type == 'edge':
        im = im.filter(ImageFilter.FIND_EDGES)
    if filter_type == 'solar':
        im = ImageOps.solarize(im)


def convertSepia(path) -> Image:
    img = Image.open('uploads/' + path)
    width, height = img.size

    pixels = img.load()

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return img
