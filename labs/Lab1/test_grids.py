"""
test_grids.py - Sample grids for testing path planning

Each grid is a 2D numpy array where:
- 0 = free space
- 1 = obstacle

Grids also include suggested start and goal positions.
"""

import numpy as np


def get_simple_grid():
    """
    A small 10x10 grid with one obstacle.
    Good for initial testing.
    
    Returns:
        grid: 2D numpy array
        start: (row, col) tuple
        goal: (row, col) tuple
    """
    grid = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    
    start = (1, 1)
    goal = (8, 8)
    
    return grid, start, goal


def get_medium_grid():
    """
    A 15x15 grid with multiple obstacles.
    Requires navigating around several barriers.
    
    Returns:
        grid: 2D numpy array
        start: (row, col) tuple
        goal: (row, col) tuple
    """
    grid = np.zeros((15, 15), dtype=int)
    
    # Obstacle 1: vertical wall
    grid[2:8, 4] = 1
    
    # Obstacle 2: horizontal wall
    grid[10, 2:10] = 1
    
    # Obstacle 3: block
    grid[5:8, 8:11] = 1
    
    # Obstacle 4: small block
    grid[2:4, 10:12] = 1
    
    start = (1, 1)
    goal = (13, 13)
    
    return grid, start, goal


def get_maze_grid():
    """
    A 16x16 maze-like grid.
    Requires finding a path through corridors.
    
    Returns:
        grid: 2D numpy array
        start: (row, col) tuple
        goal: (row, col) tuple
    """
    # This is the grid from the original course materials
    grid = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    
    start = (0, 0)
    goal = (14, 14)
    
    return grid, start, goal


def get_corridor_grid():
    """
    A grid with narrow corridors - tests tight navigation.
    
    Returns:
        grid: 2D numpy array
        start: (row, col) tuple
        goal: (row, col) tuple
    """
    grid = np.ones((12, 20), dtype=int)
    
    # Carve out corridors
    grid[1, 1:18] = 0
    grid[1:4, 17] = 0
    grid[3, 3:18] = 0
    grid[3:6, 3] = 0
    grid[5, 3:15] = 0
    grid[5:8, 14] = 0
    grid[7, 5:15] = 0
    grid[7:10, 5] = 0
    grid[9, 5:18] = 0
    grid[9:11, 17] = 0
    grid[10, 10:18] = 0
    
    start = (1, 1)
    goal = (10, 17)
    
    return grid, start, goal


def create_random_grid(rows, cols, obstacle_density=0.2, seed=None):
    """
    Create a random grid with specified obstacle density.
    
    Args:
        rows: Number of rows
        cols: Number of columns
        obstacle_density: Fraction of cells that are obstacles (0.0 to 1.0)
        seed: Random seed for reproducibility
    
    Returns:
        grid: 2D numpy array
        start: (row, col) tuple (top-left area)
        goal: (row, col) tuple (bottom-right area)
    """
    if seed is not None:
        np.random.seed(seed)
    
    grid = (np.random.random((rows, cols)) < obstacle_density).astype(int)
    
    # Ensure start and goal areas are clear
    start = (1, 1)
    goal = (rows - 2, cols - 2)
    
    # Clear area around start
    grid[0:3, 0:3] = 0
    
    # Clear area around goal
    grid[rows-3:rows, cols-3:cols] = 0
    
    return grid, start, goal


# Dictionary of all available grids for easy access
GRIDS = {
    'simple': get_simple_grid,
    'medium': get_medium_grid,
    'maze': get_maze_grid,
    'corridor': get_corridor_grid,
}


def list_grids():
    """Print available test grids."""
    print("Available test grids:")
    for name in GRIDS:
        grid, start, goal = GRIDS[name]()
        print(f"  {name}: {grid.shape[0]}x{grid.shape[1]}, start={start}, goal={goal}")


if __name__ == "__main__":
    # Demo: show all grids
    from grid_utils import print_grid, visualize_grid
    
    list_grids()
    print()
    
    for name in GRIDS:
        print(f"\n=== {name.upper()} GRID ===")
        grid, start, goal = GRIDS[name]()
        print_grid(grid, start=start, goal=goal)
