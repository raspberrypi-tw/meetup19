# Raspberry Pi User Group Meetup 19th

## Intro
In this meetup, we will introudce the FLIR camera and microscope camera on Pi. Demo code can be found below.
The slide is available on [Raspberry Pi特色相機介紹(熱成像攝影機+微距相機)](https://www.slideshare.net/raspberrypi-tw/raspberry-pi-78846465)

Our environment is Pi 4 + 2020-02-05-raspbian-buster-full.img.

## Required
### Build v4l2loopback virtual device node.
```shell  
# Install Kernel Source and Header
$ sudo apt-get update
$ sudo apt-get install bc libncurses5-dev flex bison libssl-dev
$ sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/bin/rpi-source && sudo chmod +x /usr/bin/rpi-source && /usr/bin/rpi-source -q --tag-update
$ rpi-source

# Install required module
$ sudo pip3 install imutils
```

### Install V4L2 Kernel Module
```shell  
$ cd ~
$ git clone https://github.com/umlaeute/v4l2loopback
$ cd ~/v4l2loopback
$ sudo make
$ sudo make install
$ sudo depmod -a
$ sudo modprobe v4l2loopback
```

### Enable FLIR Camera V4L2
```shell  
$ cd ~
$ git clone https://github.com/groupgets/LeptonModule
$ cd ~/LeptonModule/software/v4l2lepton
$ sed -i -e 's/video1/video0/g' v4l2lepton.cpp
$ make
$ sudo ./v4l2lepton /dev/video0 &
Waiting for sink
done reading, resets: 
```

## FLIR Camera Canny Edge Detection
```shell  
$ cd flir

# FLIR image preview
$ python3 flir_preview.py

# FLIR image to Gray scale image preview
$ python3 canny2.py

# Canny edge detection WITHOUT blur
$ python3 canny3.py

# Canny edge detection with blur
$ python3 canny4.py
```

## FLIR Camera + Raspberry Pi Camera Alpha Blending
```shell  
$ python3 blend.py
```


## USB Microscope

## Required
### Install Python-tesseract
```shell  
$ pip3 install pytesseract
```

### Use [pytesseract](https://pypi.python.org/pypi/pytesseract) to do OCR.
```shell  
$ cd micro
$ python3 ocr_preview.py 0
```

Note:
1. the `0` of `python ocr_preview.py 0` means the 0th video device node, such as `/dev/video0`.
2. When launch the program, press `t` to start Tesseract-OCR for the fixed area.
3. After finish Tesseract-OCR, the result will be shown on the preview window.
4. Press `q` to exit the program.

