# sleeping_driver_assistent
## Simple and fast Python code that recognizes a sleeping driver by image processing through the MediaPipe python library.

# Principal Features:
## Fast:
Image Processing by Python MediaPipe Library.
## Simple: 
The basic logic is based on the Euclidean distance between the points of interest on the driver's face.
## Scale invariant:
The threshold value is relative by the relationship between the distance of the eye points and the size of the face (vertical line of the head).
## Beep warning:
This code implements a beep warning by "winsound" Python Library, by the way, it can be changed to work with other OS.

# Dependencies:
1. OpenCV - in Prompt Command use: 
##   pip install opencv-python
2. MediaPipe - in Propt Command use: 
##   pip install mediapipe
