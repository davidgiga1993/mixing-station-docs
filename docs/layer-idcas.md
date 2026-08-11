# Unlimited DCAs

Mixing Station can create an unlimited number of DCAs, called "IDCA" channels.

It is also possible to select a specific mix the IDCA should affect instead of the main mix.

## New IDCA

You can create new {{ abbr('IDCA') }}s in the layer editor via the top menu (`+` symbol).

IDCAs are globally available, meaning once created, you can add them to multiple layers at the same time.

![type:video](gif/new-idca.mp4)

## IDCA Setup

This view allows you to assign channels to an IDCA.
Select the mix you want the IDCA to control by pressing the button on the right side of
the `Target Mix` label. By default `Main LR` is selected.
Now you can select the channels you want the IDCA to control.

## How it works

The IDCA stores the ratios of the levels of the assigned channels.
When a channel level is changed, the ratio is recalculated.
By changing the IDCA fader, all assigned channel levels will be adjusted according to the stored ratios.

The red line behind the fader knob of an IDCA shows the minimum/maximum levels of the assigned channels.

### Fader mode

The IDCA can be configured with different fader modes:

| Mode                 | Explanation                                                                      |
|----------------------|----------------------------------------------------------------------------------|
| Default              | All member channel faders are moved, keeping their ratio                         |
| Ignore -oo           | Member channels having their fader at the -Inf. position are ignored             |
| Ignore -oo for sends | In SoF mode: Member channels having their send at the -Inf. position are ignored |

## Removing

To remove the IDCA from a layer just drag n drop the item onto the `Remove` field.
If you want to delete the IDCA entirely you can drag and drop the item onto the `Delete` field.