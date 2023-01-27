#https://myrusakov.ru/python-opencv-move-detection.html
import cv2 # импорт модуля cv2
#import telebot
from PIL import Image
import requests
import threading
import time
import json
import argparse
import os
#cv2.VideoCapture("видеофайл.mp4"); вывод кадров из видео файла
cap = cv2.VideoCapture(0); # видео поток с веб камеры
#bot = telebot.TeleBot("1400480972:AAEA9cYMMteTfV1KMJhmK_ntvsfHfS_Q030", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

#img = open('/home/pi/robot-opencv-samples/thresholding/script4robot/test.jpg', 'rb')
#img2 = open('/home/pi/robot-opencv-samples/thresholding/script4robot/test2.jpg', 'rb')
#img3 = open('/home/pi/robot-opencv-samples/thresholding/script4robot/test3.jpg', 'rb')

TOKEN = '1400480972:AAEA9cYMMteTfV1KMJhmK_ntvsfHfS_Q030'
CHAT_ID = '636509633'

url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}'

cap.set(3,1920) # установка размера окна
cap.set(4,1080)

ret, frame1 = cap.read()
ret, frame2 = cap.read()
#===============================================

#@bot.message_handler()
def get_user_text(message):
#	bot.send_message(message.chat.id, "HELLO")
    if message.text == '':
        bot.send_message(message.chat.id, "HELLO")
        print ('ok')

def saveimage():
     #imgs = '/home/pi/robot-opencv-samples/thresholding/script4robot/test3.jpg'
     #imgs = cv2.imread('/home/pi/robot-opencv-samples/thresholding/script4robot/test3.jpg')
     path = '/home/pi/'
     cv2.imwrite(os.path.join(path , 'waka777.jpg'),frame1)
     
     
#============================================

def sendimage():
    img = open('/home/pi/waka777.jpg', 'rb')
    r = requests.get('https://api.telegram.org/bot1400480972:AAEA9cYMMteTfV1KMJhmK_ntvsfHfS_Q030/sendMessage?chat_id=636509633&text=WARNING')
    print(r.url)
    print(requests.get('https://api.telegram.org/bot1400480972:AAEA9cYMMteTfV1KMJhmK_ntvsfHfS_Q030/sendPhoto?chat_id=636509633', files={'photo': img}))
    time.sleep (2);

while cap.isOpened(): # метод isOpened() выводит статус видеопотока
 
  diff = cv2.absdiff(frame1, frame2) # нахождение разницы двух кадров, которая проявляется лишь при изменении одного из них, т.е. с этого момента наша программа реагирует на любое движение.
 
  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # перевод кадров в черно-белую градацию
 
  blur = cv2.GaussianBlur(gray, (5, 5), 0) # фильтрация лишних контуров
 
 #Можно настроит щуствителност, второе знаение
  _, thresh = cv2.threshold(blur, 75, 255, cv2.THRESH_BINARY) # метод для выделения кромки объекта белым цветом
 
  dilated = cv2.dilate(thresh, None, iterations = 3) # данный метод противоположен методу erosion(), т.е. эрозии объекта, и расширяет выделенную на предыдущем этапе область
 
 
  сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # нахождение массива контурных точек
 
   
  for contour in сontours:
    (x, y, w, h) = cv2.boundingRect(contour) # преобразование массива из предыдущего этапа в кортеж из четырех координат
   
    # метод contourArea() по заданным contour точкам, здесь кортежу, вычисляет площадь зафиксированного объекта в каждый момент времени, это можно проверить
    print(cv2.contourArea(contour))
   
    if cv2.contourArea(contour) < 9000: # условие при котором площадь выделенного объекта меньше 700 px POMOGAET PRI NASTROIKE
      continue
    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # получение прямоугольника из точек кортежа
    cv2.putText(frame1, "Status: {}".format("Dvigenie"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA) # вставляем текст

#    imgs777 = cv2.imread (str(cap.read()))
 #   path = '/home/pi/Desktop/robot-opencv-samples/thresholding/script4robot'
  #  cv2.imwrite(os.path.join(path , 'waka777.jpg'),frame1)
     
    saveimage();

    sendimage();
    #cv2.drawContours(frame1, сontours, -1, (0, 255, 0), 2) также можно было просто нарисовать контур объекта
 
  #cv2.imshow("frame1", frame1)
  frame1 = frame2  #
  ret, frame2 = cap.read() #  


#  bot.infinity_polling()

  if cv2.waitKey(40) == 27:
    break
 
 
 

cap.release()
cv2.destroyAllWindows()