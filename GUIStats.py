import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import time
video_path = "https://videos.nba.com/nba/pbp/media/2021/11/17/0022100218/25/eda3e5a7-eae3-9e8f-5856-90f7d68bcee9_1280x720.mp4"
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    start_time = time.time()

    print(fps)
    sleep_ms = int(np.round((1/fps)*1000))
    print(sleep_ms)
    player = MediaPlayer(video_path)
    while video.isOpened():
        grabbed, frame = video.read()
        if not grabbed:
            print("End of video")
            break
        audio_frame,val = player.get_frame(show=False)
        if val == 'eof':
            break
        cv2.imshow("Video", frame)
        elapsed = (time.time() - start_time)*1000
        play_time = int(video.get(cv2.CAP_PROP_POS_MSEC))
        sleep = max(1,int(play_time-elapsed))
        if cv2.waitKey(sleep) &0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)

