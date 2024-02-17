# APIs

Mixing Station provides different {{ abbr('API') }}s for integration with external software and hardware.
The goal of these APIs is to cover the majority of console parameters with a unified API, allowing your application to
work with every mixer supported by Mixing Station.

## Overview

Note that the *full* set of APIs is only available in the desktop version of Mixing Station.

## Configure APIs

To enable {{ abbr('API') }} access, open the [global app settings](../settings/global.md) and enable {{ abbr('REST') }}
and/or {{ abbr('OSC') }}.

## Data Types

The following data types are used:

| Type     | Sample     |
|----------|------------|
| bool     | true/false |
| float    | 1.20       |
| long/int | 1          |
| string   | "hello"    |

There are two possible float formats as follows:

| Format       | Description                                  | 
|--------------|----------------------------------------------|
| Plain values | The actual value of the parameter (e.g. -5)  |
| Normalized   | The value is normalized within the range 0-1 |

## REST

The REST API allows access via HTTP using json-encoded data.

### Using the API

1. Enable the HTTP/REST API in the global app settings
2. Open the following URL in your browser: `http://localhost:<your-configured-port>`

The webpage describes all API endpoints and allows you to explore all data exposed by the API.

## OSC

The OSC interface provides similar access to that provided by the REST API.
You can see all available parameters by opening the data explorer (follow the REST API steps above and open the
webpage).

Note that OSC bundles are **not** supported.

### Syntax

The following syntax is used to describe the OSC packets:

- `[]` Can be one of the chars inside.
- `{}` Placeholder which must be replaced with a value.
- OSC uses `0` bytes for padding. For better readability these padding bytes are not indicated below.

### Subscribe

Send the following packet at least once every 5 seconds to get updates for all parameters.
The last char determines the formatting

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
You can use any of the supported data types described above.

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