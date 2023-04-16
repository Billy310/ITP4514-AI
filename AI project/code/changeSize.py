import os
from PIL import Image

garder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

filedir = garder + '\Dataset\的士站\source'
os.listdir(filedir)

file_list1 = []
for root, dirs, files in os.walk(filedir):
    for file in files:
        if os.path.splitext(file)[1] == '.PNG':
            file_list1.append(os.path.join(root,file))

# 批量改变图片像素
for filename in file_list1:
    try:
        im = Image.open(filename)
        new_im = im.resize((128,128))

        new_filename = filename.split("\\")

        new_im.save(garder + '\Dataset\的士站\edit\\' + new_filename[-1])
        print('图片' + new_filename[-1] + ' 像素转换完成')
    except OSError as e:
        print(e.args)