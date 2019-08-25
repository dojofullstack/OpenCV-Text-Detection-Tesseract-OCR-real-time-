# try:
#     import Image
# except ImportError:
#     from PIL import Image


img = cv2.imread('/home/henry/Downloads/vex.jpg')

@timeit
def test():
    # print(pytesseract.image_to_string('/home/henry/Downloads/vex.jpg'))
    # print(pytesseract.image_to_string(Image.open('/home/henry/Downloads/vex.jpg')))
    print(pytesseract.image_to_string(img, lang='en'))
    # print(pytesseract.image_to_data(img))
    cv2.imwrite('img.jpg', img)
