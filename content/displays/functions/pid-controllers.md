---
title: "PID Controllers"
---

This guide explains how to configure and manage PID (Proportional-Integral-Derivative) controllers for process control. The guide covers how to set up controllers, assign channels, define conditions, adjust limits, configure gain tables, and monitor diagnostics for effective PID control.

## Overview
A PID controller adjusts a process by calculating an error (difference between a desired set point and the measured process variable) and applying proportional `P`, integral `I`, and derivative `D` corrections to produce an output. This software allows you to configure multiple PID controllers, each with customizable channels, conditions, limits, and gain tables. Real-time diagnostic plots help monitor and tune controller performance.

## Key PID Configuration Features

### Adding and Deleting Controllers

* Add a Controller: Use the "Add Controller" button to create a new PID controller with a default name ("New Controller"). This adds a new controller to the system for configuration.
* Delete a Controller: Select a controller and use the "Delete Controller" button. Confirm the action to remove the controller. Ensure you select the correct controller to avoid accidental deletion.

### Naming Controllers

* Assign a unique name to each controller in the "Name" field.
* Descriptive names (e.g., "Temperature Control" or "Speed Control") help identify the controller’s purpose.
* Changes are saved automatically when you finish editing the name.

### Input/Output Channels

Each PID controller requires four key channels:

* Input Channel: The measured process variable (e.g., current temperature).
* Set Point Channel: The desired target value (e.g., target temperature).
* Error Channel: The calculated difference between the set point and input.
* Output Channel: The controller’s output to adjust the process (e.g., solenoid duty cycle).
* Use the dropdown menus to assign appropriate channel IDs from your system. Ensure channels are correctly mapped to avoid control errors.

### Conditions

Conditions define when the controller is active and how it behaves:

* Enabled When: Set a condition to enable or disable the controller (e.g., enable only when a specific sensor is active). Use the condition editor to define this logic.
* Disabled Output Value: Specify a numeric output value (e.g., 0) for when the controller is disabled, ensuring the system remains in a safe state.
* Integral Reset When: Define a condition to reset the integral term to zero (e.g., when the error exceeds a threshold), preventing integral windup.

### Limits and Scaling

Fine-tune the PID terms and output with these settings:

* Proportional (P) Limits: Set positive and negative limits for the proportional term to cap its contribution (e.g., to prevent excessive corrections).
* Integral (I) Limits: Set positive and negative limits for the integral term to control accumulated error corrections.
* Derivative (D) Limits: Set positive and negative limits for the derivative term to manage rate-of-change corrections.
* Output Scalar: Multiply the final output by a scaling factor (default: 1) to adjust its magnitude.
* Output Offset: Add a fixed value (default: 0) to the final output for calibration or bias.
* Output Final Limits: Set positive and negative limits for the controller’s final output to ensure it stays within safe bounds.
* Enter numeric values for all limits and scaling factors, which are validated to ensure they are valid numbers.

### Gain Tables

Gain tables allow you to define variable gains for the PID terms based on operating conditions:

* Feed Forward Table: Adjusts the feed-forward term, which provides a baseline output independent of error (e.g., for known system dynamics).
* P Gain Table: Sets the proportional gain `P`, which scales the error to determine the proportional correction.
* I Gain Table: Sets the integral gain `I`, which scales the accumulated error over time.
* D Gain Table: Sets the derivative gain `D`, which scales the rate of change of the error.
* Switch between tabs to edit each table. Enter values to define how gains vary (e.g., based on error magnitude or other parameters).

### Derivative Mode

* Choose how the derivative term is calculated:
  * Derivative of Error: Uses the rate of change of the error (set point minus input).
  * Derivative of Measurement: Uses the rate of change of the input directly, which can reduce noise in systems with step changes in the set point.
* Select the mode from the dropdown in the "Miscellaneous" section.

### Diagnostic Channels and Monitoring

Monitor controller performance with real-time diagnostic plots:

* Main Plot: Shows the input, set point, output, and error channels over time, helping you visualize the control loop’s behavior.
* Diagnostic Plot: Displays diagnostic channels for:
  * Feed-Forward (FF) Output: The contribution of the feed-forward term.
  * P Output: The proportional term’s contribution.
  * I Output: The integral term’s contribution.
  * D Output: The derivative term’s contribution.
  * P Gain: The current proportional gain value.
  * I Gain: The current integral gain value.
  * D Gain: The current derivative gain value.
* Assign channel IDs for these diagnostics using the dropdown menus in the "Diagnostic Channels" section. Ensure valid channels are selected for accurate monitoring.

## Tips for Effective PID Tuning

* Start with Proportional Only: Set `I` and `D` to 0, then adjust `P` to achieve a stable but slightly oscillatory response.
* Add Integral for Steady-State Error: Gradually increase `I` to eliminate steady-state error, but watch for integral windup (use the "Integral Reset When" condition to mitigate this).
* Use Derivative Sparingly: Increase `D` to dampen oscillations, but avoid high values to prevent noise amplification. Consider "Derivative of Measurement" mode for noisy systems.
* Tune Gain Tables: Use gain tables to adjust `P`, `I`, and `D` based on operating conditions (e.g., higher `P` for larger errors).
* Monitor Diagnostics: Use the main and diagnostic plots to observe how each term (`P`, `I`, `D`) affects the output. Adjust limits if any term dominates unexpectedly.
* Test Conditions: Ensure "Enabled When" and "Integral Reset When" conditions are logical to prevent unintended controller behavior.
* Set Safe Limits: Use `P`, `I`, `D`, and final output limits to prevent excessive corrections that could damage the system.
* Iterate Gradually: Make small adjustments and test the system response, using diagnostic plots to guide tuning.

This guide covers the core PID configuration features to help you set up and tune controllers effectively.
