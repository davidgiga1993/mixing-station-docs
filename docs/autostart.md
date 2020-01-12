# Autostart

You can configure mixing station to automatically connect to a mixer on startup using a configuration file.

## PC
You can pass the same parameters as commandline arguments
```
mixing-station.exe "-appSeries=X Air" -ip=192.168.1.1 -mixTarget=-1
```

## Parameters
| Parameter | Description |
| --- | --- |
| `appSeries` | Which mixer series to use (PC/iOS). Same value as the button text in the app |
| `ip` | IP address of the mixer, remove if you want to start the search instead. |
| `mixTarget` | Target mix for the access restrictions. See table below |
