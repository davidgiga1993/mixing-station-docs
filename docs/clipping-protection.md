# Clipping Protection

Clipping Protection automatically lowers the gain of a channel if it detected clipping at the input level.

## Theory of operation

Clipping is defined as either:

1. The signal peaked (> -1dBFS) for multiple times in a 500ms segment
2. The signal average is > -4dBFS

If any of those condition match, the signal is detected as clipping and the gain will be adjusted.

If this happens, the gain will be decreased by 2dB until the clipping stopped. If enabled [Re-Gain](re-gain.md) will be used when adjusting gain to
ensure the mix stays the same.

## Usage

Clipping Protection can be enabled

1. Press the `...` menu button in the mixer view
2. Select `Gain Assist`
3. Press `Enable` in the `Clipping Protection` section

This needs to be done every time you connect to the mixer