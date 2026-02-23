# iOS

For iOS, only one app is distributed. This app can control all mixers and is only available as a "pro" version.
You can use all features of the app in the offline mode for free.
As soon as you want to connect to a mixer you must buy the app for that mixer model.

## Requirements

- iOS >= 16 (older versions may work, but I can't support them in case of issues)
- iPhone, iPad

## URL Scheme

The URL scheme of the app is `mixingstation`. This name can be used for other apps such as `BandHelper` in order to open
Mixing Station.

## MDM
For mass license or MDM managed devices, please contact support and include your Apple Business/School manager Name and ID.

Also make sure to enable `Custom Apps` in Apple School Manager Organisation Settings.
Take a look at the [apple documentation](https://support.apple.com/guide/apple-school-manager/learn-about-custom-apps-axm58ba3112a/web) for
more details.


## Known limitations

When turning the screen off iOS will terminate any network connections. Therefore, the app will lose any connections and
you must reconnect.
It's recommended to keep the screen on. By default, Mixing Station keeps the screen on, so it will not turn off
automatically.

## License changes (2.8.0)

In the past on iOS the license handling was done using the official Apple libraries.
This has been changed in Mixing Station 2.8.0 due to more and more users reporting the license dissapearing when 
the device has no internet connection for a longer period of time.

This change has the following implications:

- The same device limit used on Android and Desktop applies to iOS now (see [license overview](../license/overview.md)).
- You can now import the license on any iOS devices regardless of their Apple ID.
- You can purchase additional licenses on the [Mixing Station website](https://mixingstation.app).

To migrate the licenses into your mixing station account, simply follow the "Restore" procedure described on the [license overview](../license/overview.md) page.

If you were using the iOS license on more than 4 devices please migrate your license and then contact support at support@mixingstation.app

## License Lost (2.3.3)

If you've updated to 2.3.3 the app may have lost your license. To resolve this issue:

1. Connect to the internet
2. Make sure you're on version 2.3.4
3. Press the gear icon -> Licenses
4. Press `Restore` the top menu
5. Select `Apple ID`

This should now fully restore all licenses. The licenses will be available without internet, indefinitely.

There might still be a `Loading licenses...` message, you can however ignore it for now.
This message will be fixed in 2.4.0