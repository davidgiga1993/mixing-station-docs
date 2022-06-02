# PC
For pc only one app is distributed. This app can control all mixers and is only available as "pro" version.
You can use all features of the app in the offline mode for free.
As soon as you want to connect to a mixer it's required to buy the app for the mixer model you want to connect to.

## Requirements
- Operating system: Windows 10 (x64) or later, OSX 10.9 or later, Linux (arm64, x64)
- Screen: Any screen works - multi screen is only supported if they are the same size.
- Touchscreen: Multitouch is supported on windows 10 - untested on any other OS.

Please make sure the app is working in offline mode before purchasing any licenses!

## Settings locations
All settings and license files are stored in one folder

| OS | Location | 
| --- | --- |
| Windows | `%USERPFORILE%/MixingStation` |
| OSX | `%HOME%/MixingStation` |
| Linux | `%HOME%/MixingStation` |

## Licensing
After purchasing a license you'll receive a download like to a license file. Make sure to keep a backup of your license files in case of data loss!

You can import the license into the app via the license page:
![menu](../img/license/pc-menu.png)
![menu](../img/license/pc-file-import.png)
![menu](../img/license/pc-license-file.png)

## Scaling
Mixing Station tries to honor the scaling option of the OS.
If for whatever reason the UI is too large to too small you can manually adjust the scaling in the global app settings.
See [settings](../settings/global.md) for more details

## Keyboard shortcuts
This section is work in progress.

| Key | Function | View |
| --- | --- | --- |
| Left | Previous channel | Channel view |
| Right | Next channel | Channel view |
| Up | Previous layer | Mixer |
| Down | Next layer | Mixer |


## Program arguments
You can provide additional the following arguments to mixing station.

| Parameter | Description | Purpose |
| --- | --- | --- |
| `-appSeries` | Which mixer series to use (PC/iOS). Same value as the button text in the app | Auto connect |
| `-ip` | IP address of the mixer, remove if you want to start the search instead. | Auto connect |
| `-mixTarget` | Target mix for the access restrictions. See table below | Auto connect |
| `-web` | Port of the webserver (disabled by default) | [API](../integrations/apis.md) |
| `-osc` | Port of the OSC server (disabled by default) | [API](../integrations/apis.md) |

Example
```
mixing-station.exe "-appSeries=X AIR" -ip=192.168.1.1 -mixTarget=-1
```

#### Mix Targets
| Value | Target |
| --- | --- |
| `-1` | No restrictions |
| `0` | Bus 1 / Mix 1 |
| `1` | Bus 2 / Mix 2 |
| ... | ... |


### Auto connect
Since V0.0.8 you can configure mixing station to automatically connect to a mixer on startup. See the example above.



## Known issues
- Intel  HD Graphics 620, Driver 26.20.100.6859 - please downgrade to 22.20.16.4836