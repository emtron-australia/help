---
title: "Gauges"
description: "Comprehensive reference for all gauge types in the Emtron Displays"
---

# Gauge Types Reference

This document provides comprehensive documentation for all gauge types available in the Emtron Displays.

## Table of Contents

1. [Common Properties](#common-properties)
2. [Text Gauge](#text-gauge)
3. [Value Gauge](#value-gauge)
4. [Time Gauge](#time-gauge)
5. [Bar Gauge](#bar-gauge)
6. [Dial Gauge](#dial-gauge)
7. [Image Gauge](#image-gauge)
8. [Cropped Image Gauge](#cropped-image-gauge)
9. [Cropped Circular Image Gauge](#cropped-circular-image-gauge)
10. [Multi Image Gauge](#multi-image-gauge)
11. [Color Fade Gauge](#color-fade-gauge)
12. [Status Gauge](#status-gauge)
13. [Layer Group Gauge](#layer-group-gauge)
14. [Camera Gauge](#camera-gauge)

---

## Common Properties

All gauges share these common configuration properties:

| Property       | Description                                    |
|----------------|------------------------------------------------|
| `Channel ID`   | The channel ID to read data from               |
| `X Position`   | X position on screen (pixels)                  |
| `Y Position`   | Y position on screen (pixels)                  |
| `Width`        | Width of the gauge (pixels)                    |
| `Height`       | Height of the gauge (pixels)                   |
| `Opacity`      | Opacity level (0-100)                          |
| `Z Layer`      | Z-ordering layer (higher values render on top) |
| `TestValue`    | Value used during testing/preview              |
| `TestValueMin` | Minimum test value                             |
| `TestValueMax` | Maximum test value                             |

---

## Text Gauge

Displays static text on the screen. This gauge renders during the static content phase and does not change with channel values.

### Configuration

| Property               | Description                                                |
|------------------------|------------------------------------------------------------|
| `Colour`               | Hex color code (e.g., "#FFFFFF")                           |
| `Text`                 | The text to display                                        |
| `Pixel Size`           | Font size in pixels                                        |
| `Horizontal Alignment` | Horizontal alignment (AlignLeft, AlignHCenter, AlignRight) |
| `Vertical Alignment`   | Vertical alignment (AlignTop, AlignVCenter, AlignBottom)   |
| `Font`                 | Font file path (empty = default font)                      |

### Usage Notes

- Text is pre-rendered and cached for performance
- Static content only - no dynamic updates
- Ideal for labels, titles, and static indicators
- Uses the fast font rendering system

### Example Use Cases

- RPM label above a value gauge
- Screen titles
- Unit indicators (km/h, psi, °C)
- Static warning messages

---

## Value Gauge

Displays numeric channel values with optional decimal places and color thresholds.

### Configuration

| Property                | Description                            |
|-------------------------|----------------------------------------|
| `Colour`                | Default text color (hex code)          |
| `Decimal Places`        | Number of decimal places to display    |
| `Pixel Size`            | Font size in pixels                    |
| `Horizontal Alignment`  | Horizontal alignment                   |
| `Vertical Alignment`    | Vertical alignment                     |
| `Low Colour`            | Color when value ≤ lowColourThreshold  |
| `Low Colour Threshold`  | Threshold for low color                |
| `High Colour`           | Color when value ≥ highColourThreshold |
| `High Colour Threshold` | Threshold for high color               |
| `Font`                  | Font file path (empty = default font)  |

### Behavior

- Displays "-" if channel doesn't exist or value is NaN
- Supports both numeric and string channels
- String values use `GetStringTexture` for rendering
- Numeric values use font atlas for performance
- Color changes based on threshold comparison

### Usage Notes

- Thresholds allow for visual warnings (e.g., red for high temperature)
- Font atlas provides fast rendering for numeric displays
- String channels display the raw string value

### Example Use Cases

- Engine RPM display
- Temperature readings with warning colors
- Pressure gauges with threshold alerts
- Boost levels

---

## Time Gauge

Displays time values in `M:SS.mmm` format (minutes:seconds.milliseconds) with threshold-based coloring.

### Configuration

| Property                | Description                            |
|-------------------------|----------------------------------------|
| `Colour`                | Default text color (hex code)          |
| `Pixel Size`            | Font size in pixels                    |
| `Horizontal Alignment`  | Horizontal alignment                   |
| `Vertical Alignment`    | Vertical alignment                     |
| `Low Colour`            | Color when value ≤ lowColourThreshold  |
| `Low Colour Threshold`  | Threshold for low color                |
| `High Colour`           | Color when value ≥ highColourThreshold |
| `High Colour Threshold` | Threshold for high color               |
| `Font`                  | Font file path (empty = default font)  |

### Behavior

- Input value is in seconds (supports negative values)
- Format: `[-]M:SS.mmm`
  - Minutes padded to 1 digit minimum
  - Seconds padded to 2 digits
  - Milliseconds padded to 3 digits
- Displays "-:--.---" if channel doesn't exist or value is NaN
- Color changes based on threshold comparison

### Usage Notes

- Designed for lap times, timers, and duration displays
- Supports negative times with "-" prefix
- Millisecond precision for racing applications

### Example Use Cases

- Lap timers
- Split times
- Best lap comparison
- Countdown timers

---

## Bar Gauge

Displays a filled bar that grows/shrinks based on channel value. Supports multiple directions and color modes.

### Configuration

| Property          | Description                                             |
|-------------------|---------------------------------------------------------|
| `Min Value`       | Minimum value for 0% fill                               |
| `Max Value`       | Maximum value for 100% fill                             |
| `Colour`          | Color for SingleColour mode (hex code)                  |
| `Direction`       | Fill direction (Left, Right, Up, Down, etc.)            |
| `Invert`          | Invert the fill direction (true = empty on high values) |
| `Colour Type`     | SingleColour or MultiColour                             |
| `Mid Lower Value` | Lower threshold for MultiColour mode                    |
| `Mid Upper Value` | Upper threshold for MultiColour mode                    |
| `Min Colour`      | Color below midLowerValue (hex code)                    |
| `Mid Colour`      | Color between midLower and midUpper (hex code)          |
| `Max Colour`      | Color above midUpperValue (hex code)                    |

### Supported Directions

- `Left` (0) - Fills from right to left
- `Right` (1) - Fills from left to right
- `Up` (2) - Fills from bottom to top
- `Down` (3) - Fills from top to bottom
- `UpLeft` (4) - Fills diagonally
- `UpRight` (5) - Fills diagonally
- `DownLeft` (6) - Fills diagonally
- `DownRight` (7) - Fills diagonally

### Behavior

- Value is clamped between minValue and maxValue
- Fill ratio = (value - minValue) / (maxValue - minValue)
- `invert` flips the ratio (1 - ratio)
- MultiColour mode selects color based on current value

### Usage Notes

- Perfect for analog-style gauges
- Diagonal directions allow creative layouts
- MultiColour provides visual zones (safe/warning/danger)

### Example Use Cases

- Fuel level indicator
- Temperature bars
- RPM bars with color zones
- Battery charge indicators

---

## Dial Gauge

Rotates an image around a pivot point based on channel value. Supports linear and non-linear angle mapping.

### Configuration

| Property       | Description                              |
|----------------|------------------------------------------|
| `File Name`    | Image file name (from images/ directory) |
| `Min Value`    | Value at minAngle                        |
| `Max Value`    | Value at maxAngle                        |
| `Min Angle`    | Starting angle in degrees                |
| `Max Angle`    | Ending angle in degrees                  |
| `Pivot X`      | X coordinate of rotation pivot           |
| `Pivot Y`      | Y coordinate of rotation pivot           |
| `Direction`    | Clockwise or AntiClockwise               |
| `Mapping Type` | Linear or NonLinear                      |
| `Map`          | Non-linear mapping points                |

### AngleToValueMap

| Property | Description                 |
|----------|-----------------------------|
| `Angle`  | Angle in degrees            |
| `Value`  | Channel value at this angle |

### Behavior

- **Linear mapping**: Angle interpolates linearly between min and max
- **Non-linear mapping**: Uses custom mapping points for irregular scales
  - Points are sorted by value
  - Linear interpolation between mapping points
  - Angles outside range are clamped
- Direction affects angle sign (AntiClockwise negates angle)

### Usage Notes

- Pivot point is relative to the gauge dimensions
- Image should be designed with needle pointing at 0 degrees
- Non-linear mapping useful for non-uniform gauge scales
- Supports values outside min/max range (clamped to limits)

### Example Use Cases

- Traditional speedometer needles
- Tachometer needles
- Temperature gauge needles
- Fuel gauge needles with non-linear sweep

---

## Image Gauge

Displays a static image. Can render in static or dynamic phase.

### Configuration

| Property                  | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `File Name`               | Image file name (from images/ directory)                     |
| `Force Foreground Render` | If true, renders in dynamic phase; if false, in static phase |

### Behavior

- **Static rendering** (forceForegroundRender = false):
  - Renders once during `RenderStaticContent`
  - Image never changes
  - Best performance for backgrounds
- **Dynamic rendering** (forceForegroundRender = true):
  - Renders every frame during `RenderDynamicContent`
  - Can layer on top of other dynamic gauges
  - Slightly lower performance

### Usage Notes

- Use static rendering for backgrounds, frames, and decorations
- Use dynamic rendering when image needs to appear above other gauges
- Image is scaled to fit gauge dimensions (w × h)
- Supports transparency (PNG alpha channel)

### Example Use Cases

- Background images
- Gauge bezels and frames
- Logos and branding
- Decorative elements

---

## Cropped Image Gauge

Displays a progressively revealed image based on channel value. The image is "uncropped" as the value increases.

### Configuration

| Property    | Description                              |
|-------------|------------------------------------------|
| `File Name` | Image file name (from images/ directory) |
| `Min Value` | Value at 0% reveal                       |
| `Max Value` | Value at 100% reveal                     |
| `Direction` | Direction of reveal                      |
| `Invert`    | Invert the reveal direction              |

### Behavior

- Value is clamped between minValue and maxValue
- Ratio = (value - minValue) / (maxValue - minValue)
- `invert` flips the ratio
- Source and destination rectangles adjusted based on direction
- Only the visible portion is rendered

### Supported Directions

Same as Bar Gauge: Left, Right, Up, Down, UpLeft, UpRight, DownLeft, DownRight

### Usage Notes

- Image gradually appears based on value
- Different from opacity - only reveals portion of image
- Perfect for creative fill indicators
- Source image should represent "full" state

### Example Use Cases

- Creative fuel gauges (image of fuel tank filling)
- Battery icons that fill up
- Progress indicators with custom graphics
- Temperature visuals (thermometer filling)

---

## Cropped Circular Image Gauge

Displays an image with circular/radial cropping based on channel value. Creates a "pie chart" or "arc" effect.

### Configuration

| Property       | Description                              |
|----------------|------------------------------------------|
| `File Name`    | Image file name (from images/ directory) |
| `Min Value`    | Value at startAngle                      |
| `Max Value`    | Value at sweepAngle                      |
| `Start Angle`  | Starting angle in degrees (0° = top)     |
| `Sweep Angle`  | Ending angle in degrees                  |
| `Direction`    | Clockwise or AntiClockwise               |
| `Mapping Type` | Linear or NonLinear                      |
| `Map`          | Non-linear mapping points                |

### Behavior

- Renders image using triangular geometry from center point
- Image is UV-mapped to create circular reveal effect
- **Linear mapping**: Angle interpolates linearly between start and sweep
- **Non-linear mapping**: Uses custom mapping points
- Direction affects sweep direction

### Technical Details

- Divides sweep into triangular segments
- Handles both horizontal and vertical edge tracing
- Supports full 360° sweeps (multiple rotations)
- Angles wrap around 2π radians

### Usage Notes

- Best for circular gauges with image backgrounds
- Center of gauge (w/2, h/2) is the rotation pivot
- 0° angle points upward, increases clockwise by default

### Example Use Cases

- Circular RPM gauges with gradient backgrounds
- Radial progress indicators
- Speedometer arcs
- Fuel level circles

---

## Multi Image Gauge

Displays different images based on discrete channel values (acts like a switch statement).

### Configuration

| Property | Description                     |
|----------|---------------------------------|
| `Images` | List of value-to-image mappings |

### ValueWithFilename

| Property    | Description                                         |
|-------------|-----------------------------------------------------|
| `Value`     | Channel value to match (rounded to nearest integer) |
| `File Name` | Image to display when value matches                 |

### Behavior

- Compares channel value (rounded) to each image's value
- Displays first matching image
- If no match, nothing is displayed
- Only one image shown at a time

### Usage Notes

- Values are rounded to nearest integer before comparison
- Useful for discrete states or modes
- Images should be same size for consistent display
- Order matters - first match wins

### Example Use Cases

- Gear position indicators (1, 2, 3, 4, 5, 6, N, R)
- Drive mode displays (Eco, Sport, Race)
- Warning icons based on error codes
- State indicators (Off, Idle, Active, Error)

---

## Color Fade Gauge

Fills a rectangle with color that transitions smoothly between three colors based on channel value.

### Configuration

| Property          | Description                                            |
|-------------------|--------------------------------------------------------|
| `Min Value`       | Value at minColour                                     |
| `Mid Lower Value` | Value where minColour → midColour transition completes |
| `Mid Upper Value` | Value where midColour → maxColour transition starts    |
| `Max Value`       | Value at maxColour                                     |
| `Min Colour`      | Color at minimum value (hex code)                      |
| `Mid Colour`      | Color in middle range (hex code)                       |
| `Max Colour`      | Color at maximum value (hex code)                      |

### Behavior

- Value is clamped between Min Value and Max Value
- Three zones:
  1. **Min Value to Mid Lower Value**: Linear interpolation from Min Colour to Mid Colour
  2. **Mid Lower Value to Mid Upper Value**: Solid Mid Colour
  3. **Mid Upper Value to Max Value**: Linear interpolation from Mid Colour to Max Colour
- Color interpolation is RGB lerp (linear interpolation per channel)

### Usage Notes

- Creates smooth color gradients
- Middle zone can be zero-width (midLowerValue = midUpperValue)
- Useful for visual feedback without numbers
- Fills entire gauge area

### Example Use Cases

- Temperature warning lights (blue → green → yellow → red)
- Background status indicators
- Visual alarm states
- Mood lighting effects

---

## Status Gauge

Displays text with colored background based on discrete channel values. Similar to Multi Image but with text.

### Configuration

| Property               | Description                           |
|------------------------|---------------------------------------|
| `Pixel Size`           | Font size in pixels                   |
| `Horizontal Alignment` | Horizontal text alignment             |
| `Vertical Alignment`   | Vertical text alignment               |
| `Texts`                | List of value-to-text mappings        |
| `Font`                 | Font file path (empty = default font) |

### StatusText

| Property            | Description                                         |
|---------------------|-----------------------------------------------------|
| `Value`             | Channel value to match (rounded to nearest integer) |
| `Text`              | Text to display                                     |
| `Text Colour`       | Foreground text color (hex code)                    |
| `Background Colour` | Background fill color (hex code)                    |

### Behavior

- Compares channel value (rounded) to each status text's value
- Displays first matching text with its colors
- Background fills entire gauge area
- Text is pre-rendered and cached

### Usage Notes

- Values are rounded to nearest integer before comparison
- Both foreground and background colors customizable
- Text is cached for performance
- Order matters - first match wins

### Example Use Cases

- Gear position display ("N", "1", "2", "3")
- System status ("OK", "WARNING", "ERROR")
- Mode indicators ("ECO", "SPORT", "RACE")
- Boolean states ("ON"/"OFF", "ARMED"/"DISARMED")

---

## Layer Group Gauge

Manages multiple layers (screens within screens) that can be switched via events. Each layer contains its own set of gauges.

### Configuration

| Property           | Description                          |
|--------------------|--------------------------------------|
| `Layer Configs`    | List of layer definitions            |
| `Next Layer Event` | Event ID to switch to next layer     |
| `Prev Layer Event` | Event ID to switch to previous layer |
| `Name`             | Name of the layer group              |

### LayerConfig

| Property           | Description                          |
|--------------------|--------------------------------------|
| `Layer ID`         | ID of the layer to display           |
| `Is Default Layer` | If true, shown on startup            |
| `Show Event`       | Event ID to directly show this layer |

### Behavior

- Each layer has its own texture for off-screen rendering
- Only one layer is active/visible at a time
- Layer switching triggered by events:
  - **Next Layer Event**: Cycles to next layer (wraps around)
  - **Prev Layer Event**: Cycles to previous layer (wraps around)
  - **Show Event**: Jumps directly to specific layer
- Layers are rendered to texture, then copied to screen
- Both static and dynamic content supported per layer

### Rendering Process

1. Set render target to layer's texture
2. Clear texture
3. Render layer's gauges (static or dynamic)
4. Restore render target
5. Copy layer texture to screen at gauge position

### Usage Notes

- Layers are separate screens with independent gauge layouts
- Event-driven switching enables complex UI flows
- Each layer has its own texture (memory overhead)
- Default layer shown initially if specified
- Texture size matches layer dimensions (may differ from gauge size)

### Example Use Cases

- Multi-page dashboards (Main, Performance, Diagnostics)
- Context-sensitive displays (Normal, Warning, Critical)
- Menu systems
- Wizard-style configuration screens

---

## Camera Gauge

Displays live camera feed with optional flipping.

### Configuration

| Property          | Description             |
|-------------------|-------------------------|
| `Flip Vertical`   | Flip image vertically   |
| `Flip Horizontal` | Flip image horizontally |

### Behavior

- Renders camera texture provided externally
- Does not render anything in static or dynamic phases
- Texture alpha controlled by gauge opacity

### Usage Notes

- Camera texture provided externally (not loaded from file)
- Flip options useful for correcting camera orientation
- No static/dynamic rendering - only camera feed
- Scales camera feed to gauge dimensions

### Example Use Cases

- Rear-view camera display
- Side camera mirrors
- Track camera feed
- Dash cam preview

---

## Rendering Architecture

### Two-Phase Rendering

The gauge system uses a two-phase rendering approach:

1. **Static Content Phase**
   - Rendered once or when screen changes
   - Text labels, backgrounds, static images

2. **Dynamic Content Phase**
   - Rendered every frame
   - Values, needles, bars, etc.
   - Updated based on channel values

### Z-Layer Ordering

Gauges are rendered in order of their `Z Layer` property:
- Lower Z Layer values render first (background)
- Higher Z Layer values render last (foreground)
- Allows complex layering of gauges

### Opacity and Blending

- Opacity range: 0-100
- Supports transparency in images and colors

### Color Format

Colors are specified as hex strings:
- Format: `"#RRGGBB"` (e.g., "#FF0000" for red)

---

## Best Practices

### Layout

- Use alignment properties for precise positioning
- Consider screen resolution and scaling
- Group related gauges with similar zLayer values
- Use layer groups for complex multi-screen UIs

### Visual Design

- Use color thresholds for warnings (value/time gauges)
- Use color zones for operational ranges (bar/colorfade)
- Maintain consistent opacity for visual hierarchy
- Use multi-state gauges (status/multiimage) for discrete values

### Configuration

- Test with testValue during development
- Define clear min/max ranges for accuracy
- Use non-linear mapping for irregular scales


---

## Troubleshooting

### Common Issues

**Gauge not appearing:**
- Check channelId is valid
- Verify zLayer ordering
- Ensure opacity > 0
- Check xPos/yPos within screen bounds

**Colors not working:**
- Verify hex color format (#RRGGBB)
- Check opacity setting
- Ensure blend mode supported

**Images not loading:**
- Confirm file exists in images/ directory
- Check fileName spelling and case
- Verify image format (PNG recommended)

**Performance issues:**
- Move static elements to RenderStaticContent
- Reduce number of dynamic gauges
- Use simpler gauge types where possible
- Optimize image sizes

**Layer group issues:**
- Verify layer IDs are correct
- Check event IDs are unique and valid
- Ensure at least one default layer
- Confirm texture creation succeeded

