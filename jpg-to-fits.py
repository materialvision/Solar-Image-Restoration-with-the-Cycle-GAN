import os
from PIL import Image
import numpy as np
from astropy.io import fits
import argparse

def jpg_to_fits(jpg_filename, fits_filename):
    """
    Convert a JPEG image to a FITS file.

    Parameters:
    - jpg_filename: Path to the input JPEG file.
    - fits_filename: Path where the output FITS file will be saved.
    """
    with Image.open(jpg_filename) as img:
        img_gray = img.convert('L')
        img_data = np.array(img_gray)
    
    hdu = fits.PrimaryHDU(img_data)
    hdul = fits.HDUList([hdu])
    hdul.writeto(fits_filename, overwrite=True)

def convert_folder(input_folder, output_folder):
    """
    Convert all JPEG images in the input folder to FITS format and save them in the output folder.

    Parameters:
    - input_folder: Directory containing JPEG files.
    - output_folder: Directory where FITS files will be saved.
    """
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg"):
            jpg_filename = os.path.join(input_folder, filename)
            fits_filename = os.path.join(output_folder, os.path.splitext(filename)[0] + '.fits')
            jpg_to_fits(jpg_filename, fits_filename)
            print(f"Converted {jpg_filename} to {fits_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JPEG images to FITS format.")
    parser.add_argument("input_folder", type=str, help="Input folder containing JPEG images.")
    parser.add_argument("output_folder", type=str, help="Output folder for FITS files.")
    
    args = parser.parse_args()

    convert_folder(args.input_folder, args.output_folder)
