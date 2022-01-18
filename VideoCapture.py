import cv2
import tkinter
class MyVideoCapture:
    def __init__(self, video_source=0):
        #open video source.
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("unable to open video source")
        #get video source width and height.
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #release video when object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
            if self.vid.isOpened():
                ret,frame = self.vid.read()
                if ret:
                    #return boolean success flag and current frame in BGR
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    return (ret,None)