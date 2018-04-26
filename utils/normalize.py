# -*- coding: utf-8 -*-
import numpy as np
import os
import PIL.Image as image

def normalize(v):
    norm = np.linalg.norm(v)
    return v if norm == 0.0 else v / norm

def normalize_image(fname):
    # [0, 255]^3
    img_in  = np.array(image.open(fname).convert('RGB'))
    img_out = np.zeros_like(img_in)
    # [0.0, 1.0]^3
    img_in  = img_in.astype(np.float64) / 255.0
    # [-1.0, 1.0]x[-1.0, 1.0]x[0.0, 1.0]
    img_in[:,:,:2] = 2.0 * img_in[:,:,:2] - 1.0

    height, width, _ = img_in.shape
    for i in range(0,height):
        for j in range(0,width):
            # [-1.0, 1.0]x[-1.0, 1.0]x[0.0, 1.0]
            v = np.float64(normalize(img_in[i,j]))
            # [0.0, 1.0]^3
            v[:2] = 0.5 * v[:2] + 0.5
            # [0, 255]^3
            img_out[i,j] = np.clip(v * 255.0, 0.0, 255.0)
           
    fname_out = os.path.splitext(fname)[0] + '.png'
    image.fromarray(img_out).save(fname_out)
    
def normalize_directory(directory):
    for dir_path, dir_names, file_names in os.walk(directory):
        for file_name in file_names:
            fname = dir_path + '/' + file_name
            print(fname)
            normalize_image(fname=fname)