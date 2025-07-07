# Tascam SonicView

## Limitations / Known issues

The network protocol / mixer currently has the following limitations:

- Metering might not immediately start
- After the first connection, the data shown in the app will not match the
  mixer state. After ~40 seconds the values will update to show the correct data.
- Value control is only possible after ~20 seconds
- Connecting multiple clients may result in high traffic for all clients during the 
  sync.


These limitations are caused by limitations of the mixer, and can't be fixed
in the app.