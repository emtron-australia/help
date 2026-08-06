---
title: "Session Constants"
description: "Fixed values applied while analysing a log in EmVision."
weight: 9
---

**File → Session Constants**

Session Constants show vehicle setup values from the open log (weight, spring rates, and similar) and let you **override** them for maths “what-if” analysis. Overrides are saved with the log.

## Using session constants

1. Open a log.
2. Choose **File → Session Constants**.
3. Review values from the log; change values to override them for maths in this session.
4. **Add** a channel manually when needed (picker + value).
5. **Import** / **Export** as YAML (same format as Display Studio **Setup → Constants**). Import can take several files; later files win on the same channel. Import works even when the log has no constants — it creates session-only values for maths.

## Related

- [Math Channels](math-channels) — expressions that use constant channel values
- [User Channels](user-channels) — custom channel names for analysis
- [Constants (Display Studio)](/displays/setup/constants) — configuration constants on the vehicle
