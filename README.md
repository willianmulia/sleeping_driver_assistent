# sleeping_driver_assistent
## Simple and fast Python code that recognizes a sleeping driver by image processing through the MediaPipe python library.

# Principal Features:
## Fast:
Image Processing by Python MediaPipe Library.
## Simple: 
Basic logic is based on Euclidean distance between interesting points on driver face.
## Scale invariant:
Value of thresholding is relative by the relationship of distance of eye points and face's size (vertical head line).
## Beep warning:
This code implements a beep warning by "winsound" Python Library, by the way, it can be change to work with others OS.

## Dependencies:
1. OpenCV - in Prompt Command use: pip install opencv-python
2. MediaPipe - in Propt Command use: pip install mediapipe
