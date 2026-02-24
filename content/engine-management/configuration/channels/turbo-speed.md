---
title: "Turbo Speed"
weight: 18
---

Turbo Speed is available on Channels DI 1- 8 on KV Series and DI1-4 on SL Series. 
The units are RPM

> **Tip:** See [Speed Inputs](./speed.md) for information on sensor setup.

## Turbo Speed Calculation
```
Turbo Speed(RPM) = Frequency x Scaler x 10
```

**Example:** 2351 Hz, Scaler = 2.56
Turbo Speed = (2351 Hz x 2.56) x 10 = 60180 RPM

**Example:** 4436 Hz, Scaler = 2.56
Turbo Speed = (4436 Hz x 2.56) x 10 = 113560 RPM

> **Note:** Turbo speed sensor electronics divide the raw frequency by 8

### Scaler
Turbo Fin Count: 14
Electronics Divider : 8
Turbo Speed : 100,000
Convert Pulse to Frequency : /60
```
(100000 / 8) x 14 / 60 = 2916.67 Hz
```
Resolution Modifier : 10

2916.67 x 10 = 29166.7

```
Scaler = 10000 / 29166.7 = 3.43
```