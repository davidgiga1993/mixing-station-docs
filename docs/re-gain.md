# Re-Gain

This feature allows you to change the gain/trim of a channel without affecting the monitor sends / gate / dynamics.

A typical use case would be if an input is suddenly louder than anticipated, and you need to adjust the gain but keep
the
monitor sound stable.

## Theory of operation

Gate and dynamics thresholds will be increased / decreased with the gain value.
Sends / Faders will be adjusted in the inverted direction.

> Re-Gain only works when the gain/trim gets changed form within the app. Any changes made on the mixer side
> are ignored by Re-Gain. This is to prevent a scene-recall from causing unexpected changes being made.

> Re-Gain must be enabled after every reconnect to prevent unexpected changes due to the user forgetting about it being
> enabled.

## Usage

There are two different modes of operation: `Global` or `Temporary usage`

### Global usage

Re-Gain can be enabled globally and will be applied as soon as any gain/trim of an input channel gets changed
inside the app.

1. Press the `...` menu button in the mixer view
2. Select `Gain Assist`
3. Adjust the scope settings to your liking
4. Press `Enable` (You can also use an action to enable/disable Re-Gain)


It is possible to put a single channels into `temporary usage` mode again by following the steps below.


### Temporary usage

This section describes how to use Re-Gain temporarily for a single channel.

1. Open the config page of the relevant channel
2. Press and hold the gain knob (or right-click)
3. Enable "Re Gain" from the top menu
4. Adjust the gain
5. As soon as you close the popup Re-Gain will be disabled again

![Re-Gain popup](img/regain/overview.png)

The red lines in the gain slider indicate the minimum/maximum gain adjustment Re-Gain is able to compensate
without altering the signal relations.
If you exceed the lines some parameters (for example thresholds, send levels, ...) are at their limit, and any 
further gain adjustments will begin to alter the sound of your mix.

You can press the gear icon to change Re-Gain settings.

## Scope
The scope defines which parameters are adjusted by Re-Gain.

![Scopes](img/regain/scopes.png)

| Scope       | Description                                        |
|-------------|----------------------------------------------------|
| Sends       | Adjusts all pre-fader sends > -90dB                |
| Gate        | Adjusts the gate threshold                         | 
| Compressor  | Adjust the compressor threshold                    |
| LR          | Compensates the main fader                         |
| Other mains | Compensates any additional mono/stereo main faders |

## Example

| Value    | Before | After |
|----------|--------|-------|
| Gain     | 0dB    | 5 dB  |
| Gate thr | -20dB  | -15dB |
| Fader    | -15dB  | -20dB |

![Re-Gain example](gif/re-gain.gif)

