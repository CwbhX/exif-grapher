import exif
import matplotlib
import os

from os import listdir
from os.path import isfile, join
from exif import Image
import matplotlib.pyplot as plt


photosdir = '/Users/clement/Desktop/testphotos/'
photosdir2 = '/Users/clement/Dropbox/Editted'

filesAndFolders = os.listdir(photosdir)
onlyFiles = [f for f in listdir(photosdir2) if isfile(join(photosdir2, f))]

print(filesAndFolders[0])
print(len(filesAndFolders))
print(len(onlyFiles))

lenses = {}

for imageName in onlyFiles:
    try:
        with open(photosdir2 + "/" + imageName, 'rb') as image_file:
            loaded_image = Image(image_file)
            if loaded_image.has_exif:
                fl = loaded_image.focal_length
                
                if fl in lenses:
                    lenses[fl] = lenses[fl] + 1
                else:
                    lenses[fl] = 1
    except:
        print('TIFF error or something idgaf')
        
print(lenses)


x_axis = list(lenses.keys())
x_axis_str = list(map(str, x_axis))
y_data = list(lenses.values())

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x_axis_str,y_data)
plt.xlabel("Focal Length")
plt.ylabel("Photos Taken")
plt.show()