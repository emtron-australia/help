---
title: "Math Functions"
description: "How to configure the real time math processing system"
---

## Settings

### Evaluation

 * Continuous - the expressions are evaluated constantly at 100Hz
 * On Event - the expressions are evaluated only when the assigned event occurs

### Variable Name

This is the variable name that will become available for use in the expression.

### Derivative

When checked, an additional variable will become available containing the derivative of the input channel. The derivative variable uses the standard variable name with a `d` prefix.

e.g. If the channel variable is `EngineSpeed`, then the derivative variable will be `dEngineSpeed`.

## Expression Syntax

Expressions are written using the [Expr](https://expr-lang.org/) language.

### Numeric Literals

| Type    | Examples                              |
|---------|---------------------------------------|
| Integer | `42`, `0x2A` (hex), `0b1010` (binary) |
| Float   | `0.5`, `.5`                           |

### Arithmetic Operators

| Operator    | Description         | Example        |
|-------------|---------------------|----------------|
| `+`         | Addition            | `rpm + 500`    |
| `-`         | Subtraction         | `temp - 20`    |
| `*`         | Multiplication      | `load * 0.5`   |
| `/`         | Division            | `fuel / 4`     |
| `%`         | Modulus (remainder) | `counter % 10` |
| `^` or `**` | Exponent            | `x ^ 2`        |

### Comparison Operators

Returns `1` (true) or `0` (false).

| Operator | Description              |
|----------|--------------------------|
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

### Logical Operators

| Operator       | Description |
|----------------|-------------|
| `&&` or `and`  | Logical AND |
| `\|\|` or `or` | Logical OR  |
| `!` or `not`   | Logical NOT |

### Conditional (Ternary) Operator

```
condition ? valueIfTrue : valueIfFalse
```

Example: `rpm > 3000 ? 1 : 0`

### Local Variables

Use `let` to declare intermediate values within an expression. Separate statements with `;`.

```
let x = rpm / 60;
let y = x * 2;
y + offset
```

## Special Variables:
* `timeDelta` Time since last evaluation in seconds.
* `previousResult` Previous result of the expression.

## Math Utilities:
All trig functions are in radians.
* `math.Sin(x)` Returns the sine of x.
* `math.Cos(x)` Returns the cosine of x.
* `math.Tan(x)` Returns the tanginent of x.
* `math.Asin(x)` Returns the arcsine of x.
* `math.Acos(x)` Returns the arccosine of x.
* `math.Atan(x)` Returns the arctangent of x.
* `math.Hypot(p, q)` Returns the hypotenuse of p and q.
* `math.Exp(x)` Returns the base e exponential of x.
* `math.Abs(x)` Returns the absolute of x.
* `math.Log(x)` Returns the natural log of x.
* `math.Log10(x)` Returns the decimal log of x.
* `math.Sqrt(x)` Square root.
* `math.Min(x, y)` Mimimum.
* `math.Max(x, y)` Maximum.
* `math.Clamp(x, min, max)` Clamps x between min and max.
* `math.Pow(x, y)` Returns x to the power of y.
* `math.Pow10(n)` Returns 10 to the power of n.
* `math.Round(x)` Rounds to the nearest ingteger.
* `math.Deg2Rad(x)` Converts degrees to radians.
* `math.Rad2Deg(x)` Converts radians to degrees.
* `math.Blend(ratio, x, y)` Blends x and y together depending on the ratio. A ratio of 0 uses all of x, 0.5 half of each and 1 uses all of y.

## Filter Utilities:
Only one of each type of filter function can be used per expession.
* `filter.MovingAverage(input, n)` Returns the moving average based on n samples. The value of n must be constant.
* `filter.Exponential(input, smoothing)` Returns the exponential filtered value based on smoothing factor. Smoothing factor ranges from 0 to 1, with 0 being the most filtering. The smoothing factor can be changed dynamically.
* `filter.Schmitt(input, lowValue, highValue)` Schmitt trigger. Turns the input into 1 once the value has gone above highValue, then to 0 once the value has gone below lowValue.
* `filter.DelayedSchmitt(input, lowValue, highValue, offTimeS, onTimeS)` Schmitt trigger. Turns the input into 1 once the value has gone above highValue for onTimeS, then to 0 once the value has gone below lowValue for offTimeS.
* `filter.RateOfChange(input, maxPositiveRatePerSecond, maxNegativeRatePerSecond)` Limits the rate of change of the input. The rate of change is limited to the maxPositiveRatePerSecond and maxNegativeRatePerSecond. Both rates limits are positive numbers.
* `filter.Median(input, n)` Returns the median of the last n samples. The value of n must be constant and should be an odd number.
* `filter2.MovingAverage(input, n)` Same as filter.MovingAverage.
* `filter2.Exponential(input, smoothing)` Same as filter.Exponential.
* `filter3....` Same as filter...

## Calculus Utilities:
* `calc.Integrate(input, deltaTime, initial, enable)` Returns the integral of the input. The initial value is the starting value of the integral. If the enable flag is false, the integral is reset to the initial value..
* `calc.IntegrateClamped(input, deltaTime, initial, min, max, enable)` Same as calc.Integrate, but clamps the output between min and max.