# Waves SuperRack

This integration allows Waves SuperRack to follow the selected
channel in Mixing Station, as well as recall matching snapshots

## Requirements

- Mixing Station >=3.2.0
- Waves SuperRack
- IPv6 network (link local only)
- Mixing Station SuperRack license or subscription (can be tested without)

Mixing Station and Waves SuperRack must be running
on devices which have IPv6 enabled.
This is required by the ProLink protocol.

## Setup

1. In Mixing Stations main menu press `SuperRack`
   and press the On/Off button to enable the integration.

   ![Setup](setup.png)

2. In SuperRack go to Setup
3. Add a new Controller "Pro Link Console Remote"
4. Press the gear icon to open the ProLink configuration.
   You should see a "Mixing Station" entry. Press "Assign" on the left side.
   ![ProLink](prolink.png)
5. Mixing Station should now show "SuperRack connected".

## Open Racks

This option opens a rack in SuperRack whenever the channel
selection in Mixing Station changes.

In the selection grid you can select
which mixer channel corresponds to which
rack.

## Recall Snapshot

When enabled a SuperRack snapshot will be recalled
every time the "current scene" value changes (aka you recall a scene on your desk).

In addition, the currently selected scene will be highlighted in SuperRack as well.

The mapping for this is always 1:1, meaning when you recall
Scene 5, it will also recall Snapshot 5 in SuperRack.
