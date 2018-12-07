#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:27:55 2018

@author: dell
"""

import numpy as np
import nibabel as nib
import os.path


### variables ###

# validation list7 7, 8, 9]

# source folder where the .nii.gz files are located 
source_folder = './data/TrainingData'

#################


# destination folder where the subfolders with npy files will go
destination_folder = 'data3'

# returns the patient number from the filename
def get_patient(s): return int(s.split("-")[-1].split(".")[0])

# create destination folder and possible subfolders
subfolders = ["train", "val"]
if not os.path.isdir(destination_folder):
	os.makedirs(destination_folder)
for name in subfolders:
	if not os.path.isdir(os.path.join(destination_folder, name)):
        	os.makedirs(os.path.join(destination_folder, name))
sub='val'            
for k in range(121,131):            
    print(k)
    name2='segmentation-'+str(k)+'.nii.gz'
    data2 = nib.load(os.path.join(source_folder, name2))# load file
    data3 = nib.load(os.path.join(source_folder, name2))# load file
    data3 = data3.get_data()
    data2 = data2.get_data()# convert to numpy
    
    data2 = (data2>0).astype(np.uint8)
    data2 = np.transpose(data2, (2, 0, 1))
    index=[]
    for j, zz_slice in enumerate(data2):    
        bb=np.where(zz_slice>0)
        if len(bb[0])>0:
            index.append(j)
        
    data3= (data3==2).astype(np.uint8)  
    data3 = np.transpose(data3, (2, 0, 1))   
    data3=data3[index,:,:]
    for i, z_slice in enumerate(data3):
        # save at new location (train or val)
        np.save(os.path.join(destination_folder, sub, name2[:-7] + '_' + str(i)), z_slice)
    
    
    name1='volume-'+str(k)+'.nii.gz'
    data1 = nib.load(os.path.join(source_folder, name1))# load file
    data1 = data1.get_data()
    data1 = np.clip(data1, -200, 200) / 400.0 + 0.5
    data1 = np.transpose(data1, (2, 0, 1))
    data1=data1[index,:,:]
    for i1, z_slice1 in enumerate(data1):
        # save at new location (train or val)
        np.save(os.path.join(destination_folder, sub, name1[:-7] + '_' + str(i1)), z_slice1)
    
'''    
foldername=os.listdir(source_folder)
foldername.sort()
for file_name in os.listdir(source_folder):

    print (file_name)

    # create new file name by stripping .nii.gz and adding .npy
    new_file_name = file_name[:-7]

    # decide whether it will go to the train or val folder
    sub = subfolders[1] if get_patient(file_name) in val_list else subfolders[0]

    
    

    

    # check if it is a volume file and clip and standardize if so
    if file_name[:3] == 'vol': 
        data = np.clip(data, -200, 200) / 400.0 + 0.5

    # check if it is a segmentation file and select only the tumor (2) as positive label
    if file_name[:3] == 'seg': data = (data==2).astype(np.uint8)

    # transpose so the z-axis (slices) are the first dimension
    
    #########################################################################xu

'''
