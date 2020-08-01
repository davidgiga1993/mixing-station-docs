## What is a layer?
A layer defines what channels should be shown in the mixer.
You can creates an unlimited number of layers and 
each layer can contain up to 32 channels in a user definable order.

## Layer settings
This view lets you configure all layers

Open from the mixer view:
```
Menu -> Setup (gear icon) -> Layers
```

![Overview](img/layers-overview.png)


### Channels per layer
Selects the number of channels that should be shown in the mixer.
This also defines the width of the channel strip shown in the mixer. The more channels you show, the smaller each channel gets.

When you change this number the app can automatically resize each layer to contain the selected number of channels.
It will automatically take different channel types into account so you will always end up with a logical layer setup.

#### Auto
If you select `Auto` instead of a number the app will always show all channels assigned to a layer. If required the channel strips will be resized so they fit on the screen

### Layer list
The list in the bottom of the screenshot shows all layers.

- **Drag left bars** Reorder the layer item
- **Press and hold item** Opens a context menu for editing / deleting


## Add new layer
By pressing the `+` menu item you can add a new layer to the list. It will be appended to the bottom.

## Reset
Press the back arrow in the top right to reset all layers. This will take the currently selected `Channels per layer` into account.

## Editing a layer
A layer can be edited by selecting `Edit` from the context menu or by **Press and hold** a layer button directly from the mixer view.

Use the `+` button to add more channels / [IDCAs](layer-idcas.md) to the layer.

![Edit channel order](gif/layer-channel-drag.gif)