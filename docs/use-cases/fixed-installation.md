# Fixed Installation

Mixing Station is perfect for fixed-installation tablets to control conference rooms or similar.

This guide explains what settings should be set to ensure a smooth client experience, and prevent 
changes by the client.

## Layout

1. First create a new [layout](../custom-layouts.md)
2. Change the `behavior` to `Open on start` - this will now be your main layout that gets opened by default
3. Enable `Password on exit` to ensure the client can't leave this layout without a password


## Settings

1. Make sure to [save your settings](../settings/user.md) as `default` so they get recalled when opening the app
2. Disable autosave - This is recommended so the app won't save any changes made by the client

## Autostart


1. To ensure the app directly connects with your mixer when being launched open the [global settings](../settings/global.md)
2. Enable Autostart and enter the IP address of the mixer

Note that autostart will only work after fully closing the app.