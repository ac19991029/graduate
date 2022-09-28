# from PIL import Image


# img=Image.open(r'C:\Users\阿超\Desktop\test.png')
# print(type(img))
import base64

image=r'C:\Users\阿超\Desktop\test.png'
# print(type(image))


def imageToStr(image):
    with open(image, 'rb') as f:
        image_byte = base64.b64encode(f.read())
        # print(type(image_byte))
    image_str = image_byte.decode('ascii')  # byte类型转换为str
    # print(image_str)
    return image_str


image1 = imageToStr(image)
print(len(image1))
