# WING
This page is for the specifics of the Behringer WING mixer.

## Connection

The mixer allows up to 16 simultaneous connections.

Make sure the `Remote Lock` setting on the mixer (`Setup -> Remote -> Remote lock`) is disabled for tcp.
Otherwise, the app will be in read-only mode.

## RTA

As with most mixers there is only one {{ abbr('RTA') }} available.

In comparison to the XM32 series, the mixer will always override the RTA source if not locked.
This means that the RTA shown in the app will be different from the actual selected channel.

To properly use the RTA in the app make sure to lock the **console first**!
This behaviour cannot be changed by the app.

## USB Player / Show / Scenes

The current firmware version doesn't support file listing, thus it is currently **not**
possible for me to implement the following features:

- USB Player file selection
- Multitrack file selection
- Showfile selection (scenes in a currently active show can be recalled)
