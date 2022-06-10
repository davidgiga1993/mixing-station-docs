# Channel Links and Quick Gangs
Channel Links allows you to link the values of multiple channels together.
Quick-Gangs allows you to edit multiple channels relative to each other.

This video gives a quick demonstration about the two features:
<div class="video-wrapper">
  <iframe width="650" height="400" src="https://www.youtube.com/embed/dLx8Jjchq7s" frameborder="0" allowfullscreen></iframe>
</div>

** Warning ** Using channel links on multiple mixing station instances at the same time may cause issues!
It is recommended only to use this feature on one instance.

## Channel Links
Open main menu -> `Channel Links` to open the Channel Links view.

![overview](img/chlinks/overview.png)

#### Menu Items
1. Adds a new link group
2. Enables/Disables all link groups
3. Opens the settings dialog

#### Link table description
This section describes the meaning of the columns of the link table

| Column   | Description                                                       | 
|----------|-------------------------------------------------------------------|
| Name     | Name of the link group                                            |
| Channels | Number of channels included                                       |
| Status   | Shows if the link is currently active                             |
| Startup  | Indicates if this link group will be enabled when opening the app |


All channel links are stored automatically for the current mixer model.
When connecting to a mixer, all links will be disabled by default. This can be changed in the settings.


### Creating links
1. Press the `+` icon to add a new link group
2. Select the channels you want to link
3. Press the `Scope` button to adjust which parameters to link



### Settings
The `Apply after connect` setting defines if the links marked with `Startup: true` should be enabled automatically after 
connecting to a mixer.


## Quick-Gang
This feature allows you to quickly edit multiple channels at the same time.
The difference between quick-gang and channel links is that quick-gang links all parameters relative to each other.

An example use case would be to adjust the gain of all drum channels by a certain amount - for example when the drummer 
suddenly plays louder than during soundcheck.

You can access this feature via the chain icon in the top menu of any channel view

![quick-gang](img/chlinks/quickgang.png)

Simply select the channels you want to gang together and hit `Apply`.
A green icon indicates an active gang: ![active-gang](img/chlinks/activegang.png)

Press the icon again to disable the gang.
