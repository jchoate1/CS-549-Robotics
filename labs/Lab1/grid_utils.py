"""
grid_utils.py - Helper functions for grid visualization and manipulation

This module provides utilities for:
- Visualizing grids with obstacles, paths, and explored nodes
- Converting between grid coordinates and world coordinates
- Saving visualizations to files
"""

import numpy as np

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.colors import ListedColormap
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not installed. Visualization disabled.")
    print("Install with: pip install matplotlib")


def print_grid(grid, path=None, start=None, goal=None):
    """
    Print a text representation of the grid.
    
    Args:
        grid: 2D numpy array (0 = free, 1 = obstacle)
        path: List of (row, col) tuples representing the path
        start: (row, col) tuple for start position
        goal: (row, col) tuple for goal position
    """
    rows, cols = grid.shape
    path_set = set(path) if path else set()
    
    # Print column numbers
    print("   ", end="")
    for c in range(cols):
        print(f"{c % 10}", end="")
    print()
    
    for r in range(rows):
        print(f"{r:2d} ", end="")
        for c in range(cols):
            if start and (r, c) == start:
                print("S", end="")
            elif goal and (r, c) == goal:
                print("G", end="")
            elif (r, c) in path_set:
                print("*", end="")
            elif grid[r, c] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def visualize_grid(grid, path=None, start=None, goal=None, 
                   explored=None, title="Path Planning", 
                   save_path=None, show=True):
    """
    Create a matplotlib visualization of the grid.
    
    Args:
        grid: 2D numpy array (0 = free, 1 = obstacle)
        path: List of (row, col) tuples representing the path
        start: (row, col) tuple for start position
        goal: (row, col) tuple for goal position
        explored: Set of (row, col) tuples that were explored
        title: Title for the plot
        save_path: If provided, save the figure to this path
        show: If True, display the figure
    
    Returns:
        The matplotlib figure object
    """
    if not HAS_MATPLOTLIB:
        print("Matplotlib not available. Using text visualization:")
        print_grid(grid, path, start, goal)
        return None
    
    rows, cols = grid.shape
    
    fig, ax = plt.subplots(figsize=(max(8, cols * 0.5), max(6, rows * 0.5)))
    
    # Create a colored grid
    display_grid = np.zeros((rows, cols, 3))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:
                display_grid[r, c] = [0.2, 0.2, 0.2]  # Dark gray for obstacles
            else:
                display_grid[r, c] = [1, 1, 1]  # White for free space
    
    # Mark explored cells
    if explored:
        for (r, c) in explored:
            if grid[r, c] == 0:  # Only mark free cells
                display_grid[r, c] = [0.8, 0.9, 1.0]  # Light blue
    
    # Mark path
    if path:
        for (r, c) in path:
            display_grid[r, c] = [0.2, 0.6, 1.0]  # Blue
    
    # Mark start and goal
    if start:
        display_grid[start[0], start[1]] = [0, 0.8, 0]  # Green
    if goal:
        display_grid[goal[0], goal[1]] = [1, 0, 0]  # Red
    
    ax.imshow(display_grid, origin='upper')
    
    # Add grid lines
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
    
    # Add labels
    ax.set_xticks(np.arange(0, cols, max(1, cols // 10)))
    ax.set_yticks(np.arange(0, rows, max(1, rows // 10)))
    
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_title(title)
    
    # Add legend
    legend_elements = [
        patches.Patch(facecolor=[0.2, 0.2, 0.2], label='Obstacle'),
        patches.Patch(facecolor=[1, 1, 1], edgecolor='black', label='Free'),
        patches.Patch(facecolor=[0, 0.8, 0], label='Start'),
        patches.Patch(facecolor=[1, 0, 0], label='Goal'),
        patches.Patch(facecolor=[0.2, 0.6, 1.0], label='Path'),
    ]
    if explored:
        legend_elements.insert(2, patches.Patch(facecolor=[0.8, 0.9, 1.0], label='Explored'))
    
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved visualization to {save_path}")
    
    if show:
        plt.show()
    
    return fig


def path_to_commands(path, cell_size_cm=10):
    """
    Convert a path to robot movement commands.
    
    Args:
        path: List of (row, col) tuples
        cell_size_cm: Size of each grid cell in centimeters
    
    Returns:
        List of command strings like "move_forward(10)" or "turn_right()"
    """
    if not path or len(path) < 2:
        return []
    
    commands = []
    
    # Direction vectors: (delta_row, delta_col) -> direction name
    # Note: In grid coordinates, row increases downward
    directions = {
        (-1, 0): 'up',
        (1, 0): 'down',
        (0, -1): 'left',
        (0, 1): 'right',
    }
    
    # Turn mapping: (current_dir, target_dir) -> turn command
    turns = {
        ('up', 'right'): 'turn_right()',
        ('up', 'left'): 'turn_left()',
        ('up', 'down'): 'turn_right()\nturn_right()',
        ('down', 'right'): 'turn_left()',
        ('down', 'left'): 'turn_right()',
        ('down', 'up'): 'turn_right()\nturn_right()',
        ('left', 'up'): 'turn_right()',
        ('left', 'down'): 'turn_left()',
        ('left', 'right'): 'turn_right()\nturn_right()',
        ('right', 'up'): 'turn_left()',
        ('right', 'down'): 'turn_right()',
        ('right', 'left'): 'turn_right()\nturn_right()',
    }
    
    current_dir = None
    move_count = 0
    
    for i in range(1, len(path)):
        prev = path[i - 1]
        curr = path[i]
        
        delta = (curr[0] - prev[0], curr[1] - prev[1])
        new_dir = directions.get(delta)
        
        if new_dir is None:
            print(f"Warning: Invalid move from {prev} to {curr}")
            continue
        
        if current_dir is None:
            # First move - assume robot is facing this direction
            current_dir = new_dir
            move_count = 1
        elif new_dir == current_dir:
            # Continue in same direction
            move_count += 1
        else:
            # Direction change - output accumulated moves and turn
            if move_count > 0:
                commands.append(f"move_forward({move_count * cell_size_cm})")
            
            turn_cmd = turns.get((current_dir, new_dir), f"# Unknown turn: {current_dir} -> {new_dir}")
            for cmd in turn_cmd.split('\n'):
                commands.append(cmd)
            
            current_dir = new_dir
            move_count = 1
    
    # Output final moves
    if move_count > 0:
        commands.append(f"move_forward({move_count * cell_size_cm})")
    
    return commands


def save_commands(commands, filename):
    """Save robot commands to a file."""
    with open(filename, 'w') as f:
        f.write("# Robot commands generated by A* path planner\n")
        f.write("# Each command should be executed in sequence\n\n")
        for cmd in commands:
            f.write(cmd + "\n")
    print(f"Saved {len(commands)} commands to {filename}")
