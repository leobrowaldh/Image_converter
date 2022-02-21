#!/usr/bin/env python3
"""Converts all images in target folder to desired format, rotating and/or resizing if needed."""

from PIL import Image, UnidentifiedImageError
import os


def converter(infold, outfold, formatout, rot, sze):
    # Iterating through the folder:
    for filename in os.listdir(infold):
        file = os.path.join(infold, filename)
        # Make sure it is a file and not a folder:
        if os.path.isfile(file):
            # Try to open, modify, and save the image file to the desired folder
            try:
                im = Image.open(file)
                print("im data: " + str(im.getdata()))
                # Rotating, resizing:
                new_im = im.rotate(rot).resize(sze).convert('RGBA')
                print("new_im data: " + str(new_im.getdata()))
                # Changing format:
                # Obtaining the new file name:
                f, e = os.path.splitext(filename)
                outfile = "/" + f + "." + formatout
                # Creating background:
                background = Image.new('RGBA', new_im.size, (60, 60, 60))
                print("background data: " + str(background.getdata()))
                # Joining modified file with background:
                final = Image.alpha_composite(background, new_im).convert("RGB")
                # Saving
                if file != outfile:
                    final.save(outfold + outfile, formatout, quality=80)
            # If it is not a valid image file, continue to next file.
            except UnidentifiedImageError:
                continue


if __name__ == '__main__':
    # The Variables, modify as needed:
    folder_in = "./test"
    folder_out = "./test/destination_folder"
    format_to = "JPEG"
    rotation = 270
    size = 128, 128
    converter(folder_in, folder_out, format_to, rotation, size)
