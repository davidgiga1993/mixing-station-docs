# Unlimited DCAs
Mixing Station can created an unlimited number of DCA channels, called IDCA.

It is also possible to create an IDCA which changes the send level of multiple channels instead of the LR mix.


# New IDCA
To add a new IDCA to a layer, open the `Layer Setup` view.
Press the `+` symbol in the menu and select `IDCA`
This will open the `IDCA Setup` view.

![New IDCA](gif/new-idca.gif)

# IDCA Setup
This view allows you to assign channels to an IDCA.
Select the mix you want to control with this IDCA by pressing the button on the right side of 
the `Target Mix` label. By default `Main LR` is selected.
Now you can select the channels you want to control with this IDCA.

# How it works
The IDCA stores the ratios of the levels of the assigned channels.
When a channel level gets changed, the ratio will be recalculated.
By changing the IDCA fader, all assigned channel levels will be adjusted accordingly to the stored ratios.

The red line behind the fader knob of an IDCA shows the minimum/maximum levels of the assigned channels.