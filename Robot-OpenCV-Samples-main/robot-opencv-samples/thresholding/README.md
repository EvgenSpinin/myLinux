<h1 align="center">
  <a href="https://youtu.be/grqoGBd1ch0"><img src="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/raw/branch/main/thresholding/img/thr.png" alt="Распознавание по цвету" width="800"></a>
  <br>
	Распознавание цветных объектов
  <br>
</h1>

<p align="center">
  <a href="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/src/branch/main/thresholding/README.md">Русский</a> •
  <a href="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/src/branch/main/thresholding/README-en.md">English(Английский)</a> 
</p>

## Примеры работы
<h1 align="center">
  <img src="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/raw/branch/main/thresholding/img/chs.png" width="800">
  <br>
	Преследование цветных объектов
  <br>
</h1>    

<h1 align="center">
  <img src="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/raw/branch/main/thresholding/img/laser.png" width="800">
  <br>
	Движение по целеуказанию на лазер
  <br>
</h1>

<h1 align="center">
  <img src="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/raw/branch/main/thresholding/img/line.png" width="800">
  <br>
	Движение по линии
  <br>
</h1>

## Тестовая тележка
<h1 align="center">
  <a href=""><img src="https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples/raw/branch/main/thresholding/img/cvbot.png" width="800"></a>
</h1>

Базируется на orange pi zero 512мб и веб-камере. 
Подробнее про сборку и установку софта [тут](https://codeberg.org/TrashRobotics/CVbot)  

## Запуск приложения
Скачиваем репозиторий проекта
```shell
git clone https://codeberg.org/TrashRobotics/Robot-OpenCV-Samples.git
```
и запускаем приложение
```shell
cd Robot-OpenCV-Samples/thresholding/script4robot
python3 app.py -i (ip-адресс orange pi) -p (порт) -s (последовательный порт)
```
Открываем браузер и вводим в нем 
```shell
(ip-адресс orange pi):(порт)
```
Например так:
```shell
192.168.43.56:5000
```     

Подробнее про все остальное смотрите в [видео](https://youtu.be/grqoGBd1ch0)
