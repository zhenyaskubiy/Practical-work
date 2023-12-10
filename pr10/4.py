from PIL import Image

def create_gradient(width, height, start_color, end_color):
    img = Image.new('RGBA', (width, height))
    r1, g1, b1, a1 = start_color
    r2, g2, b2, a2 = end_color

    for y in range(height):
        r = int(r1 + (r2 - r1) * y / height)
        g = int(g1 + (g2 - g1) * y / height)
        b = int(b1 + (b2 - b1) * y / height)
        a = int(a1 + (a2 - a1) * y / height)

        for x in range(width):
            img.putpixel((x, y), (r, g, b, a))

    return img

width = 300
height = 200
start_color = (0, 0, 255, 255) 
end_color = (255, 204, 0, 255) 

gradient_image = create_gradient(width, height, start_color, end_color)
gradient_image.show()  
