# IoT Sensor Data Analyzer

A Python pipeline built to process CSV telemetry data, track temperature metrics, and filter status alerts. 

## Key Features
- **Safe File Operations:** Uses context managers and exception handling to read files safely without crashing or leaking resources.
- **Data Parsing & Cleaning:** Skips headers, trims whitespace, splits CSV streams, and casts types for accurate math.
- **Statistical Aggregations:** Calculates peak and running average temperatures across logs.
- **Smart Alerting:** Triggers warnings based on status tags (`WARNING` / `CRITICAL`) instead of basic numbers to avoid alert fatigue.

## Tech Stack
- **Language:** Python 3
- **Concepts:** File I/O, error handling, string parsing, type casting, loops, conditional logic.

## Sample Output
```text
ALERT! Sensor Status is WARNING : 38.2°C
ALERT! Sensor Status is CRITICAL : 45.1°C

 =====SENSOR SUMMARY=====
The Highest Temperature is 46.0°C
The Average Temperature is 29.0°C
```
