# Beta program

The beta program allows you to test an upcoming version before anyone else.

## Discussion / Feedback

All discussion about the beta versions and feedback is happening in our [discord channel](https://discord.gg/d8bJPg6kZm)
. Feel free to join us!

## Android

If you want to join the program just follow the
link: [Mixing Station beta](https://play.google.com/apps/testing/org.devcore.mixingstation )

You will receive the beta version as an regular update from the google play store.

If you're still using the old android app, make sure to read the [migration guide](../platforms/android/#migration)

To leave the beta group, just delete and reinstall the app from your device.

## iOS

Open this link on your iOS device and follow the instructions:

- [Test Flight](https://testflight.apple.com/join/lsd9mugy)

Note: Beta builds are only available for 90 days. In that time, all in app payment features can be **tested for free!**
The beta testers are limited to 750 accounts so if there are no slots left you can't join the beta program.

## PC

1. Open the app
2. Click the gear icon
3. Select `Beta` as update branch
4. Restart app

## Mixer specific beta

This beta only applies to a single mixer series which should be tested.
These tests are required since I don't have access to the hardware and developed the
integration solely based off an emulator.

I'm very thankful for all the feedback I can get for those mixers.

This section will get updated based off the feedback I receive

### A&H Dlive

1. Open secret mode (see below)
2. Enter `dlive` and confirm

Things which should be tested:

| Feature      | Result   | Remark                                                                  |
|--------------|----------|-------------------------------------------------------------------------|
| Metering     | Untested | The metering of the channels should work                                |
| Value update | Untested | The values of the app should update correctly                           | 
| Errors       | Untested | The mixer should not show any errors during the usage of mixing station |

### Soundcraft UI 24

1. Open secret mode (see below)
2. Enter `ui` and confirm

Things which should be tested:

| Feature      | Result   | Remark                                                                           |
|--------------|----------|----------------------------------------------------------------------------------|
| Metering     | Untested | The metering of the channels should work, especially the gain reduction metering |
| Value update | Untested | The values of the app should update correctly                                    | 

#### Known issues

- Search doesn't work
- Channel link may not work
- Features missing

## Secret Mode
The secret mode allows you to access untested features of the app.

You can open it by `double-tapping with two fingers` on the screen after opening the app,
or by pressing `CTRL+D`.
This will open a new dialog where you can enter the code.