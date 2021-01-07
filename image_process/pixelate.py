from PIL import Image

img = Image.open("OIP.jpg")
imgSmall = img.resize((32,32),resample=Image.BILINEAR)
result = imgSmall.resize(img.size,Image.NEAREST)
result.save('result.png')
