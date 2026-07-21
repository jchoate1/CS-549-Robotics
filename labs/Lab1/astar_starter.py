"""
Lab 1: A* Path Planning - Starter Code

Complete the TODO sections to implement:
1. Configuration space expansion
2. A* search algorithm

Run with: python astar_starter.py
Run with visualization: python astar_starter.py --visualize
"""

import numpy as np
import heapq
import argparse
from test_grids import get_simple_grid, get_medium_grid, get_maze_grid, GRIDS
from grid_utils import print_grid, visualize_grid, path_to_commands, save_commands


def expand_obstacles(grid, robot_radius_cells):
    """
    Expand obstacles to account for robot size (configuration space).
    
    The robot has a physical size. To plan paths treating the robot as a point,
    we "grow" the obstacles by the robot's radius.
    
    Args:
        grid: 2D numpy array (0 = free, 1 = obstacle)
        robot_radius_cells: Robot radius in grid cells
    
    Returns:
        expanded_grid: New grid with expanded obstacles
    
    Example:
        If robot_radius_cells = 1, a single obstacle cell should expand
        to a 3x3 block (1 cell in each direction).
    """
    rows, cols = grid.shape
    expanded = np.copy(grid)
    
    # TODO: Implement obstacle expansion
    #
    # Hint: For each obstacle cell in the original grid,
    # mark all cells within robot_radius_cells as obstacles
    # in the expanded grid.
    #
    # Be careful with boundary conditions!
    #
    # Your code here:
    
    pass  # Remove this line when you add your code
    
    return expanded


def heuristic(a, b):
    """
    Calculate heuristic distance between two points.
    
    We use Euclidean distance, which is admissible (never overestimates).
    
    Args:
        a: Tuple (row, col)
        b: Tuple (row, col)
    
    Returns:
        Estimated distance from a to b
    """
    # TODO: Implement Euclidean distance heuristic
    #
    # Hint: distance = sqrt((a[0]-b[0])^2 + (a[1]-b[1])^2)
    #
    # Your code here:
    
    pass  # Remove this line when you add your code


def get_neighbors(pos, grid, connectivity=4):
    """
    Get valid neighboring cells.
    
    Args:
        pos: Current position (row, col)
        grid: 2D numpy array
        connectivity: 4 (up/down/left/right) or 8 (include diagonals)
    
    Returns:
        List of (neighbor_pos, cost) tuples
    """
    rows, cols = grid.shape
    row, col = pos
    neighbors = []
    
    # 4-connectivity: up, down, left, right
    directions_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 8-connectivity: add diagonals
    directions_8 = directions_4 + [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    directions = directions_8 if connectivity == 8 else directions_4
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Check bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            # Check if not an obstacle
            if grid[new_row, new_col] == 0:
                # Cost is 1 for cardinal directions, sqrt(2) for diagonals
                cost = 1.414 if (dr != 0 and dc != 0) else 1.0
                neighbors.append(((new_row, new_col), cost))
    
    return neighbors


def reconstruct_path(came_from, current):
    """
    Reconstruct the path from start to goal.
    
    Args:
        came_from: Dictionary mapping each node to its parent
        current: The goal node
    
    Returns:
        List of (row, col) tuples from start to goal
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, goal, connectivity=4):
    """
    Find the shortest path from start to goal using A*.
    
    Args:
        grid: 2D numpy array (0 = free, 1 = obstacle)
        start: Starting position (row, col)
        goal: Goal position (row, col)
        connectivity: 4 or 8 for neighbor connectivity
    
    Returns:
        path: List of (row, col) tuples from start to goal, or None if no path
        explored: Set of all explored nodes (for visualization)
    """
    # Check if start or goal is blocked
    if grid[start[0], start[1]] == 1:
        print("Error: Start position is blocked!")
        return None, set()
    if grid[goal[0], goal[1]] == 1:
        print("Error: Goal position is blocked!")
        return None, set()
    
    # TODO: Implement A* search algorithm
    #
    # Data structures you'll need:
    # - open_set: Priority queue of nodes to explore (use heapq)
    #   Format: (f_score, counter, position) - counter breaks ties
    # - came_from: Dictionary mapping each node to its parent
    # - g_score: Dictionary mapping each node to its cost from start
    # - closed_set: Set of already explored nodes
    #
    # Algorithm:
    # 1. Initialize with start node
    # 2. While open_set is not empty:
    #    a. Pop node with lowest f_score
    #    b. If it's the goal, reconstruct and return path
    #    c. Add to closed_set
    #    d. For each neighbor:
    #       - Skip if in closed_set
    #       - Calculate tentative g_score
    #       - If better than known g_score, update and add to open_set
    # 3. If open_set is empty, no path exists
    #
    # Your code here:
    
    explored = set()  # Track explored nodes for visualization
    
    # Placeholder - remove when you implement
    print("TODO: Implement A* algorithm")
    return None, explored


def main():
    parser = argparse.ArgumentParser(description='A* Path Planning')
    parser.add_argument('--grid', choices=list(GRIDS.keys()), default='simple',
                        help='Which test grid to use')
    parser.add_argument('--visualize', action='store_true',
                        help='Show matplotlib visualization')
    parser.add_argument('--connectivity', type=int, choices=[4, 8], default=4,
                        help='Neighbor connectivity (4 or 8)')
    parser.add_argument('--robot-radius', type=int, default=0,
                        help='Robot radius in grid cells for C-space expansion')
    parser.add_argument('--save-commands', type=str, default=None,
                        help='Save robot commands to file')
    args = parser.parse_args()
    
    # Load the selected grid
    grid, start, goal = GRIDS[args.grid]()
    
    print(f"Grid: {args.grid} ({grid.shape[0]}x{grid.shape[1]})")
    print(f"Start: {start}, Goal: {goal}")
    print(f"Connectivity: {args.connectivity}")
    print()
    
    # Expand obstacles if robot radius specified
    if args.robot_radius > 0:
        print(f"Expanding obstacles by robot radius: {args.robot_radius} cells")
        grid = expand_obstacles(grid, args.robot_radius)
    
    # Show the grid
    print("Grid (S=start, G=goal, #=obstacle, .=free):")
    print_grid(grid, start=start, goal=goal)
    print()
    
    # Run A*
    print("Running A*...")
    path, explored = astar(grid, start, goal, connectivity=args.connectivity)
    
    if path:
        print(f"\nPath found! Length: {len(path)} steps")
        print("Path:", path)
        
        # Show path on grid
        print("\nGrid with path (*=path):")
        print_grid(grid, path=path, start=start, goal=goal)
        
        # Convert to robot commands
        commands = path_to_commands(path, cell_size_cm=10)
        print(f"\nRobot commands ({len(commands)} total):")
        for cmd in commands:
            print(f"  {cmd}")
        
        # Save commands if requested
        if args.save_commands:
            save_commands(commands, args.save_commands)
        
        # Visualize if requested
        if args.visualize:
            visualize_grid(grid, path=path, start=start, goal=goal,
                          explored=explored, title=f"A* Path - {args.grid} grid")
    else:
        print("\nNo path found!")
        
        if args.visualize:
            visualize_grid(grid, start=start, goal=goal,
                          explored=explored, title=f"A* - No Path Found - {args.grid} grid")


if __name__ == "__main__":
    main()
