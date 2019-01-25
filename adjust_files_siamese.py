# Python Script to convert the dataset of SigWiComp 2013 into the format required by Siamese Net

''' Final Directory structure:
    Data_for_3
    --> 54 Authors (Author1, Author2, etc)
        --> Genuine (24 sign each)
        --> Forged (~12 sign each)
'''

import os
import shutil

base_dir = '/home/raahat/Documents/Signet/Datasets'
dir1 = os.path.join(base_dir, 'SigWiComp2013', 'TrainDutch', 'SigComp2011', 'Offline')
set1 = os.path.join(dir1, 'Questioned')
set2 = os.path.join(dir1, 'Reference')

new_dir = os.path.join(base_dir, 'Data_for_3')
os.mkdir(new_dir)

authors = os.listdir(set1)
for author in authors:
    os.mkdir(os.path.join(new_dir, author))

    gen = os.path.join(new_dir, author, 'Genuine')
    os.mkdir(gen)

    forg = os.path.join(new_dir, author, 'Forged')
    os.mkdir(forg)

    cur_dir = os.path.join(set1, author)
    for fille in os.listdir(cur_dir):
        src = os.path.join(cur_dir, fille)
        if len(fille) == 10:
            dest = os.path.join(gen, fille)
        else:
            dest = os.path.join(forg, fille)
        shutil.copyfile(src, dest)

    cur_dir2 = os.path.join(set2, author)
    for fille in os.listdir(cur_dir2):
        src = os.path.join(cur_dir2, fille)
        dest = os.path.join(gen, fille)
        shutil.copyfile(src, dest)

print('Done')
