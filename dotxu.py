#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:38:18 2018

@author: dell
"""

import numpy as np
import nibabel as nib
import os
file_dir1="/home/bme/文档/research/xu/fei/liver/TestData"
file_dir="/home/bme/文档/research/xu/fei/liver/result-liver"

file_dir3="/home/bme/文档/research/xu/fei/liver/test-tumor"

for i in range(70):
    print(i)
    
    
    '''
    name1='test-volume-'+str(i)+'.nii.gz'
    data=nib.load(os.path.join(file_dir1,name1))
    
    input_aff = data.affine
    data=data.get_data()
    data = np.transpose(data, (2, 0, 1))
    name2='test-segmentation-'+str(i)+'.nii'
    data2=nib.load(os.path.join(file_dir,name2))
    data2=data2.get_data()
    #data3=data*data1
    data2 = np.transpose(data2, (2, 0, 1))
    index=[]
    #index1=[]
    for j, z_slice in enumerate(data2):    
        bb=np.where(z_slice==0)
    #    index1.append(j)
        if len(bb[0])==262144:
            index.append(j)
    data[index,:,:]=0
    data = np.transpose(data, (1, 2, 0))
    new_file_name = "test-volume-"+str(i)+'.nii'
    data = nib.Nifti1Image(data, affine=input_aff)	
    nib.save(data, os.path.join(file_dir3, new_file_name))
    '''
    name1='test-volume-'+str(i)+'.nii.gz'
    data=nib.load(os.path.join(file_dir1,name1))
    
    input_aff = data.affine
    data=data.get_data()
    #data = np.transpose(data, (2, 0, 1))
    name2='test-segmentation-'+str(i)+'.nii'
    data2=nib.load(os.path.join(file_dir,name2))
    data2=data2.get_data()
    data3=data*data2
    new_file_name = "test-volume-"+str(i)+'.nii'
    data3 = nib.Nifti1Image(data3, affine=input_aff)	
    nib.save(data3, os.path.join(file_dir3, new_file_name))


    
