# Channel move
The channel move feature allows you to move a channel to another position.
Since this process requires a channel preset it's only available when connected to the mixer.

## How to use
1. Select the channel you want to move by pressing its channel button.
2. Press the folder icon in the top menu bar -> Select `Move`
3. Select the position where you want the channel to be moved to. The `[INS]` label represents the position where the channel will be after moving it.
4. Press `Move`

![channel move popup](/img/xm32/channel-move.png)

**Important notice:**
All channels between start and destination position will be muted to avoid possible feedback while the channels are moved.
The source channel will be stored in channel preset slot 100.
Make sure you've got a good network connection!

## Signal source
The signal source of a channel is fixed to its position. Due to the nature of how the move process works the routing will stay fixed at the physical channel.

Before moving

| Channel | Source |
| -- | -- |
| Ch 01 | 01 |
| Ch 02 | 02 |
| Ch 03 | 03 |
| Ch 04 | 04 |
| Ch 05 | 05 |

After moving `Ch 05` to `Ch 01`

| Channel | Source |
| -- | -- |
| Ch 05 | 01 |
| Ch 01 | 02 |
| Ch 02 | 03 |
| Ch 03 | 04 |
| Ch 04 | 05 |

## How it works internally
1. Mute all affected channels
2. Save source channel as channel preset 100
3. Copy all channels in between one space to the left/right
4. Load saved preset at destination position
