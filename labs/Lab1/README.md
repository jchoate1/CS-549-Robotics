# Lab 1: Path Planning with A*

## Objectives

1. Understand configuration space and obstacle expansion
2. Implement the A* path planning algorithm
3. Generate a path through a grid with obstacles
4. Visualize the planning process and solution

## Background

### Configuration Space

When planning paths for a robot, we need to account for the robot's physical size. **Configuration space** (C-space) transforms the problem by "growing" obstacles by the robot's radius, allowing us to then treat the robot as a point.

For example, if your robot is 10cm wide and an obstacle is a 20cm x 20cm box, in configuration space that obstacle becomes a 30cm x 30cm box (original size + robot radius on each side).

### A* Algorithm

A* is a best-first search algorithm that finds the shortest path between a start and goal. It uses:

- **g(n)**: Cost from start to node n
- **h(n)**: Heuristic estimate from n to goal (we'll use Euclidean distance)
- **f(n) = g(n) + h(n)**: Total estimated cost

A* expands the node with the lowest f(n) value first, guaranteeing an optimal path when using an admissible heuristic.

```
OPEN = priority queue containing start node
CLOSED = empty set

while OPEN is not empty:
    current = node in OPEN with lowest f(n)
    
    if current is goal:
        return reconstruct_path(current)
    
    move current from OPEN to CLOSED
    
    for each neighbor of current:
        if neighbor in CLOSED:
            continue
        
        tentative_g = g(current) + cost(current, neighbor)
        
        if neighbor not in OPEN or tentative_g < g(neighbor):
            set parent of neighbor to current
            g(neighbor) = tentative_g
            f(neighbor) = g(neighbor) + h(neighbor)
            
            if neighbor not in OPEN:
                add neighbor to OPEN

return failure (no path exists)
```

## Assignment

### Part 1: Configuration Space Expansion

Complete the `expand_obstacles()` function in `astar_starter.py`. Given a grid and robot radius, expand all obstacles to account for the robot's size.

### Part 2: A* Implementation

Complete the `astar()` function to find a path from start to goal. Your implementation should:

1. Use a priority queue (heapq) for the open set
2. Track visited nodes to avoid revisiting
3. Use Euclidean distance as the heuristic
4. Support 4-connectivity (up, down, left, right) or 8-connectivity (diagonals too)
5. Return the path as a list of (row, col) tuples

### Part 3: Path Output

Generate output suitable for the Alvik robot (Lab 2). Convert your path into a sequence of commands:
- `move_forward(distance)`
- `turn_left()` or `turn_right()`

## Files

| File | Description |
|------|-------------|
| `astar_starter.py` | Your starting point - fill in the TODOs |
| `grid_utils.py` | Helper functions for visualization |
| `test_grids.py` | Sample grids to test your implementation |

## Running the Code

```bash
# Install dependencies (if needed)
pip install numpy matplotlib

# Run your implementation
python astar_starter.py

# Run with visualization
python astar_starter.py --visualize
```

## Test Grids

Three test grids are provided in `test_grids.py`:

1. **Simple**: Small grid with one obstacle
2. **Medium**: Larger grid with multiple obstacles  
3. **Maze**: Grid requiring navigation through corridors

## Deliverables

1. Completed `astar_starter.py` with working A* implementation
2. Screenshot or saved image of your path visualization
3. Output file with robot commands for one grid

## Hints

- Start with the simple grid to test your logic
- Use `heapq` for an efficient priority queue
- Remember: grid coordinates are (row, col), not (x, y)
- Draw your path on paper first if you're stuck
- The heuristic must never overestimate the true cost (admissibility)

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Configuration space expansion works correctly | 20 |
| A* finds valid paths | 30 |
| A* finds optimal (shortest) paths | 20 |
| Path output in robot command format | 15 |
| Code quality and documentation | 15 |
| **Total** | **100** |

## Resources

- [A* Pathfinding for Beginners](https://www.redblobgames.com/pathfinding/a-star/introduction.html) - Excellent visual tutorial
- [A* Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- LaValle, Planning Algorithms, Chapter 2
