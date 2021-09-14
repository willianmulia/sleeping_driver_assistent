# sleeping_driver_assistent
## Simple and fast Python code that recognizes a sleeping driver by image processing through the MediaPipe python library.

# Principal Features:
## Real-time recognition:
With a camera, it implements frame-by-frame image processing.
## Fast:
Image Processing by Python MediaPipe Library.
## Simple: 
The basic logic is based on the Euclidean distance between the points of interest on the driver's face.
## Scale invariant:
The threshold value is relative by the relationship between the distance of the eye points and the length of nose (vertical line).
## Beep warning:
This code implements a beep warning by "winsound" Python Library, by the way, it can be changed to work with other OS.

# Dependencies:
##   OpenCV
pip install opencv-python
##   MediaPipe: 
pip install mediapipe
