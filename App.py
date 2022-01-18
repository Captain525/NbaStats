import tkinter
import cv2
from VideoCapture import MyVideoCapture
import PIL.Image, PIL.ImageTk
import time
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        self.vid = MyVideoCapture(video_source)
        #create canvas to fit vid source size.
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        #after calling update once, it calls itself every delay seconds.
        self.delay = 1
        self.update()

        self.window.mainloop()
    def update(self):
        #get a frame from video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)
    def snapshot(self):
        ret,frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
App(tkinter.Tk(), "Tkinter and OpenCV","https://videos.nba.com/nba/pbp/media/2015/11/23/0021500204/165/471afc6f-cb9f-3ef4-0cd0-a191b5507e9a_1280x720.mp4")