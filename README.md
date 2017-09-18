# Robot-Opera
Code for an Arduino Yún-based robotic musical instrument.

## Arduino Yún Setup
Hardware
- Arduino Yún
- Micro SD card (>1 GB)
- Wireless router

Software
- Arduino IDE

default user (Arduino/Linino): root/root
default password (Arduino/Linino): arduino/doghunter


##Enabling extroot
The first step towards installing the necessary packages on the Yún is to enable storage on an external filesystem. Insert the micro SD card into the Yún's card reader slot. 




##SFTP File Transfer
It is possible to view and manage files on the Yún using utilities like *Filezilla* by installing the *openssh-sftp-server* package.
```
opkg update
opkg install openssh-sftp-server
```

##Installing PyOSC


`opkg update`
`opkg install distribute`
`opkg install python-openssl`
`easy_install pip`

```
pip install pyosc
pip install pyserial
pip install pymata
```


##Disabling *Bridge*
The Yún's hardware serial port and system console, */dev/ttyATH0*, is tied to the Atmega32U4's serial port. Output from the console must be disabled to send serial data to the Atmega32U4.

Run `nano /etc/inittab` and comment out the line `ttyATH0::askfirst:/bin/ash --login`.

##Run the Script on Startup





