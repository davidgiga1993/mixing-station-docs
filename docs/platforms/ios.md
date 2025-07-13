# iOS

For iOS, only one app is distributed. This app can control all mixers and is only available as a "pro" version.
You can use all features of the app in the offline mode for free.
As soon as you want to connect to a mixer you must buy the app for that mixer model.

## Requirements

- iOS >= 11
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


## License Lost (2.3.3)

If you've updated to 2.3.3 the app may have lost your license. To resolve this issue:

1) Connect to the internet
2) Make sure you're on version 2.3.4
3) Press the gear icon -> Licenses
4) Press `Restore` the top menu
5) Select `Apple ID`

This should now fully restore all licenses. The licenses will be available without internet, indefinitely.

There might still be a `Loading licenses...` message, you can however ignore it for now.
This message will be fixed in 2.4.0