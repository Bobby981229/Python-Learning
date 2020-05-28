"""
操作图像
"""

from PIL import Image

# 读取图像
image = Image.open('C:\\Users\\72946\\Pictures\\QQ.jpg')
image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
image.show()

# 剪裁图像
rect = 80, 20, 310, 360
image.crop(rect).show()

# 生成缩略图
size = 128, 128
image.thumbnail(size)
image.show()

# 缩放和黏贴图像
image1 = Image.open('xxx.png')
image2 = Image.open('xxx.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

# 旋转和翻转
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
image = Image.open('./res/guido.jpg')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

    image.show()

# 滤镜效果
from PIL import Image, ImageFilter

image = Image.open('./res/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()

# 处理Excel电子表格
# Python的openpyxl模块让我们可以在Python程序中读取和修改Excel电子表格
# 当然实际工作中，我们可能会用LibreOffice Calc和OpenOffice Calc来处理Excel的电子表格文件
# 这就意味着openpyxl模块也能处理来自这些软件生成的电子表格

# 处理Word文档
# 利用python-docx模块，Pytho 可以创建和修改Word文档
# 当然这里的Word文档不仅仅是指通过微软的Office软件创建的扩展名为docx的文档
# LibreOffice Writer和OpenOffice Writer都是免费的字处理软件

# 处理PDF文档
# PDF是Portable Document Format的缩写，使用.pdf作为文件扩展名
