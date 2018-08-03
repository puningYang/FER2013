# 将.csv文件还原为48*48的8位灰度图
import csv
import os
from PIL import Image
import numpy as np

datasets_path = 'G:/fer2013'
train_csv = os.path.join(datasets_path, 'train.csv')
val_csv = os.path.join(datasets_path, 'val.csv')
test_csv = os.path.join(datasets_path, 'test.csv')
train_set = os.path.join(datasets_path, 'train')
val_set = os.path.join(datasets_path, 'val')
test_set = os.path.join(datasets_path, 'test')

for save_path, csv_file in [(train_set, train_csv), (val_set, val_csv), (test_set, test_csv)]:
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    num = 1
    with open(csv_file) as f:
        csvr = csv.reader(f)
        header = next(csvr)
        # 使用enumerate遍历csvr中的标签(label)和特征值（pixel)
        for i, (label, pixel) in enumerate(csvr):
            # 将特征值的数组转化为48*48的矩阵
            pixel = np.asarray([float(p) for p in pixel.split()]).reshape(48, 48)
            subfolder = os.path.join(save_path, label)
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
            # 将该矩阵转化为RGB图像，再通过convert转化为8位灰度图像，L指灰度图模式，L=R*299/1000+G*587/1000+B*114/1000
            im = Image.fromarray(pixel).convert('L')
            image_name = os.path.join(subfolder, '{:05d}.jpg'.format(i))
            print(image_name)
            im.save(image_name)
