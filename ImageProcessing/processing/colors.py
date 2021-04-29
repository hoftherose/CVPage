from PIL import ImageOps

def img2gray(img):
    gray_img = ImageOps.grayscale(img)
    return gray_img

def img2neg(img):
    neg_img = ImageOps.invert(img)
    return neg_img