# PreSonus StudioLive Series 3

## Metering

When comparing the metering scale of mixing station with the UC app, you'll notice that
the metering in Mixing Station is usually higher. This is for multiple reasons:

- As with every mixer Mixing Station uses the start of yellow as +4dBU reference point, the StudioLive mixers
  have less headroom at the reference point compared to other mixer.
- In UC the scale places +4dbU at the lower half. So everything above the lower half in UC control is already above the
  reference level.
- Mixing Station shows the metering quicker than Universal Control does. Thus, you may not see the clipping in
  UC, but in mixing station.
 
Here is some video to show the metering differences:

![type:video](metering.mp4)


## Limitations

### Networking

The mixer must be in the same subnet as the remote control device. Otherwise, metering might not work correctly.

### Mutegroup assignment

Due to the way the Mutegroup assignment works, it is not possible to assign a single channel via network.
Only all currently muted channels can be "stored" as a mutegroup. Thus, this functionality is not available
in mixing station until a good alternative solution is found.

### Search on desktop systems

On desktop systems which also have UC installed the search may not work due to UC blocking the search port.
Either enter the IP address of the mixer manually, or fully close the UC service.