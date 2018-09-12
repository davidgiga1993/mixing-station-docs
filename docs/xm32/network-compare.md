# Network traffic: X32-Mix vs Mixing Station

As some user reported a delay and lag with the X32-Mix iPad app I wanted to take a look at the differences in the network communication.
In the following the X32-Mix iPad app is only referred as X32-Mix.

Here are some quick facts about the network protocol the X32 uses. This will be the same for both apps:

- OSC (Open Sound Control) send via UDP
- UDP is not connection based, nor does it guarantee that all packets are delivered.
- OSC data structure: 
	- Path string: This indicated what content is in the package. Example: /ch/01/mix/level
	- Value string: Information about the type and order of the values in the osc message
	- Value(s): Values attached to the osc message. (Numbers, Text, etc.)



## Keeping data in sync
Key functionality of a remote app is to show the current values of the console. To get this functionality the data in the app and the data in the console need to stay in sync.
There are two different methods to get data from the X32:
  - Polling (X32-Mix): The app sends a `/subscribe` command to the X32. The X32 will now send the requested value every 50 ms for the next 10 seconds. The 10 second timeout can be rested by sending the same command again.
  - Events (Mixing Station): The app sends a `/xremote` command to the X32. The X32 will now send all value changes that are occurring in the next 10 seconds.

As you may have noticed the "event" mechanism only sends data when a value changes. This saves a lot of data! This is also the reason why Mixing Station requires a sync when connecting and X32-Mix doesn't as it gets all values that are currently visible send every 50 ms.


## Measurements

| View | X32-Mix iPad receive  | X32-Mix iPad send | Mixing Station receive | Mixing Station send |
| -- | -- | -- | -- | -- |
| Sync | N/A | N/A | ~65 | ~50 |
| Mixer Ch 1-8 |  < 1 | ~44 | < 1 | ~21 |
| Change to Ch9-8 |  ~20 | ~44 | ~5 | ~34 |
| LR PEQ |  < 1 |  ~28 |  < 1 | ~7 |

All values in kByte/s


For better comparison here are some differences about the data requested by the apps:

| Feature | X32-Mix iPad | Mixing Station |
| -- | -- | -- |
| RTA data | No | Yes |
| GR meters in mixer view | No | Yes |



## Why the lag?
You still may wonder "why does the iPad app lag sometimes?"
The data that is shown to you on the screen is not cached inside the app, it's the last data that was received from the X32 via network.
This means, when you drag the fader on the screen with your finger, the fader shown on the screen will only move when the value that is send back from the X32 to X32-Mix was updated. On a regular network this isn't a issue, but we're talking about a Wifi network that has to transfer a lot of small packets in both directions. Depending on the Wifi-Router some packets will get lost and the average latency will increase. Also when you change the view in X32-Mix it has to wait until all required values arrived before it can show any content as the app has no local cache to store old values.


## How does Mixing Station stay in sync?
As you may have noticed, UDP may drop some packages. If a value has been changed (like a mute button) and the packet gets lost and the app will not be notified about the change. To overcome this issue, Mixing Station syncs all required values in the background periodically to overcome this issue.
This also means that if a package gets lost the app might be out of sync for up to 1 minute.