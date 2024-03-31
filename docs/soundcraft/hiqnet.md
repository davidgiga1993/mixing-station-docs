# HiQNet Guide

Soundcraft mixers use HiQNet for remote control apps. This protocol has certain limitations which may prevent the app
from working correctly.

## Limitations

The Soundcraft Vi and Si series mixer does not allow remote control of all parameters via a network.
Mixing Station currently implements nearly all parameters which can be remote controlled.

## Network Requirements

- All devices must be in the same subnet
- Broadcast must be allowed

## Setup

For the basic setup guide see the [getting started page](../getting-started.md).
Additional configuration for the hiqnet addresses (this is a sample configuration and can be adjusted if required.)

| Device      | HiQNet address      | Misc                                                                                                   | 
|-------------|---------------------|--------------------------------------------------------------------------------------------------------|
| Console     | Any other than 1337 | Make sure **not** to use any access restrictions on the mixer, or use "All" for the App HiQNet address | 
| Android/iOS | 1337                | Make sure each instance of the app (including ViSi remote) has a different address!                    |

You can also refer to the official [Soundcraft setup guide](https://www.youtube.com/watch?v=P-j-x1BJrx0).

### Without hiqnet access control
This is a sample configuration how to use Mixing Station without hiqnet access control

![No access control](noAccessControl.png)

### With access control
This is a sample configuration how to use Mixing Station with hiqnet access control.
Note the hiqnet address `1337` is the one configured in Mixing Station.
This might be different depending on your configuration.

![With access control](accessControl.png)

## Troubleshooting

### Mixer not connecting

Sometimes the network stack of the mixer crashes - this also happens with the official ipad app and is not related to
Mixing Station.
Only a reboot of the mixer can fix this issue.

1. Make sure you can ping the IP address of the mixer from your mobile device. If this is not possible your network
   configuration is wrong.
2. Make sure to fully close any other HiQNet apps (ViSi Remote) for at least one minute.
   This is required as otherwise the mixer won't connect to any other apps on the same device.
3. If the mixer is detected by the app but the sync doesn't work make sure you've disabled any access restrictions on
   the mixer side.

### Inside knowledge: How a connection is established

HiQNet is special in the way it establishes connections: Instead of the app connecting to a mixer, the mixer connects to
the app. For this to work the app must be able to send broadcast requests to the mixer.
Here is how the connection is established:

1. App sends broadcast request for connection (udp)
2. The mixer connects to the app (tcp)

Note: If the mixer does not respond to the message from step `1.` for whatever reason (e.g. the network of the mixer
crashed internally), you won't be able to connect to the mixer.

During testing this happened randomly with the Si Performer and Expression series but is known to happen with any
Soundcraft mixer.
I cannot change this behaviour since it's a bug in the mixers' firmware.

