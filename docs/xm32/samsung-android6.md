# Samsung and Android 6
Since the rollout of the Android 6 update the sync mechanism does not work anymore.
It just stops a random positions and won't connect at all.

## Root cause
Samsung broke something in their wifi driver / network stack which causes packet and connection losses.
Especially with udp packages. As this is a system component, I can't do anything about it.
The network just stops working after some packets.

## How to fix it?
As this issue is on a much lower level than the app itself there is sadly nothing that can be done from my side to fix this issue.
In some countries and for some devices there is already a second update from Samsung available which fixes this issue.

The following countries are fixed (to my knowledge):

- Germany
- Croatia
- Some US devices (non branded)

Please note that branded devices make take longer to receive the update.
The following kernel versions are reported as working:

- 3.10.61-7884513 (S6)
- 3.10.61-7497559 (S6)

# Workaround
This will make the app connect but it will be out of sync with the mixer.
The sync can be disabled by the following steps: 
```
Open the app->Setup->Skip Sync
```