import base64

with open("C:\\Users\\user\\Desktop\\img\\smileanon.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
print(encoded_string)