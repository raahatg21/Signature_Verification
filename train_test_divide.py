# Divide the data into training, testing and validation sets

import os
import shutil
import random

TRAIN_SIZE = 0.7
VAL_SIZE = 0.15
TEST_SIZE = 0.15

source_dir = '/home/raahat/Documents/Signet/Datasets/AdjustedData'
dest_dir = '/home/raahat/Documents/Signet/Datasets/Data_for_1'
os.mkdir(dest_dir)

# Creating Directories
train_dir = os.path.join(dest_dir, 'TrainDir')
os.mkdir(train_dir)
f1_dir = os.path.join(train_dir, 'Forged')
os.mkdir(f1_dir)
g1_dir = os.path.join(train_dir, 'Genuine')
os.mkdir(g1_dir)

val_dir = os.path.join(dest_dir, 'ValDir')
os.mkdir(val_dir)
f2_dir = os.path.join(val_dir, 'Forged')
os.mkdir(f2_dir)
g2_dir = os.path.join(val_dir, 'Genuine')
os.mkdir(g2_dir)

test_dir = os.path.join(dest_dir, 'TestDir')
os.mkdir(test_dir)
f3_dir = os.path.join(test_dir, 'Forged')
os.mkdir(f3_dir)
g3_dir = os.path.join(test_dir, 'Genuine')
os.mkdir(g3_dir)

# Copying Forged files into training, val and test sets
cur_dir = os.path.join(source_dir, 'Forged')
flist = os.listdir(cur_dir)
random.shuffle(flist)
num = len(flist)

for i in range(0, int(TRAIN_SIZE * num)):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(f1_dir, ffile)
	shutil.copyfile(src, dest)

for i in range(int(TRAIN_SIZE * num), int((TRAIN_SIZE + VAL_SIZE) * num)):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(f2_dir, ffile)
	shutil.copyfile(src, dest)

for i in range(int((TRAIN_SIZE + VAL_SIZE) * num), num):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(f3_dir, ffile)
	shutil.copyfile(src, dest)

# Copying genuine files into training, val and test sets
cur_dir = os.path.join(source_dir, 'Genuine')
flist = os.listdir(cur_dir)
random.shuffle(flist)
num = len(flist)

for i in range(0, int(TRAIN_SIZE * num)):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(g1_dir, ffile)
	shutil.copyfile(src, dest)

for i in range(int(TRAIN_SIZE * num), int((TRAIN_SIZE + VAL_SIZE) * num)):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(g2_dir, ffile)
	shutil.copyfile(src, dest)

for i in range(int((TRAIN_SIZE + VAL_SIZE) * num), num):
	ffile = flist[i]
	src = os.path.join(cur_dir, ffile)
	dest = os.path.join(g3_dir, ffile)
	shutil.copyfile(src, dest)
	
print('Done')
