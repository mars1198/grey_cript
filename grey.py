from skimage import io, color
import os
import imghdr

source = r'images/Ginia munda munda'
destination = r'greyscale/Ginia munda munda'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Ginia sublitoralis'
destination = r'greyscale/Ginia sublitoralis'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Macedopyrgula pavlovici'
destination = r'greyscale/Macedopyrgula pavlovici'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Macedopyrgula wagneri'
destination = r'greyscale/Macedopyrgula wagneri'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Ohridopyrgula charensis'
destination = r'greyscale/Ohridopyrgula charensis'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Ohridopyrgula macedonica'
destination = r'greyscale/Ohridopyrgula macedonica'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)


source = r'images/Ohridopyrgula svnaum'
destination = r'greyscale/Ohridopyrgula svnaum'

image_files = [os.path.join(root, filename) 
                   for root, dirs, files in os.walk(source) 
                   for filename in files 
                   if imghdr.what(os.path.join(root, filename))]

for fn in image_files:
    rgb = io.imread(fn)
    grey = color.rgb2gray(rgb)
    head, tail = os.path.split(fn)
    io.imsave(os.path.join(destination, tail), grey)

