import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [16, 8]
plt.rcParams["figure.autolayout"] = True
plt.rcParams['figure.titlesize'] = 'large'

images = ['Slide1.JPG','Slide2.JPG','Slide3.JPG','Slide4.JPG','Slide5.JPG','Slide6.JPG','Slide7.JPG'
   ,'Slide8.JPG','Slide9.JPG','Slide10.JPG','Slide11.JPG','Slide12.JPG','Slide13.JPG','Slide14.JPG'
   ,'Slide15.JPG','Slide16.JPG','Slide17.JPG','Slide18.JPG','Slide19.JPG','Slide20.JPG','Slide21.JPG'
   ,'Slide22.JPG','Slide23.JPG','Slide24.JPG']


plt.axis('off')
img = None

num = 10
for _ in range(num):
    for f in images:
        im = plt.imread(f)
        if img is None:
            img = plt.imshow(im)
            plt.pause(0.1)
        else:
            img.set_data(im)
            plt.pause(0.1)
            plt.draw()