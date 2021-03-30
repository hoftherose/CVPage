from PIL import ImageOps

def img2gray(img):
    gray_img = ImageOps.grayscale(img)
    return gray_img