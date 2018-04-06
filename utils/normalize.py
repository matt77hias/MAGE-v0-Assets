# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

def normalize(v):
    norm = np.linalg.norm(v)
    return v if norm == 0 else v / norm

def normalize_image(fname):
    img_in  = cv2.imread(fname)
    img_out = np.zeros(img_in.shape)
    img_in  = img_in.astype(float) / 255.0
    
    height, width, _ = img_in.shape
    for i in range(0,height):
        for j in range(0,width):
            img_out[i,j] = np.clip((normalize(img_in[i,j]) * 255.0), 0.0, 255.0)
            
    cv2.imwrite(fname, img_out)
    
def normalize_directory(directory='C:/Users/Matthias/Desktop/normal'):
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            fname = os.path.join(dir_path, file_name)
            if fname.endswith('.png'):
                print(fname)
                normalize_image(fname=fname)
