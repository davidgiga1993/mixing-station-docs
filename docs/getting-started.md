# Getting started

## Compatible mixers
Please make sure your mixer has the latest compatible firmware

| App | Mixers | Required firmware |
| -- | -- | -- |
| XM32 | Any X32/M32 mixer | V1.15 or newer |
| XAir | Any XAir mixer | V1.12 or newer |
| Qu | Any Qu mixer | V1.90 or newer |
| GLD | Any GLD mixer | V1.61 |


## Offline mode
The offline mode provides access to nearly all app features without
the need of connecting to a mixer.

Some features will not work in this mode:

- Channel link

## Network setup
Please consult the manual of the mixer manufacturer on how to setup your network.
Here is a basic sample configuration:

| Device | IP | Subnet mask | Misc | 
| -- | -- | -- | -- |
| Wifi AP | 192.168.1.1 | 255.255.255.0 | DHCP enabled - Range 192.168.1.20-255 |
| Console | 192.168.1.10 | 255.255.255.0 | - | 
| Android | Assigned by DHCP | - | - |