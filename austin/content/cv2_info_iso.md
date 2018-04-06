Title: OpenCV2 information isolation part 1
Date: 2017-12-07 20:00
Category: openCV
Status: published

#### Isolating image info using OpenCV2

A colleague of mine was asking if it was possible to isolate certain colors of 
dyed mouse skeletons.

Luckily for me, I had written a helper library to do a similar task in another 
application. With a little modification, I was able to use this tool to save 
lots of time.

##### Script setup and file import

```python
'''
Name: mouse_skeleton.py
By: ADG Dec 07, 2017
Description: Quick script to reduce/isolate information in a dyed mouse skeleton
'''

import cv2
import lab_colors
import sim_image_utils as siu

img = cv2.imread("mouse_images/mouse_skeleton.jpg", 1)
```
The source x-ray image I am using is pretty low quality, and has JPEG artifacts 
all over.  However, it is still a good candidate for color isolation as the 
lighting provides clear separation between color zones.
[(original image source)](https://news.utexas.edu/2013/09/30/science-visualized)
![original image](https://image.ibb.co/iRs6aG/mouse_skeleton.jpg)


#####Removal of Unimportant Information
First thing I want to do is remove whatever useless information I can. The 
white background does not provide any useful information.
```python
# Lets remove the white information from the image
# The JPG artifacts are really messing with the image and it shows here
white_mask = siu.get_color_mask(img, lab_colors.MOUSE_COLORS['wht'])
not_white_mask = cv2.bitwise_not(white_mask)
cv2.imwrite("mouse_images/reduce_white.jpg",not_white_mask)
```
![Removal of white](https://image.ibb.co/no6M9b/reduce_white.jpg)

After this step, the JPEG artifacting is very apparent, one of the first things 
that JPEG compression does is reduction of information in the whites and blacks.

Luckily for us, there is an outline of yellowish membrane (probably muscle and 
skin, I'm certainly no biological expert) surrounding the skeleton. This color
was far enough away from white that the JPEG compression algorithm didn't group
all these pixels into blocks.
```python
# If you look closely near the bones, there is a membrane of yellowish color
# This is probably muscle/skin, lets see if we can isolate and remove it
membrane_mask = siu.get_color_mask(img, lab_colors.MOUSE_COLORS['membrane'])
not_membrane_mask = cv2.bitwise_not(membrane_mask)
cv2.imwrite("mouse_images/reduce_membrane.jpg", not_membrane_mask)
```
![Removal of membrane](https://image.ibb.co/mtFg9b/reduce_membrane.jpg)

That made the difference!  This could be tweaked for better accuracy, but
without a clear goal in mind, it's pointless to lament over detail.

Let's take a look at the original image after masking out the unimportant data.
```python
# Lets just look at the information from the dyed portions of skeleton
isolated_skeleton_img = cv2.bitwise_and(img, img, mask=not_membrane_mask)
cv2.imwrite("mouse_images/iso_skeleton.jpg", isolated_skeleton_img)
```
![Isolated Skeleton](https://image.ibb.co/nOWM9b/iso_skeleton.jpg)

Thats pretty clear. Now we can begin working on isolating the primary colors.
 
#####Color Isolation
The primary colors in this image are magenta, and cyan. It
should be pretty easy to isolate them.

```python
#cycle through the color boundaries (cb's)
for cb in lab_colors.MOUSE_COLORS:
    mask = siu.get_color_mask(isolated_skeleton_img, lab_colors.MOUSE_COLORS[cb])
    color_img = siu.get_colored_img(isolated_skeleton_img,
                                    color_boundary=lab_colors.MOUSE_COLORS[cb],
                                    mask=mask)

    cv2.imwrite("mouse_images/{}_img.jpg".format(cb), color_img)
```
![Cyan](https://image.ibb.co/iOYCFG/cyan_img.jpg)
![Magenta](https://image.ibb.co/c71chw/mgnt_img.jpg)

That's all I got for tonight. A brief look at the source image in comparison to
the color-isolated images shows that my color regions are too broad and should 
probably be defined into more precise categories other than just *Cyan* and *Magenta*.

#####Up Next
Next time I will attempt to do some other cool stuff with this image:

 - Identify centers of mass and coordinates of each region
 - Determine percentages of each color by area 
 - Mark regions with certain color characteristics
 
 I'll do my best to address these things in part 2.





