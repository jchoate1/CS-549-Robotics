# Lab 3: Distance Sensor Integration

## Objectives

1. Read and interpret ToF distance sensor data
2. Implement threshold-based obstacle detection
3. Create visual feedback using LEDs
4. Build reactive behaviors based on sensor input

## Background

The Arduino Alvik has a Time-of-Flight (ToF) distance sensor that returns 5 readings covering different zones of its field of view. This lab will familiarize you with the sensor before using it for maze navigation.

### Sensor Output

```python
left, center_left, center, center_right, right = alvik.get_distance()
# Returns 5 values in CENTIMETERS
# Example: (41.6, 37.5, 41.2, 45.0, 37.1)
```

The 5 zones span approximately 60° field of view, allowing the robot to determine not just distance, but also the direction of obstacles.

## Assignment

### Part 1: Basic Sensor Reading

Complete `sensor_reader.py` to continuously read and display sensor values.

Requirements:
- Print all 5 sensor values
- Update at least 5 times per second
- Handle Ctrl+C gracefully

### Part 2: LED Feedback

Modify your code to change LED colors based on the center distance:
- **Green**: > 30 cm (clear)
- **Yellow**: 15-30 cm (caution)  
- **Red**: < 15 cm (danger)

### Part 3: Directional Detection

Enhance your code to indicate obstacle direction:
- If obstacle is more to the left: left LED red, right LED green
- If obstacle is more to the right: left LED green, right LED red
- If obstacle is centered: both LEDs same color

### Part 4: Reactive Stop

Make the robot drive forward slowly and automatically stop when an obstacle is detected within 15 cm.

## Files

| File | Description |
|------|-------------|
| `sensor_reader_starter.py` | Starter code for Part 1-3 |
| `reactive_stop_starter.py` | Starter code for Part 4 |

## Testing

1. Run your sensor reader and wave your hand at different distances
2. Move your hand left and right to test directional detection
3. Place obstacles at known distances and verify readings
4. Test reactive stop by placing hand in front of moving robot

## Deliverables

1. Working `sensor_reader.py` with LED feedback
2. Working `reactive_stop.py` 
3. Brief notes on sensor accuracy observations

## Hints

- The sensor can be noisy - consider averaging a few readings
- Test in consistent lighting conditions
- Keep the sensor lens clean
- `time.sleep(0.1)` gives ~10 readings per second

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Sensor reading works | 25 |
| LED color feedback correct | 25 |
| Directional detection works | 25 |
| Reactive stop works | 25 |
| **Total** | **100** |
