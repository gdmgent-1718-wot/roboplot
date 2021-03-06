ROBOPLOT
==================================

	roboplot/
	├── docs/
	├── vue/
	├── src/
	│	├── lib/
	│	└── app.py
	└── README.md


## Info

- Contributors: **Lode Muylaert & Jef Roosens**
- Opleidingsonderdeel: **Web Of Things**
- Academiejaar: **2017-2018**
- Opleiding: **Bachelor in de grafische en digitale media**
- Afstudeerrichting: **Multimediaproductie**
- Keuzeoptie: **New Media Development**
- Opleidingsinstelling: **Arteveldehogeschool**

## Promovideo

[![IMAGE ALT TEXT HERE](https://github.com/gdmgent-1718-wot/roboplot/blob/master/docs/video_roboplot.jpg)](https://www.youtube.com/watch?v=e1qKE4O-l1A)

## Hardware

- Raspberry Pi 3
- L293D Quadruple Half-H Drivers
- 9v Battery
- 9v DC motors
- BC547 Transistor
- Small powerbank
- Active 5v buzzer
- Jumpcables
- Leds
- Resistors

## Technische Tekening

![Robotplot Connections](https://github.com/gdmgent-1718-wot/roboplot/blob/master/docs/Roboplot_Schema.png)

## Deploy

### Clone

```
$ cd ~/Code/
```

```
$ git clone https://github.com/gdmgent-1718-wot/roboplot.git
```

### Install required packages

```
$ sudo apt-get update
```

```
$ sudo apt-get -y install libusb-dev joystick python-pygame
```

### Install Sixpair

```
$ cd ~
```

```
$ wget http://www.pabr.org/sixlinux/sixpair.c
```

```
$ gcc -o sixpair sixpair.c -lusb
```

Reboot your PI

```
$ sudo reboot
```

### Connect PS3 controller

Connect your controller via USB to the PI

Getting the hardware address from your controller

```
$ sudo ~/sixpair
```

Disconnect your controller and try connecting via bleutooth. If the controller asks for a pin. Just leave the field empty. 
(Try this a couple of times if it's not working)


### Test the controller

```
$ jstest /dev/input/js0
```

This script delivers all value's of the buttons. You will see changes when you press a button

## Execute

```
$ cd roboplot/src
```

```
$ python3 app.py
```
