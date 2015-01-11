
"""
Shrinks image files to half their size.
"""

from PIL import Image
import os, sys


def shrink(infile, outfile):
    if os.path.exists(outfile):
        raise IOError("ABORTING. File exists: %s" % outfile)
    im = Image.open(infile)
    x = int(im.size[0] / 2)
    y = int(im.size[1] / 2)
    small = im.resize( (x, y) )
    small.save(outfile)
    print (infile, 'resized to', x, '*', y)

def shrink_dir(dirname='.'):
    if not dirname.endswith(os.sep):
        dirname += os.sep
    for filename in os.listdir(dirname):
        if len(filename) > 4:
            suffix = filename[-3:].lower()
            if suffix in ['png', 'jpg']:
                outname = 'small/' + filename
                shrink(dirname + filename, outname)


def run_halfsize():
    if len(sys.argv) == 2:
        shrink_dir(sys.argv[1])
    elif len(sys.argv) == 3:
        shrink(sys.argv[1], sys.argv[2])
    else:
        print("""usage:
    1. Shrink a single image file: halfsize <infile> <outfile>
    2. Shrink all PNG/JPG files in a directory into small/ : halfsize <indir>
    """)


if __name__ == '__main__':
    run_halfsize()