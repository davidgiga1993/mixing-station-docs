# HiQNet Guide

Soundcraft mixers use HiQNet for remote control apps. This protocol has certain limitations which may prevent the app from working correctly.


## Requirements

- All devices must be in the same subnet
- Broadcast must be enabled

## Connecting a mixer
When connecting the app to a mixer the process works in an reverse order:

1) App sends broadcast request for connection
2) The mixer connects to the app

Note that if the mixer does not respond to the message from step `1)` for whatever reason (e.g. the network of the mixer crashed internaly) you won't be able to connect to the mixer.

During testing this happend randomly with the Si Performer and Expression series but is known to happen to any soundcraft mixer.
I cannot change this behaviour since it's a bug in the mixers firmware.

