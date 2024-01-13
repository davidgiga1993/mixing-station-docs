# Si Performer / Expression

The performer and expression series has certain limitations when it comes to remote controlling.
Mixing Station currently implements all parameters which can be remote controlled. 
Any other features such as Mutegroups, FX or routing **cannot be implemented**.

The following parameters are **not controllable** via network due to firmware limitations:

- Mutegroups
- FX
- Routing

### Mutegroups
It is not possible to access the mutegroups of the mixer - therefore the mute status might be shown incorrectly in the app. Consider using VCAs instead of mutegroups, since the on/off status of a VCA causes associated channels to mute in the same way as a mutegroup, and the VCA on/off status is controllable from Mixing Station.

## Mixer not connecting
Sometimes the network stack of the mixer crashes - this also happens with the official ipad app and is not related to Mixing Station.
Please read [HiQNet guide](hiqnet.md) for more details.

## Scribble Strip Channel Colors
The Si platform does not support user-configurable channel coloring.  MS allows users in unrestricted mode to edit the Scribble Strip colors, but the color choice ends up just being saved in Mixing Station, and not in the mixer itself. MS does **not** allow users in Personal Mixer (restricted) mode to edit the scribble strip colors; this is for consistency with other platforms where a personal mixer user shouldn't be allowed to alter the scribble strip coloring on the actual console...
