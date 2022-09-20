
# import required module
import glob
import imageio
# get the path/directory
folder_dir = '/home/user/Desktop/Data/Max Data/ConvertedData/DataAndScreenshots/Screenshots/small gif'
 
# iterate over files in
# that directory
imagesList = []
for images in glob.iglob(f'{folder_dir}/*'):
   
    # check if the image ends with png
    if (images.endswith(".png")):
        imagesList.append(images)
        print(images)
imagesList.sort()

with imageio.get_writer(folder_dir + '/Crystal_GIF.gif', mode='I') as writer:
    for filename in imagesList:
        image = imageio.imread(filename)
        writer.append_data(image)