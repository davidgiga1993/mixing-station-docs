# Bus password protection
It is possible to lock certain buses with a password (Mixing Station only).


## Usage
1. Open the "Security view": `Menu -> Setup -> Security`
2. Enter a password. The password is stored on the X32 and is **NOT** encrypted
3. Select the buses you want to protect. `Main LR` will lock the `No restrictions` mode.
4. Press back to close the view and store the settings on the X32.

When you connect to the X32 and the data sync is completed, a password prompt will be shown if the bus you want to access is protected.

## Supported devices
All devices using Mixing Station. Any other app including the X32-Mix will simply ignore this setting as it is a custom solution.

## Where is the password stored?
The security settings are stored in the `Name` field of the 100th routing preset on the X32. The routing preset itself will not be touched.

## How to reset the password?
Delete the 100th routing preset using any official X32-Edit app.