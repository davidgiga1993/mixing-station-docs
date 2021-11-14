# Raspberry PI

Mixing Station can be used on Raspberry PI 4.

## Requirements
- arm64 OS (tested with Ubuntu 21.10, but [raspios arm64](https://downloads.raspberrypi.org/raspios_arm64/images/) should also work)
- Java 11 or newer

## Installation
1) Install java:
	```
	apt install openjdk-11-jre
	```

2) Download mixing station. In this case I'm installing it to `~/ms`.
	```
	mkdir ms
	cd ms
	wget https://mixingstation.app/backend/api/web/download/update/mixing-station-pc/release
	unzip release
	rm release
	```

3) Start the app
	```
	java -jar mixing-station-pc.jar
	```