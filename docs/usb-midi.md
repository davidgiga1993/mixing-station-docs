# USB Midi

You can use any generic midi device to remote control the mixer via mixing station.

## Requirements

### Android
- [USB OTG](http://en.wikipedia.org/wiki/USB_On-The-Go) compatible Android device
- [USB OTG cable](https://www.google.com/search?q=USB+OTG+cable) / USB host port
- Mixing Station Pro

#### Known issues
In Android 5.0 (Lollipop) only the last plugged USB device is working correctly. This is a [known bug](https://code.google.com/p/android/issues/detail?id=159897) in Android and cannot be fixed.

### iOS
- Not supported yet


## Overview
A midi device will be represented in the app as one or more input / output devices.
In the app you define `faders`, `buttons` and `knobs` which then use one of those input/output devices.

- Midi controller (fader, button, ..)
	- Use one midi input and output device assigned
	- Have one or more actions assigned which define what should be controlled

Make sure you're selecting the correct controller type:

- Button: Midi device sends a value when pressed and/or released
- Fader: Midi device sends an absolute value when fader/knob is moved (e.g. `0-127`)
- Knob: Midi device sends a fixed value for each increment / decrement (e.g. `24` and `27`)

## Midi Setup
The midi overview can be opened from the mixer via the menu:
```
Menu -> Setup -> Midi
```
You can add / edit midi controllers from here.

### Add a new controller
1. Press the `+` item in the menu to add a new controller.
2. Select the controller

### Configure a controller
The edit controller view allows you to change the properties of the controller:

- Unique name: Name which will be shown in the controller overview
- Input/Output: Selects which USB device should be used for Midi communication

#### Output Modes
The output mode configures when the value should be send back to the midi device.

| Mode | Description |
| -- | -- |
| On value change | Sends midi value when the action value has been changed without a midi input |
| On midi event+change | Sends a midi event when a midi event was received or the action value has been changed |
| On note up+change | Sends a midi event when a "note up" command was received or the action value has been changed |
