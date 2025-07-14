# Flood Data Dataset

This dataset contains environmental features used to predict whether a flood will occur. It is ideal for binary classification tasks in machine learning.

## Dataset Summary

- **File Name**: `Flood_data.csv`
- **Total Entries**: 1010
- **Total Features**: 5

## Columns Description

| Column Name     | Data Type | Description                                                  |
|-----------------|-----------|--------------------------------------------------------------|
| `rainfall_mm`   | float     | Rainfall in millimeters.                                     |
| `river_level`   | float     | River water level in meters.                                 |
| `temp`          | float     | Temperature in degrees Celsius.                              |
| `wind_speed`    | float     | Wind speed in km/h.                                          |
| `flood_occurred`| integer   | Binary value indicating flood occurrence (1 = Yes, 0 = No).  |

## Sample Data

```
| rainfall_mm | river_level | temp | wind_speed | flood_occurred |
|-------------|--------------|------|-------------|-----------------|
| 120.0       | 6.5          | 28.0 | 20.0        | 1               |
| 85.0        | 5.8          | 30.0 | 15.0        | 1               |
| 30.0        | 3.2          | 32.0 | 12.0        | 0               |
```

## Use Cases

- **Flood Prediction**
- **Environmental Monitoring**
- **Risk Assessment for Natural Disasters**

## Suggested Machine Learning Tasks

- Binary Classification (Flood vs. No Flood)
- Feature Importance Analysis

## License

This dataset is provided for educational and research purposes.
