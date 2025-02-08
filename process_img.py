from PIL import Image
from io import BytesIO

async def add_watermark(data):
#Create an Image Object from an Image
    im = Image.open( BytesIO(data))
    # width, height = im.size

    # draw = ImageDraw.Draw(im)
    # text = shop_name
    # font_size = int(width/20)
    # font = ImageFont.truetype('arial.ttf', font_size)
    # textwidth, textheight = draw.textsize(text, font)

    # # calculate the x,y coordinates of the text
    # margin = int(height/20)
    # x = width - textwidth - margin
    # y = height - textheight - margin

    # # draw watermark in the bottom right corner
    # draw.text((x, y), text, font=font,fill='#FFF',stroke_width=5,stroke_fill='#222')
    # # im.show()
    data = list(im.getdata())
    image_without_exif = Image.new('RGB', im.size)
    image_without_exif.putdata(data)
    with BytesIO() as f:
        image_without_exif.save(f, format="JPEG")
        return f.getvalue()