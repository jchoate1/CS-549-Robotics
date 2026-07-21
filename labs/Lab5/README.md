# Lab 5: Maze Challenge

## Objectives

1. Integrate all skills from the course
2. Successfully navigate a maze autonomously
3. Optimize for speed and reliability
4. Compete in the maze challenge

## The Challenge

Navigate from the maze entrance to the exit as quickly as possible.

### Rules

1. **Autonomous only** - No remote control or human intervention
2. **Start position** - Robot must start behind the start line
3. **Timing** - Starts when robot crosses start line, stops when robot reaches goal
4. **Attempts** - Each team gets 3 attempts, best time counts
5. **Disqualification** - Touching the robot during a run disqualifies that attempt

### Scoring

| Criterion | Points |
|-----------|--------|
| Completes maze | 50 |
| Time bonus (under 60s) | 20 |
| Time bonus (under 45s) | 10 additional |
| Time bonus (under 30s) | 10 additional |
| Code quality | 10 |
| **Maximum** | **100** |

## Approach Options

### Option 1: Wall Following (Recommended)

Use your Lab 4 wall follower with enhancements:
- Better corner handling
- Speed optimization
- Recovery from stuck situations

### Option 2: Exploration + Return

Two-phase approach:
1. Explore maze while building a map
2. Use A* on the map to find optimal path
3. Execute optimal path at higher speed

More complex but potentially faster.

### Option 3: Hybrid

Combine wall following with simple memory:
- Remember when you've been somewhere
- Prefer unexplored paths
- Backtrack when stuck

## Files

| File | Description |
|------|-------------|
| `maze_runner_starter.py` | Starting template |
| `maze_runner_enhanced.py` | Enhanced wall follower |

## Enhancement Ideas

### Speed Improvements
- Increase speed on straightaways
- Look ahead to anticipate turns
- Use diagonal sensor readings

### Reliability Improvements
- Add stuck detection (no progress for X seconds)
- Implement recovery behaviors
- Handle dead ends gracefully

### Smart Navigation
- Remember visited cells (simple odometry grid)
- Detect loops (same place twice)
- Prefer right turns (biased wall following)

## Testing Strategy

1. **Module testing** - Test each behavior separately
2. **Integration testing** - Run complete maze logic in open space
3. **Simple maze** - Test with a simple 2-turn maze
4. **Full maze** - Graduated difficulty
5. **Speed runs** - Once reliable, optimize for speed

## Competition Format

### Practice Round (15 minutes)
- Tune your parameters
- Test in the actual maze
- Make final adjustments

### Official Runs
- 3 attempts per team
- Best time is recorded
- Teams run in random order

### Awards
- **Fastest Time** - Quickest successful run
- **Most Reliable** - Most consistent times
- **Best Recovery** - Best handling of stuck situations

## Hints

1. **Start conservative** - A slow completion beats a fast failure
2. **Test incrementally** - Don't change everything at once
3. **Watch the battery** - Performance varies with charge
4. **Print debug info** - Know what your robot is "thinking"
5. **Have a backup** - Keep a working version before experimenting

## Deliverables

1. Final `maze_runner.py` code
2. Video of successful maze run
3. Brief write-up of your approach and challenges

## Sample Code Structure

```python
class MazeRunner:
    def __init__(self, alvik):
        self.alvik = alvik
        self.state = 'START'
        self.start_time = None
        
    def run(self):
        self.start_time = time.time()
        
        while self.state != 'FINISHED':
            self.step()
            
        elapsed = time.time() - self.start_time
        print(f"Maze completed in {elapsed:.1f} seconds!")
        
    def step(self):
        sensors = self.read_sensors()
        
        if self.detect_goal(sensors):
            self.state = 'FINISHED'
            return
            
        # Your navigation logic here
        self.navigate(sensors)
```

## Good Luck!

Remember: The goal is to learn and have fun. Everyone who completes the maze is a winner!
