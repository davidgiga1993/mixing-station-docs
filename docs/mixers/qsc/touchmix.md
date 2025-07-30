# TouchMix Series

There are some limitations for the TouchMix series mixers when using Mixing Station:

### Metering lag

Due to limitations in the firmware the update rate of the metering data in Mixing Station will be
slower than usually. This "lag" is expected and can't be fixed.

A more technical explanation: The mixer only supports sending 26 meters at a time.
Thus Mixing Station needs to request all meters one after another, for example

```text
Mixing Station      TouchMix
Get meter ch1-8 --> 
                <-- Meter 1-8
Get meter ch9-16 -->
                <-- Meter 9-16
```

This multiplexing also needs to be in sequential order as the mixer can't process multiple requests
following each-other.
