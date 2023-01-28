# Automatic ringing out

The feedback detection view allows you to eliminate feedback while ringing out monitors.
This feature was **not** designed to be used as a feedback destroyer **while music is playing**!

The feature can be accessed from the main mixer:
```
Menu -> Fbk Detection
```

## UI Elements
- RTA Source: Select the signal source that should be used for showing the RTA and detecting the feedback.
- Target: Select the channel on which GEQ should be used to eliminate the feedback.
- Auto: This button activates automatic GEQ mode. It reduces the gain of the frequencies which are causing feedback.
- Yellow RTA lines: These lines indicate which frequencies the app infers to be feedback. A higher line indicates greater confidence in the app's evaluation.

## Example
There follow instructions on how to ring out a monitor with the feedback detection view.

Requirements: a monitor and a microphone.

1. Send the signal of the microphone to the monitor
2. Insert a GEQ in the bus for the monitor
3. Open the feedback detection view and select the microphone as RTA source
4. Select the Bus as target
5. Press the auto button
6. Create feedback by holding the mic close to the monitor or increasing its gain

The app should now remove the frequencies that are creating the feedback.
Make sure you stop the "auto" mode when the desired goal is reached.
Auto mode stops automatically when you leave the view.