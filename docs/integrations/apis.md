# APIs
Mixing Station provides different APIs for external software and hardware to connect to.
The goal of these APIs is to cover most of the console parameters using a unified API.
This enables your app to work with every mixer compatible with Mixing Station.

## Overview
All APIs are only available in the desktop version of Mixing Station.

## Configure APIs
To enable the API access, open the [global app settings](../settings/global.md) and enable REST and/or OSC.

## Data Types
The following data types are used:

| Type | Sample |
| --- | --- |
| bool | true/false |
| float | 1.20 |
| long/int | 1 |
| string | "hello" |



There are two possible float formats which can be used:

| Format | Description | 
| --- | --- |
| Plain values | The actual value of the parameter (e.g. -5) |
| Normalized | The value will be normalized into a range of 0-1 |


## REST
The REST api allows access via http using json encoded data.

### Using the API

1. Enable the http/rest api in the global app settings
2. Open the following URL in your browser: `http://localhost:<your-configured-port>`

You should now see a landing page which describes all API endpoints available.
Additionaly you can explore all data exposed via the API.


## OSC
Provides access to the same parameters accessible via the rest api.
You can see all available parameters by opening the data explorer (follow the rest api steps above and open the webpage)

OSC bundles are **not** supported.


### Syntax
The following syntax is used to describe the OSC packets:

- `[]` Can be one of the chars inside
- `{}` Placeholder which must be replaced with a value
- OSC uses `0` bytes for padding. For better readability these padding bytes are not indicated below.

### Subscribe
Send the follow packet at least once every 5 seconds to get updates for all parameters.
The last char determins the formatting

Plain value
```
/hi/v
```

Normalized value
```
/hi/n
```

### Get data
A OSC packet without any parameters is used to request the current value.
```
/con/[vn]/{dataPath}
```

### Set data
Setting the data is similar to getting but with additional parameters.
You can use any of the supported data types above.

```
/con/[vn]/{dataPath} f 0.0
```


### Examples
Get fader of ch 1 as dB value
```
/con/v/ch.0.mix.lvl
```

Get fader of ch 1 as normalized value
```
/con/n/ch.0.mix.lvl
```

Set fader of ch 1 using a dB value
```
/con/v/ch.0.mix.lvl f -5
```

Set fader of ch 1 using a normalized
```
/con/n/ch.0.mix.lvl f 0.5
```