---
marp: true
theme: default
paginate: true
header: 'CS-549 Robotics'
footer: 'Day 1 | Path Planning Algorithms'
math: mathjax
---

# Path Planning Algorithms
## Finding the Way

---

# The Path Planning Problem

**Given:**
- Configuration space (grid with obstacles)
- Start configuration
- Goal configuration

**Find:**
- A sequence of configurations from start to goal
- All configurations must be in free space
- (Ideally) Optimal path (shortest distance)

<!-- 
NOTES:
- We've built the C-space, now we need to search it
- Graph search algorithms are the key
- Grid cells are nodes, movements are edges
-->

---

# Representation Choices

Different representations for different problems:

| Representation | Good For | Cost |
|----------------|----------|------|
| **Grid** | Global planning, complete | Memory, coarse |
| **Waypoints** | Compact storage, execution | Loses detail |
| **Splines** | Smooth curves, trajectories | Computation |
| **Reactive rules** | Fast response, simple | No global view |

**Key insight**: Each is a tool with tradeoffs.
We use grids for planning, then convert to waypoints for execution.

<!-- 
NOTES:
- This framing helps students see the big picture
- Labs 1-5 use different representations
- Real robots combine multiple representations
-->

---

# Graph Search Basics

Think of the grid as a graph:
- **Nodes**: Grid cells
- **Edges**: Valid movements between adjacent cells
- **Edge weights**: Cost of movement (usually 1 or √2)

Path planning = Graph search from start to goal

<!-- 
NOTES:
- If students haven't seen graph algorithms, brief intro
- Classic CS problem with many solutions
- We'll cover several approaches
-->

---

# Algorithm 1: Breadth-First Search (BFS)

Explore all nodes at distance $d$ before distance $d+1$

```
1. Add start to queue
2. While queue not empty:
   a. Remove first node from queue
   b. If it's the goal, done!
   c. Add all unvisited neighbors to queue
   d. Mark current as visited
```

