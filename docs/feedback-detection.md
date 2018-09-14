# Automatic ringing out

The feedback detection view allows you to eliminate feedback while ringing out monitors.
This feature was **not** designed to be used as a feedback destroyer **while music is playing**!

The feature can be accessed from the main mixer:
```
Menu -> Fbk Detection
```

## UI Elements
- RTA Source: Selects the signal source which should be used for showing the RTA and detecting the feedback.
- Target: Select the channel of which GEQ should be used to eliminate the feedback.
- Auto: This button activates automatic GEQ mode. It will reduce the gain of the frequencies which are creating a feedback.
- Yellow RTA lines: These lines indicate which frequencies are detected as feedback. The higher the line, the more the app is confident that this frequency is a feedback.

## Example
Here is an example on how to ring out a monitor with the feedback detection view.

Requirements: a monitor and a microphone.

1. Send the signal of the microphone to the monitor
2. Insert a GEQ in the bus for the monitor
3. Open the feedback detection view and select the microphone as RTA source
4. Select the Bus as target
5. Press the auto button
6. Create a feedback by holding the mic close to the monitor or increasing its gain

The app should now remove the frequencies that are creating the feedback.
Make sure you stop the "auto" mode when the desired goal was reached.
Auto mode will be stopped automatically when leaving the view.