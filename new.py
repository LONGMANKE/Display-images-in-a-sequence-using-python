import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.autolayout"] = True

images = ['Slide1.JPG','Slide2.JPG','Slide3.JPG','Slide4.JPG','Slide5.JPG','Slide6.JPG','Slide7.JPG'
   ,'Slide8.JPG','Slide9.JPG','Slide10.JPG','Slide11.JPG','Slide12.JPG','Slide13.JPG','Slide14.JPG'
   ,'Slide15.JPG','Slide16.JPG','Slide17.JPG','Slide18.JPG','Slide19.JPG','Slide20.JPG','Slide21.JPG'
   ,'Slide22.JPG','Slide23.JPG','Slide24.JPG']

plt.axis('off')
img = None

for f in images:
   im = plt.imread(f)
   if img is None:
      img = plt.imshow(im)
      plt.pause(0.5)
   else:
      img.set_data(im)
   plt.pause(0.5)
   plt.draw()