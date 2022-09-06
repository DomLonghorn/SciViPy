
# import required module
import glob
import imageio
# get the path/directory
folder_dir = '/home/user/Desktop/States and pngs/GIF PNGS/pngs/Gif 2 pngs'
 
# iterate over files in
# that directory
imagesList = []
for images in glob.iglob(f'{folder_dir}/*'):
   
    # check if the image ends with png
    if (images.endswith(".png")):
        imagesList.append(images)
        print(images)
imagesList.sort()
print(imagesList)
with imageio.get_writer(folder_dir + '/Jorek_GIF.gif', mode='I') as writer:
    for filename in imagesList:
        image = imageio.imread(filename)
        writer.append_data(image)