# Getting started

When opening the app you'll see the mixer selection screen:

![Mixer selection](../img/mixer-selection.png)

On this screen you can select to which mixer you want to connect to.

By pressing the `Add Mixer` button you can add a new entry.

## Mixer entry

When adding a new mixer (or when pressing the gear icon on an existing entry) you see the connection settings entry:

![settings](../img/mixer-connection-settings.png)

This dialogue allows you to configure the access mode and connection settings

### Access Mode

The access mode defines which parameters are accessible to the user.
Use `Personal Monitoring` if you want to control your own monitor (IEM/Wedge).

### Network setup

Please consult the manual of the mixer manufacturer on how to set up your network.
Here is a basic sample configuration:

| Device  | IP               | Subnet mask   | Misc                                  | 
|---------|------------------|---------------|---------------------------------------|
| WiFi AP | 192.168.1.1      | 255.255.255.0 | DHCP enabled - Range 192.168.1.20-255 |
| Console | 192.168.1.10     | 255.255.255.0 | -                                     | 
| Android | Assigned by DHCP | -             | -                                     |

For Soundcraft mixers also take a look at the [HiQNet guide](soundcraft/hiqnet.md)

### iOS privacy settings

Starting with iOS 14 you need to explicitly allow the app to communicate with your local network.
iOS asks for your permission once you try to connect to a mixer for the first time.
You can check the settings in iOS: `Settings > Privacy > Local Network`

## Offline mode

The offline mode provides access to nearly all app features without
needing to connect to a mixer. However, some features that will not work in offline mode including:

- Channel link
- Mutegroups / DCA hardmute
- Scenes / Presets (if stored on the mixer)

## Favorites

<div style="float:left;margin:0 10px 10px 0" markdown="1">
![Favorite mixer](img/favorite-mixer.png)
</div>

You can pin connections by pressing the `star` or `mixer icon`:
Pinned entries will always appear at the top of the list
and won't get removed over time.
<div style="clear: both;"></div>
