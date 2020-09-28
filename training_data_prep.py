import glob
from shutil import copyfile

# files = glob.glob("train_v2_labels//*.txt")
# for file_name in files:
#     name = file_name.split('/')[1].split('.')[0]
#     if name == 'classes':
#         continue
#     copyfile('train_v2/{0}.jpg'.format(name),'custom_data/images/{0}.jpg'.format(name))
#     copyfile('train_v2_labels/{0}.txt'.format(name),'custom_data/images/{0}.txt'.format(name))
file_names = []

files = glob.glob("train_v2_labels//*.txt")
for file_name in files:
    name = file_name.split('/')[1].split('.')[0]
    if name == 'classes':
        continue

    file_names.append('custom_data/images/{0}.jpg'.format(name))