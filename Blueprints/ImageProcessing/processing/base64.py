from PIL import Image
import io
import base64

def encode(img):
    buf = io.BytesIO()
    img.save(buf, "png")
    img_data = base64.b64encode(buf.getvalue())
    return img_data.decode()

def decode(img_64):
    img_data = base64.b64decode(img_64)
    i = io.BytesIO(img_data)
    return Image.open(i)