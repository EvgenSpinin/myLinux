#!/usr/bin/python3
"""
This Program is for Voice less video Streaming using UDP protocol 
-------
This is a Client
    - Run Client Code first then Server Code
    - Configure IP and PORT number of your Server
    
Requirements
    - Outside Connection 
    - IP4v needed select unused port number
    - WebCamera needed
"""
import cv2, socket, pickle, os    # Import Modules

# AF_INET refers to the address of family of ip4v
# SOCK_DGRAM means connection oriented UDP protocol
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000) # setSockoptTo open two protocols,SOL_SOCKET: Request applies to socket layer.
serverip="192.168.0.104"       # Server public IP
serverport=5600                # Server Port Number to identify the process that needs to recieve or send packets

cap = cv2.VideoCapture(0)       # Start Streaming video, will return video from your first webcam
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('Src opened, %dx%d @ %d fps' % (w, h, fps))


# In order to iterate over block of code as long as test expression is true
while True:
    ret,photo = cap.read()      # Start Capturing a images/video
    
    #cv2.imshow('my pic', photo) # Show Video/Stream

    #ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),30])  # ret will returns whether connected or not, Encode image from image to Buffer code(like [123,123,432....])
    #x_as_bytes = pickle.dumps(buffer)       # Convert normal buffer Code(like [123,123,432....]) to Byte code(like b"\x00lOCI\xf6\xd4...")
    #s.sendto(x_as_bytes,(serverip , serverport)) # Converted byte code is sending to server(serverip:serverport)
 
    #gst_out = "appsrc ! v4l2h264enc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=5600 sync=false"
    #gst_out = "appsrc ! v4l2h264enc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink sync=false host=192.168.0.104 port=5600"
    gst_out = "appsrc ! autovideoconvert ! v4l2h264enc extra-controls=\"encode,h264_level=10,h264_profile=4,frame_level_rate_control_enable=1,video_bitrate=2000000\" ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.0.104 port=5600 sync=false"
    #gst_out = "appsrc ! decodebin ! videoconvert ! x264enc ! rtph264pay ! udpsink host=192.168.0.104 port=5600 sync=false"

    out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, float(30), (int(w), int(h)))
    #out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, float(24), (640, 480))

    if cv2.waitKey(10) == 13:    # Press Enter then window will close
        break                    
# Destroy all Windows/close
cv2.destroyAllWindows() 
cap.release()