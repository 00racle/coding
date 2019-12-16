import ctypes
import base64

img_base64 = b'adflkjadf;lkjadf'
imgdata = base64.b64decode(img_base64)

img_result = open("C:\\Temp\dred.jpg", "wb")
img_result.write(imgdata)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Temp\\dred.jpg", 0)

img_result.close()
