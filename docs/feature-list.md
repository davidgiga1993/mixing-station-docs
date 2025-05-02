# Versions and features

## App versions

The app is available for three different platforms: **[iOS](platforms/ios.md)**, **[Android](platforms/android.md)** and
**[Desktop](platforms/desktop.md)**(Win,MacOS,Linux).

Since the app store policies are slightly different, each app has different versions on each platform.
Click on the left menu items to open the page for your platform and see further details.

### Licensing

For licensing information, please refer to the [licensing page](license/overview.md).

## Compatible mixers

Please make sure your mixer has the latest compatible firmware.

| Feature name   | Mixers                                           | Required firmware       | Notes                                                    | 
|----------------|--------------------------------------------------|-------------------------|----------------------------------------------------------|
| XM32           | Behringer X32/M32(R)                             | V1.15 or newer          |                                                          |
| XAir           | Behringer XAir or Midas MR                       | V1.12 or newer          |                                                          |
| HD96           | Midas HD96 series                                | V1.24.0 or newer        |                                                          |
| dLive          | A&H dLive                                        | V1.93 or newer          |                                                          | 
| Avantis        | A&H Avantis                                      | V1.12 or newer          |                                                          | 
| GLD            | A&H GLD                                          | V1.61                   |                                                          |
| iLive          | A&H iLive                                        | V1.94                   | Secondary mixracks and surface routing are not supported |
| SQ             | A&H SQ                                           | V1.4.1 or newer         |                                                          |
| Qu             | A&H Qu                                           | V1.90 or newer          |                                                          |
| CQ             | A&H CQ                                           | V1.1 or newer           |                                                          |
| Si             | Soundcraft Si                                    | V1.8 / V1.8 / V1-2      | See [HiQNet guide / limitations](soundcraft/hiqnet.md)   |
| Vi             | Soundcraft Vi ([view details](soundcraft/vi.md)) | Latest                  | See [HiQNet guide / limitations](soundcraft/hiqnet.md)   |
| Ui             | Soundcraft Ui                                    | Latest                  |                                                          |
| Wing           | Behringer Wing (Full, Compact, Rack)             | Any                     |                                                          |
| StudioLive III | PreSonus StudioLive Series 3                     | V2.7.2 or newer         | See [SL3](presonus/sl3.md)                               |
| DL             | Mackie DL32S(E)/DL16S(E)/DL32R/DL1608            | MFV V5.2 (Mandolin 1.6) |                                                          |
| DM3            | Yamaha DM3/DM3S                                  | V1.10 or newer          | See [DM](yamaha/dm3)                                     |
| DM7            | Yamaha DM7/DM7 Compact                           | V1.70 or newer          |                                                          |
| TF             | Yamaha TF                                        | V4.50 or newer          | See [TF](yamaha/tf.md)                                   |
| QSC            | QSC TouchMix 8/16/30                             | Latest                  | See [Limitations](qsc/general)                           |

See [incompatible mixers](incompatible-mixers.md) for a list of mixers
which will never be supported in mixing station.

## Features

This page lists all the special features in the professional version.

| Feature                                                 | Pro | Free | Model                                                        | Platform |
|---------------------------------------------------------|-----|------|--------------------------------------------------------------|----------|
| Channel parameters                                      | X   | X    | Any                                                          | Any      |
| {{ abbr('FX') }} access                                 | X   | X    | Any                                                          | Any      |
| FX Presets                                              | X   |      | Any                                                          | Any      |
| Routing                                                 | X   | X    | Any                                                          | Any      |
| [Layers](layers.md)                                     | X   | X    | Any                                                          | Any      |
| [Fixed layer mix](layers.md)                            | X   |      | Any                                                          | Any      |
| [Unlimited {{ abbr('DCA') }}](layer-idcas.md)           | X   | X    | Any                                                          | Any      |
| [{{ abbr('MCA') }}s](mca.md)                            | X   | X    | Any                                                          | Any      |
| [Channel/DCA Spill](settings/app.md#dca-spill)          | X   |      | Any                                                          | Any      |
| [App-Link](app-link.md)                                 | X   | X    | Any                                                          | Any      |
| [Gain/trim on fader](sends-on-faders.md#gain-on-faders) | X   |      | Any                                                          | Any      |
| {{ abbr('RTA') }}                                       | X   | X    | Any\*                                                        | Any      |
| [Channel links](channel-links.md)                       | X   | X    | Any                                                          | Any      |
| [Channel quick-gang](channel-links.md#quick-gang)       | X   | X    | Any                                                          | Any      |
| Different color schemes                                 | X   |      | Any                                                          | Any      |
| Configurable peak hold an decay time                    | X   |      | Any                                                          | Any      |
| Gain reduction timeline                                 | X   |      | Any                                                          | Any      |
| [Custom channel strip](settings/channel-strip.md)       | X   |      | Any                                                          | Any      |
| Meterbridge                                             | X   |      | Any                                                          | Any      |
| Cross mixer channel presets                             | X   |      | Any                                                          | Any      |
| [Personal mix presets](mix-presets.md)                  | X   |      | Any                                                          | Any      |
| Supports development                                    | X   |      | Any                                                          | Any      |
| [Re-Gain](re-gain.md)                                   | X   |      | Any                                                          | Any      |
| [Custom layouts](custom-layouts.md)                     | X   |      | Any                                                          | Any      |
| [Mix copy](mix-copy.md)                                 | X   |      | Any                                                          | Any      |
| [Midi device support](midi.md)                          | X   |      | Any                                                          | Any      |
| [Channel move](xm32/channel-move.md)                    | X   |      | XM32                                                         | Any      |
| Dashboard view                                          | X   |      | Any                                                          | Any      |
| [Automatic ringing out](feedback-detection.md)          | X   |      | Any*                                                         | Any      |
| Password protection                                     | X   | X    | [XM32](xm32/bus-password.md)/[XAir](xair/bus-password.md)/Qu | Any      |

\* Mixer must have RTA functionality
