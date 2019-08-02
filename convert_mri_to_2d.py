#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nii_to_tif

command line executable to convert 3d nifti images to 
individual tiff images along a user-specified axis

call as: python nii_to_tif.py /path/to/nifti /path/to/tif
(append optional arguments to the call as desired)

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)
Adopted by: Julius van Dis (julius.van.dis@flock.community)
"""

import argparse
from glob import glob
import os
import sys
from pathlib import Path
from PIL import Image
import nibabel as nib


def arg_parser():
    parser = argparse.ArgumentParser(description='split 3d image into multiple 2d images')
    parser.add_argument('img_dir', type=str,  
                        help='path to nifti image directory')
    parser.add_argument('out_dir', type=str, 
                        help='path to output the corresponding tif image slices')
    parser.add_argument('-a', '--axis', type=int, default=2, 
                        help='axis of the 3d image array on which to sample the slices')
    parser.add_argument('-p', '--pct-range', nargs=2, type=float, default=(0.2,0.8),
                        help=('range of indices, as a percentage, from which to sample ' 
                              'in each 3d image volume. used to avoid creating blank tif '
                              'images if there is substantial empty space along the ends '
                              'of the chosen axis'))
    parser.add_argument('-r', '--recursive', type=bool, default=False, 
                        help=('whether to process folder recursively, i.e. process subfolders.'
                             'The folder structure will be maintained in the output folder'))
    
    return parser


def split_filename(filepath):
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext


def convert(img_dir, out_dir, axis=2, pct_range = (0.2,0.8), recursive= False):    
    if recursive:
        fns = Path(img_dir).glob('**/*.nii*')  
    else:
        fns = glob(os.path.join(img_dir, '*.nii*'))
        
    for fn in fns:
        fn = str(fn)
        path, base, _ = split_filename(fn)

        img = nib.load(fn).get_data()
        start = int(pct_range[0] * img.shape[axis])
        end = int(pct_range[1] * img.shape[axis]) + 1
        out_path = path.replace(img_dir, out_dir)
        os.makedirs(out_path, exist_ok=True)
        for i in range(start, end):
            I = Image.fromarray(img[i,:,:]) if axis == 0 else \
                Image.fromarray(img[:,i,:]) if axis == 1 else \
                Image.fromarray(img[:,:,i])
            
            
            I.save(os.path.join(out_path, f'{base}_{i}.tif'))
    
    
def main():
    try:
        args = arg_parser().parse_args()
        convert(args.img_dir, args.out_dir, args.axis, args.pct_range)
        return 0
    except Exception as e:
        print(e)
        return 1

    
if __name__ == "__main__":
    sys.exit(main())
