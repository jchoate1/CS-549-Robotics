# Lab 4: Wall Following

## Objectives

1. Implement the right-hand rule for wall following
2. Create a state machine for navigation behaviors
3. Tune parameters for smooth wall tracking
4. Test in the physical maze

## Background

Wall following is a fundamental maze-solving algorithm. The **right-hand rule** states: keep your right hand touching the wall, and you will eventually find the exit of any simply connected maze.

### State Machine Approach

Wall following can be modeled as a state machine:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌──────────┐    wall on right    ┌──────────────┐     │
│  │  FIND    │ ──────────────────▶ │   FOLLOW     │     │
│  │  WALL    │                     │   WALL       │     │
│  └──────────┘ ◀────────────────── └──────────────┘     │
│       │           lost wall              │             │
│       │                                  │             │
│       │ blocked                  blocked │             │
│       ▼                                  ▼             │
│  ┌──────────┐                     ┌──────────────┐     │
│  │  TURN    │                     │   TURN       │     │
│  │  LEFT    │                     │   LEFT       │     │
│  └──────────┘                     └──────────────┘     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Right-Hand Rule Logic

```
1. If right side is clear: turn right, move forward (find the wall)
2. If right side has wall AND front is clear: move forward (follow wall)
3. If front is blocked: turn left
4. If completely blocked: turn around
```

## Assignment

### Part 1: Basic Wall Following

Implement the right-hand rule in `wall_follow_starter.py`:

- Read all 5 distance sensor values
- Determine if wall is on right, front is clear, etc.
- Execute appropriate movement

### Part 2: Smooth Following

Enhance your implementation to:
- Maintain consistent distance from wall
- Avoid jerky corrections
- Handle corners smoothly

### Part 3: Maze Navigation

Test your wall follower in the physical maze:
- Start at the entrance
- Navigate to the exit
- Time your runs

## Files

| File | Description |
|------|-------------|
| `wall_follow_starter.py` | Starter code with TODOs |
| `wall_follow_solution.py` | Reference solution |

## Parameters to Tune

| Parameter | Suggested Start | Purpose |
|-----------|-----------------|---------|
| `WALL_THRESHOLD` | 20 cm | Max distance to consider "wall present" |
| `FRONT_THRESHOLD` | 15 cm | Distance to consider "blocked" |
| `FOLLOW_SPEED` | 8 cm/s | Forward driving speed |
| `TURN_ANGLE` | 45° | Angle for turns |

## Testing Approach

1. **Open space first**: Test basic turning in open area
2. **Single wall**: Test following a single wall
3. **Corner**: Test turning at corners
4. **Simple maze**: Test in a basic maze configuration
5. **Full maze**: Complete maze navigation

## Common Issues and Solutions

**Robot oscillates along wall:**
- Increase the dead band between "turn toward wall" and "turn away from wall"
- Add hysteresis to your threshold checks

**Robot clips corners:**
- Reduce forward speed
- Start turning earlier (increase front threshold)
- Add a small backup before turning

**Robot loses the wall:**
- Decrease wall threshold
- Add a "search" behavior when wall is lost

**Robot gets stuck in corners:**
- Add a "stuck" detection (no movement for X seconds)
- Implement backup and turn recovery

## Deliverables

1. Working `wall_follow.py`
2. Video of robot navigating the maze
3. Notes on parameter tuning

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Wall detection works | 20 |
| Right-hand rule implemented | 30 |
| Smooth wall following | 20 |
| Successfully navigates maze | 30 |
| **Total** | **100** |
