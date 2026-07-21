# CS-549 Robotics: Lecture Slides

## Slide Format

These slides are written in Markdown using [Marp](https://marp.app/) format. They can be:

1. **Presented directly** using Marp CLI or VS Code extension
2. **Converted to PowerPoint** using Marp CLI
3. **Converted to PDF** for handouts
4. **Viewed as HTML** in a browser

## Installing Marp

### Option 1: VS Code Extension (Recommended)
1. Install "Marp for VS Code" extension
2. Open any `.md` slide file
3. Click the Marp icon in the top right to preview
4. Export to PDF/PPTX from the command palette

### Option 2: Marp CLI
```bash
npm install -g @marp-team/marp-cli

# Convert to PDF
marp slides/01-course-overview.md -o slides/01-course-overview.pdf

# Convert to PowerPoint
marp slides/01-course-overview.md -o slides/01-course-overview.pptx

# Start presenter mode
marp slides/01-course-overview.md --preview
```

## Slide Files

### Day 1: Foundations & Path Planning
| File | Topic | Duration |
|------|-------|----------|
| `01-course-overview.md` | Course overview, robotics landscape | 30 min |
| `02-configuration-space.md` | Configuration space, obstacles | 60 min |
| `03-path-planning.md` | BFS, Dijkstra, A*, wavefront | 60 min |
| `04-robot-kinematics.md` | Differential drive, odometry | 45 min |
| `05-motor-control.md` | Motors, encoders, PID | 45 min |
| `06-intro-ros2.md` | ROS2 introduction | 30 min |

### Day 2: Sensing & Navigation
| File | Topic | Duration |
|------|-------|----------|
| `07-sensors-overview.md` | Sensor types, range sensing | 75 min |
| `08-maze-algorithms.md` | Wall follower, Pledge, flood fill | 45 min |
| `09-ros2-nav2.md` | Nav2, costmaps, SLAM concepts | 45 min |
| `10-trajectories.md` | Splines, smooth motion | 45 min |
| `11-advanced-topics.md` | SLAM, localization, where to go next | 30 min |

## Speaker Notes

Speaker notes are included in HTML comments below each slide:

```markdown
---

# Slide Title

Content here

<!-- 
NOTES:
- Key point to mention
- Demo to show
- Question to ask students
-->
```

## Customization

Edit the theme in the frontmatter of each file:

```yaml
---
marp: true
theme: default
paginate: true
---
```

Available themes: default, gaia, uncover
