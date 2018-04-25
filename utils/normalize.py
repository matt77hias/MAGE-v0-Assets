# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

def normalize(v):
    norm = np.linalg.norm(v)
    return v if norm == 0.0 else v / norm

def normalize_image(fname):
    # [0, 255]^3
    img_in  = cv2.imread(fname)
    img_out = np.zeros(img_in.shape)
    # [0.0, 1.0]^3
    img_in  = img_in.astype(np.float64) / 255.0
    # [0.0, 1.0]x[-1.0, 1.0]x[-1.0, 1.0] (BGR)
    img_in[:,:,1:] = 2.0 * img_in[:,:,1:] - 1.0

    height, width, _ = img_in.shape
    for i in range(0,height):
        for j in range(0,width):
            # [0.0, 1.0]x[-1.0, 1.0]x[-1.0, 1.0]
            v = np.float64(normalize(img_in[i,j]))
            # [0.0, 1.0]^3
            v[1:] = 0.5 * v[1:] + 0.5
            # [0, 255]^3
            img_out[i,j] = np.clip(v * 255.0, 0.0, 255.0)
            
    cv2.imwrite(fname, img_out)
    
def normalize_directory(directory):
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            fname = dir_path + '/' + file_name
            if fname.endswith('.png'):
                print(fname)
                normalize_image(fname=fname)
