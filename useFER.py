# 项目数据集使用了表情识别的fer2013数据集
# 该数据集下载下来是.csv格式，需要先对数据集进行分割，得到train.csv, test.csv, val.csv
import csv
import os

database_path = r'H:/'  # 数据集的路径
datasets_path = r'G:/fer2013'
# 将路径组合后返回
csv_file = os.path.join(database_path, 'fer2013.csv')
train_csv = os.path.join(datasets_path, 'train.csv')
val_csv = os.path.join(datasets_path, 'val.csv')
test_csv = os.path.join(datasets_path, 'test.csv')

with open(csv_file) as f:
    # 使用csv中的reader()打开.csv文件
    csvr = csv.reader(f)
    # 将迭代器指向文件的第二行，第一行为标签
    header = next(csvr)
    rows = [row for row in csvr]
    # 按最后一列的标签将数据集进行分割
    trn = [row[:-1] for row in rows if row[-1] == 'Training']
    csv.writer(open(train_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + trn)
    print(len(trn))

    val = [row[:-1] for row in rows if row[-1] == 'PublicTest']
    csv.writer(open(val_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + val)
    print(len(val))

    tst = [row[:-1] for row in rows if row[-1] == 'PrivateTest']
    csv.writer(open(test_csv, 'w+'), lineterminator='\n').writerows([header[:-1]] + tst)
    print(len(tst))
