import cv2
import numpy
import os

def capture(fname, path='', start=0, stop=0, x1=0, x2=None, y1=0, y2=None):
    
    
    
    
    cap = cv2.VideoCapture(os.path.normpath(os.path.join(path, fname)))
    flags =[]
    frames = []
    try:
        n_frames = int(numpy.ceil(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)))
    except:
        n_frames = int(numpy.ceil(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        
    if stop == 0:
        stop = int(numpy.floor(n_frames))
    count = 0
    ret,frame = cap.read()
    if frame.ndim==3:
        frames = numpy.zeros((stop-start, frame[y1:y2,x1:x2].shape[0], frame[y1:y2,x1:x2].shape[1], frame[y1:y2,x1:x2].shape[2]))
    if frame.ndim==2:
        frames = numpy.zeros((stop-start, frame[y1:y2,x1:x2].shape[0], frame[y1:y2,x1:x2].shape[1]))
        
    if start == 0:
        frames[0] = frame[y1:y2,x1:x2]
    count+=1
    
    while count < stop:
        ret,frame = cap.read()
        if count>=start:
            flags.append(ret)
            frames[count-start] = frame[y1:y2,x1:x2]
        count += 1
    cap.release()
    return frames