<!-- 
NOTES:
- Simplest complete algorithm
- Guaranteed to find shortest path (in # of steps)
- Uses a FIFO queue
- Explores in expanding "wavefront"
-->

---

# BFS Visualization

```
Step 0:    Step 1:    Step 2:    Step 3:
S . . .    S 1 . .    S 1 2 .    S 1 2 3
. . . .    1 1 . .    1 1 2 .    1 1 2 3
. . . .    . . . .    1 1 . .    1 1 2 .
. . . G    . . . G    . . . G    1 1 . G
```

Numbers show distance from start (S)

<!-- 
NOTES:
- Draw this progression on the board
- Show how it expands uniformly
- Will eventually reach G
-->

---

# BFS Properties

| Property | Value |
|----------|-------|
| Complete? | Yes (finds path if one exists) |
| Optimal? | Yes (for uniform costs) |
| Time complexity | O(V + E) |
| Space complexity | O(V) |

where V = vertices (cells), E = edges (connections)

<!-- 
NOTES:
- Complete and optimal are important guarantees
- But explores many unnecessary nodes
- Can we do better?
-->

---

# Algorithm 2: Dijkstra's Algorithm

Like BFS, but handles **weighted edges**

```
1. Add start to priority queue with cost 0
2. While queue not empty:
   a. Remove node with LOWEST cost
   b. If it's the goal, done!
   c. For each neighbor:
      - Calculate cost through current node
      - If better than known cost, update and add to queue
```

<!-- 
NOTES:
- Priority queue instead of FIFO queue
- Always expands lowest-cost node first
- Handles different edge weights (diagonal = √2)
-->

---

# Dijkstra Visualization

```
Costs:       Priority Queue:
S . . .      [(0, S)]
. # . .      [(1, A), (1, B)]  after expanding S
. . . G      [(1, B), (2, C)]  after expanding A
             ...

     1    1
  S --- A --- C
  |     |     |
  1     #     1
  |           |
  B --------- G
       3
```

<!-- 
NOTES:
- Draw a weighted graph example
- Show how it always picks the lowest cost
- Guarantees optimal path
-->

---

# Problem with BFS/Dijkstra

They explore **uniformly in all directions**

Even if the goal is to the right, they explore left too!

Can we be smarter?

<!-- 
NOTES:
- Transition to heuristic search
- We have information about where the goal is
- Should use it!
-->

---

# Algorithm 3: A* Search

**Key idea**: Use a **heuristic** to guide the search toward the goal

$$f(n) = g(n) + h(n)$$

- $g(n)$ = actual cost from start to $n$
- $h(n)$ = **estimated** cost from $n$ to goal
- $f(n)$ = estimated total cost through $n$

<!-- 
NOTES:
- A* is the most important algorithm we'll cover
- Combines best of Dijkstra (optimal) and greedy (fast)
- The heuristic h(n) is key
-->

---

# The Heuristic Function

$h(n)$ estimates the cost from $n$ to goal

**Must be admissible**: Never overestimate!

Common choices:
- **Euclidean distance**: $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- **Manhattan distance**: $|x_2-x_1| + |y_2-y_1|$

<!-- 
NOTES:
- Admissible = optimistic estimate
- Euclidean: straight-line distance (always ≤ actual)
- Manhattan: for 4-connectivity grids
- If h(n) = 0, A* becomes Dijkstra
-->

---

# A* Algorithm

```python
def astar(grid, start, goal):
    open_set = PriorityQueue()
    open_set.add(start, f=h(start, goal))
    
    g_score = {start: 0}
    came_from = {}
    
    while not open_set.empty():
        current = open_set.pop()  # lowest f-score
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + cost(current, neighbor)
            
            if tentative_g < g_score.get(neighbor, inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + h(neighbor, goal)
                open_set.add(neighbor, f)
    
    return None  # No path
```

<!-- 
NOTES:
- This is the core algorithm students will implement
- Key difference from Dijkstra: f = g + h instead of just g
- Priority queue ordered by f-score
-->

---

# A* Visualization

```
     S → → → → G
     ↓   #     ↑
     ↓   #     ↑
     → → → → → ↑
     
BFS explores:     A* explores:
everywhere!       toward goal
```

A* expands far fewer nodes while still finding optimal path

<!-- 
NOTES:
- Draw comparison on board
- Show how A* heads toward the goal
- Still guaranteed optimal with admissible heuristic
-->

---

# A* Properties

| Property | Value |
|----------|-------|
| Complete? | Yes |
| Optimal? | Yes (with admissible heuristic) |
| Time complexity | O(b^d) worst case |
| Space complexity | O(b^d) |

In practice, much faster than BFS/Dijkstra for most maps

<!-- 
NOTES:
- b = branching factor, d = depth of solution
- Heuristic quality affects performance
- Better heuristic = fewer nodes expanded
-->

---

# Algorithm 4: Wavefront Planning

Also called "Brushfire" or "Distance Transform"

1. Start from goal, mark it as 0
2. Mark all free neighbors as 1
3. Mark their free neighbors as 2
4. Continue until reaching start
5. Follow decreasing numbers from start to goal

<!-- 
NOTES:
- Alternative to A* - builds entire distance field
- Useful when you need to plan from multiple starts
- Similar to BFS but from goal backward
-->

---

# Wavefront Example

```
Step 1:    Step 2:    Step 3:    Final:
. . . .    . . . .    . . . 3    4 5 4 3
. # . .    . # . .    . # 2 2    5 # 3 2
. # . 0    . # 1 0    . # 1 0    6 # 1 0
. . . .    . . 1 .    . 2 1 .    7 2 1 .
                                   S     G
Path: 7→6→5→4→3→2→1→0
```

<!-- 
NOTES:
- Draw step by step
- Once field is built, path is trivial to find
- Good for games/situations with fixed goal
-->

---

# Comparing Algorithms

| Algorithm | Use Case |
|-----------|----------|
| BFS | Unweighted, uniform cost |
| Dijkstra | Weighted edges, no heuristic |
| A* | Weighted, with good heuristic |
| Wavefront | Pre-compute distances to goal |

**For this course**: A* is our primary algorithm

<!-- 
NOTES:
- A* is the workhorse of robotics path planning
- Wavefront useful in specific cases
- Both are complete and optimal
-->

---

# Beyond A*: Incremental Replanning

What if the world changes while you're navigating?

**LPA*** (Lifelong Planning A*):
- Reuses previous search when map changes
- Only updates affected areas

**D* Lite**:
- Plans from goal to robot (like wavefront)
- Efficiently repairs path as obstacles appear

Real robots discover new obstacles → need to replan fast!

*Beyond our scope, but know these exist.*

<!-- 
NOTES:
- A* replans from scratch each time
- LPA* and D* Lite are smarter about reuse
- Mars rovers use D* variants
- Mention for completeness, don't implement
-->

---

# Implementation Tips

1. **Priority Queue**: Use `heapq` in Python
   ```python
   import heapq
   heapq.heappush(queue, (priority, item))
   priority, item = heapq.heappop(queue)
   ```

2. **Tie-breaking**: Add counter to avoid comparing positions
   ```python
   heapq.heappush(queue, (f_score, counter, position))
   ```

3. **Closed set**: Use a `set()` for O(1) lookup

<!-- 
NOTES:
- Common implementation pitfalls
- Heapq doesn't handle ties well without counter
- Set is much faster than list for "visited" check
-->

---

# Path Reconstruction

Once goal is reached, trace back through `came_from`:

```python
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
```

<!-- 
NOTES:
- came_from maps each node to its parent
- Walk backward from goal to start
- Reverse to get start-to-goal order
-->

---

# Lab 1: Your Task

Implement A* to find paths through grids:

1. **Configuration space expansion** ✓ (covered)
2. **Heuristic function** (Euclidean distance)
3. **A* search algorithm**
4. **Path output** (convert to robot commands)

Test grids provided: simple, medium, maze

<!-- 
NOTES:
- Students should now have enough background
- Encourage them to start with the simple grid
- Visualization helps debugging
-->

---

# Demo: A* in Action

Let's run the solution on different grids:

```bash
python astar_solution.py --grid simple --visualize
python astar_solution.py --grid maze --visualize
```

<!-- 
NOTES:
- Live demo if possible
- Show explored nodes (blue) vs path (dark blue)
- Show how A* focuses toward the goal
-->

---

# Summary

1. **BFS**: Simple, complete, explores uniformly
2. **Dijkstra**: Handles weights, still uniform
3. **A***: Uses heuristic to guide search efficiently
4. **Wavefront**: Pre-computes distance field

**Key formula**: $f(n) = g(n) + h(n)$

**Key requirement**: Heuristic must be admissible

<!-- 
NOTES:
- Make sure A* formula is understood
- Admissibility is crucial for optimality
- Questions before lab?
-->

---

# Lab 1 Time!

Work on Lab 1: A* Path Planning

- Implement `expand_obstacles()`
- Implement `heuristic()`
- Implement `astar()`

Ask for help if you get stuck!

<!-- 
NOTES:
- Allocate ~60-90 minutes for the lab
- Walk around and help students
- Common issues: bounds checking, priority queue ties
-->
