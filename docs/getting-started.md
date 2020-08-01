# Getting started

See [features](feature-list.md) for compatible mixers.

## Offline mode
The offline mode provides access to nearly all app features without
the need of connecting to a mixer.

Some features will not work in this mode:

- Channel link
- Mutegroups / DCA hardmute
- Presets (if stored on the mixer)

## Network setup
Please consult the manual of the mixer manufacturer on how to setup your network.
Here is a basic sample configuration:

| Device | IP | Subnet mask | Misc | 
| -- | -- | -- | -- |
| Wifi AP | 192.168.1.1 | 255.255.255.0 | DHCP enabled - Range 192.168.1.20-255 |
| Console | 192.168.1.10 | 255.255.255.0 | - | 
| Android | Assigned by DHCP | - | - |

For Soundcraft mixers also take a look at the [HiQNet guide](soundcraft/hiqnet.md)


## First launch

When opening the app you'll see the launcher view.
![Launcher](img/launcher.png)

This view allows you to configure where and how you want to connect to the mixer.

## Mix access
Mix access allows you to restrict access to certain mix buses. 
The user will not be able to change any other mix than the ones selected. This is ideal for personal monitor mixing or dedicated monitor engineers.
It is possible to limit the access to multiple mixes as well.

## Console IP
This field allows entering the console IP address. It's only used the using the `Connect` button.

## App version
In the bottom left of the screen you can see the version of the app

## Menu
The top menu gives you access to the global settings as well as this help page.
