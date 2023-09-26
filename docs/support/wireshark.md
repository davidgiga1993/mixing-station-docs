# Wireshark

This page describes how to capture the network traffic using wireshark. This should only be done if requested by support for resolving very specific issues.

## Setup
- Install wireshark from [the official page](https://www.wireshark.org/download.html)
   	- Make sure to select `Install Npcap` if not already installed.
      ![setup](0.png)<br>
- Install the editor software of the mixer

## Capture
1. Start wireshark as administrator
2. Double click on your network interface
   ![capture](1.png)
3. Start the editor software of the mixer
4. Connect to the mixer
5. Once the software has been connected to the mixer and synchronized all the data, stop the capture<br>
   ![stop](2.png)<br>
6. Click on `File -> Save as` and save the capture.