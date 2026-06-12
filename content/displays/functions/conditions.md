---
title: "Conditions"
---

# Condition Setup

Conditions are the trigger logic used throughout the system — in alarms, virtual inputs, conditional logic, and more. A **condition set** is a list of one or more individual conditions combined with logic operators.

---

## Individual Conditions

Each condition compares a channel value against a threshold and returns true or false.

| Field          | Description                                                                                    |
|----------------|------------------------------------------------------------------------------------------------|
| **Channel**    | The channel whose live value is read as the left-hand side (LHS) of the comparison.            |
| **Comparison** | The operator to apply (see table below).                                                       |
| **RHS**        | The right-hand side — either a fixed constant (`#` mode) or a second live channel (`CH` mode). |

### Comparison Operators

| Name                     | Meaning                                                | RHS needed |
|--------------------------|--------------------------------------------------------|------------|
| Always False             | Always evaluates to false regardless of channel value. | No         |
| Greater Than             | LHS > RHS                                              | Yes        |
| Less Than                | LHS < RHS                                              | Yes        |
| Equal                    | LHS == RHS                                             | Yes        |
| Not Equal                | LHS ≠ RHS                                              | Yes        |
| Greater Than Or Equal To | LHS ≥ RHS                                              | Yes        |
| Less Than Or Equal To    | LHS ≤ RHS                                              | Yes        |
| Always True              | Always evaluates to true regardless of channel value.  | No         |

### Constant vs Channel RHS

The small **`#` / `CH` toggle** to the left of the RHS field switches modes:

- **`#` mode** — compare against a fixed number you type in.
- **`CH` mode** — compare against the live value of a second channel. This lets you express relationships like *"Engine RPM > Target RPM"* or *"Oil pressure < Minimum oil pressure"*.

In CH mode the live value of the RHS channel is shown alongside the LHS value so you can see both sides in real time.

---

## Live Preview

The coloured dot at the left of each condition row shows its current evaluation result:

| Colour    | Meaning                                                |
|-----------|--------------------------------------------------------|
| **Green** | Condition is currently true.                           |
| **Red**   | Condition is currently false.                          |
| **Grey**  | No live data available yet (channel not yet received). |

The dot updates every realtime frame — you can watch conditions transition as the system runs without needing to save or trigger anything.

---

## Logic Operators

When a condition set contains more than one condition, a logic operator sits between each pair and controls how they are combined.

| Operator | Meaning                                                   |
|----------|-----------------------------------------------------------|
| **AND**  | Both sides must be true.                                  |
| **OR**   | At least one side must be true.                           |
| **NOR**  | Neither side may be true (true only when both are false). |

### Evaluation Order — Left to Right, No Precedence

> **Important:** Logic operators are evaluated strictly left to right. There is no AND-before-OR precedence as you might expect from mathematics or programming languages.

Given conditions A, B, C with operators between them:

```
A  [AND]  B  [OR]  C
```

Evaluates as:

```
(A AND B) OR C
```

And:

```
A  [OR]  B  [AND]  C
```

Evaluates as:

```
(A OR B) AND C
```

This means **the order of your conditions matters**. If you need AND to bind tighter than OR, place the AND conditions consecutively at the top of the list.

#### Example — Engine over-temperature alarm

You want: *"Water temp high AND (RPM above idle OR load above 50%)"*

With left-to-right evaluation you cannot express this directly in one flat list. Instead, split it across two condition sets, or reorder so the OR comes first:

```
RPM > 1000
[OR]
Load > 50
[AND]
Water > 95
```

Evaluates as `((RPM > 1000) OR (Load > 50)) AND (Water > 95)` — which is correct for this case because the AND is last.

---
