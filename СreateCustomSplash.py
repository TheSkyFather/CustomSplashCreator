import io
import zipfile
import os

offset0 = 0x4000
offset1 = 0x5000
offset2 = 0x770000
offset3 = 0xEDB000
offset4 = 0x1646000

outpt = open("bin\logo.img", "wb")

emptyContent =  [0 for i in range(0x1CF5000)]

mi9offset = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
                0x6B, 0x07, 0x00, 0x00, 0x70, 0x07, 0x00, 0x00, 0x6B, 0x07, 0x00, 0x00,
                0xDB, 0x0E, 0x00, 0x00, 0x6B, 0x07, 0x00, 0x00, 0x46, 0x16, 0x00, 0x00,
                0x6B, 0x07]

outpt.write(bytearray(emptyContent))

outpt.seek(offset0)
outpt.write(bytearray(mi9offset))

outpt.seek(offset1)
img = open("pics\pic1.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset2)
img = open("pics\pic2.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset3)
img = open("pics\pic3.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset4)
img = open("pics\pic4.bmp", "rb")
outpt.write(img.read())
outpt.close()

myZipFile = zipfile.ZipFile("output\CustomSplash.zip", "w" )
myZipFile.write("bin\\logo.img", "logo.img", zipfile.ZIP_DEFLATED )
myZipFile.write("bin\\firmware-update\\xbl.img", "firmware-update\\xbl.img", zipfile.ZIP_DEFLATED )
myZipFile.write("bin\\firmware-update\\xbl_config.img", "firmware-update\\xbl_config.img", zipfile.ZIP_DEFLATED )
myZipFile.write("bin\\firmware-update\\uefisecapp.img", "firmware-update\\uefisecapp.img", zipfile.ZIP_DEFLATED )
myZipFile.write("bin\\updater-script", "META-INF\\com\\google\\android\\updater-script", zipfile.ZIP_DEFLATED )
myZipFile.write("bin\\update-binary", "META-INF\\com\\google\\android\\update-binary", zipfile.ZIP_DEFLATED )
os.remove("bin\logo.img")