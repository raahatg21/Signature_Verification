# Python Script to convert SigWiComp 2013 Dataset into just two classes: Genuine and Forgery

import os
import shutil

base_dir = '/home/raahat/Documents/Signet/Datasets'
set1 = os.path.join(base_dir, 'SigWiComp2013/TrainDutch/SigComp2009')
set2 = os.path.join(base_dir, 'SigWiComp2013/TrainDutch/SigComp2011')

new_dir = os.path.join(base_dir, 'AdjustedData')
os.mkdir(new_dir)

new_gen = os.path.join(new_dir, 'Genuine')
os.mkdir(new_gen)

new_for = os.path.join(new_dir, 'Forged')
os.mkdir(new_for)

gen1 = os.path.join(set1, 'Offline/Genuine')
for i in range(1, 13):
	cur_dir = os.path.join(gen1, str(i))
	for fille in os.listdir(cur_dir):  
		src = os.path.join(cur_dir, fille)
		dest = os.path.join(new_gen, fille)
		if os.path.isfile(src):
			shutil.copyfile(src, dest)

for1 = os.path.join(set1, 'Offline/Forged')
for i in range(1, 13):
	cur_dir = os.path.join(for1, str(i))
	for fille in os.listdir(cur_dir):  
		src = os.path.join(cur_dir, fille)
		dest = os.path.join(new_for, fille)
		if os.path.isfile(src):
			shutil.copyfile(src, dest)

dir2 = os.path.join(set2, 'Offline/Questioned')
for i in range(1, 70):
	i_ = '0' + str(i)
	cur_dir = os.path.join(dir2, i_)
	if os.path.isdir(cur_dir):
		for fille in os.listdir(cur_dir):
			scr = os.path.join(cur_dir, fille)
			if len(fille) == 10:
				dest = os.path.join(new_gen, fille)
			else:
				dest = os.path.join(new_for, fille)
			shutil.copyfile(scr, dest)

dir3 = os.path.join(set2, 'Offline/Reference')
for i in range(1, 70):
	i_ = '0' + str(i)
	cur_dir = os.path.join(dir3, i_)
	if os.path.isdir(cur_dir):
		for fille in os.listdir(cur_dir):
			scr = os.path.join(cur_dir, fille)
			dest = os.path.join(new_gen, fille)
			shutil.copyfile(scr, dest)

print('Done')
