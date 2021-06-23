# Android
For Android one app is distributed. Depending on the mixer model you can connect without purchasing a `pro` license. 
You can use all features of the app in the offline mode for free. As soon as you want to connect to a mixer it's required to buy the app for the mixer model you want to connect to.


## Requirements
- Android >= 4.0.1
- Android emulators will work for Midas/Behringer mixers, but not for A&H mixers
- Chromebooks are not supported (but still might work)

## Settings location
The app does store all settings in the internal storage of the device.

You can access all setting files at `Internal/Android/data/org.devcore.mixingstation/files/MixingStation`


## Migration
In the past Mixing Station was available in multiple versions, one for each supported mixer model.
All these apps have been merged into one app. The old apps won't receive any updates in the near future.

Your existing pro versions will be converted into licenses for the new app.
Here is a step by step guide:

1. [Download the new app](https://play.google.com/store/apps/details?id=org.devcore.mixingstation)
2. Make sure you have installed all the Mixing Station Pro versions that should be migrated
3. Start the new app
4. You will be shown a list with all found existing pro licenses.
   ![Screenshot 1](../img/migration/1.png)
5. All licenses will be associated with an email address.
   Select your google account or enter your email address.
   ![Screenshot 2](../img/migration/2.png)
   ![Screenshot 3](../img/migration/3.png)
6. Done! You can now uninstall all other mixing station apps from your device

### Multiple devices
If you have multiple devices follow the guide above for the first device, then continue here for the other devices:

1.  Create a [mixing station account](https://dev-core.org/mixing-station/profile/create) with the same email address as above
2. Select `Skip`
   ![Screenshot skip](../img/migration/10.png)
3. Open the license page
   ![Screenshot menu](../img/migration/11.png)
4. Select `Restore purchases`
   ![Screenshot license](../img/migration/12.png)

### Settings
Due to more restrictive google play policies the app settings can't be migrated automatically.
To overcome this issue either export/import your settings using the [community feature](https://dev-core.org/ms-docs/settings/overview) or
copy the files manually to the new location:

From `internal storage/MixingStation` to `Internal/Android/data/org.devcore.mixingstation/files/MixingStation`
