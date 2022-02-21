#!/usr/bin/env python3
"""Converts all images in target folder to desired format, rotating and/or resizing if needed."""

from PIL import Image, UnidentifiedImageError
import os


def converter(input):
    # Iterating through the folder:
    for filename in os.listdir(input):
        file = os.path.join(input, filename)
        # Make sure it is a file and not a folder:
        if os.path.isfile(file):
            # Try to open, modify, and save the image file to the desired folder
            try:
                im = Image.open(file)
                new_im = im.rotate(270).resize((128,128))
                # Changing format:
                f, e = os.path.splitext(filename)
                outfile = "/" + f + "." + format_to
                if file != outfile:
                    new_im.convert('RGB').save(folder_out + outfile)
            # If it is not a valid image file, continue to next file.
            except UnidentifiedImageError:
                continue

if __name__ == '__main__':
    # The Variables, modify as needed:
    folder_in = "./test"
    folder_out = "./test/destination_folder"
    format_to = "jpeg"
    rotation = "90"
    size = "128x128"
    converter(folder_in)