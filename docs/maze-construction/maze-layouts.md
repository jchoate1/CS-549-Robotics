# Maze Layout Diagrams

Printable maze layouts for the CS-549 course. Each grid square represents 10cm.

## Layout 1: Beginner (2 turns)

Use this for initial testing and Lab 4 practice.

```
Grid: 10×10 (100cm × 100cm)
S = Start, G = Goal, # = Wall

    0 1 2 3 4 5 6 7 8 9
   ┌─────────────────────┐
 0 │ # # # # # # # # # # │
 1 │ #                 # │
 2 │ #   # # # # # #   # │
 3 │ #   #           G   │
 4 │ #   #   # # # # # # │
 5 │ #   #           # # │
 6 │ #   # # # # #   # # │
 7 │ #               # # │
 8 │ #   S           # # │
 9 │ # #     # # # # # # │
   └─────────────────────┘

Path: S → up → right → up → right → down → G
Turns: 4 (but simple layout)
```

### Wall Segments for Layout 1

| Wall | Start | End | Length |
|------|-------|-----|--------|
| Top outer | (0,0) | (0,9) | 100cm |
| Bottom outer left | (9,0) | (9,3) | 40cm |
| Bottom outer right | (9,5) | (9,9) | 50cm |
| Left outer | (0,0) | (9,0) | 100cm |
| Right outer | (0,9) | (8,9) | 90cm |
| Internal 1 | (2,2) | (2,7) | 60cm |
| Internal 2 | (2,2) | (6,2) | 50cm |
| Internal 3 | (4,4) | (4,9) | 60cm |
| Internal 4 | (6,4) | (6,7) | 40cm |

---

## Layout 2: Intermediate (4-5 turns)

Recommended for Lab 5 competition.

```
Grid: 10×10 (100cm × 100cm)

    0 1 2 3 4 5 6 7 8 9
   ┌─────────────────────┐
 0 │ # # # # # # # # # # │
 1 │ #       #         # │
 2 │ #   # # #   # #   # │
 3 │ #   #       # # G   │
 4 │ #   #   # # # # # # │
 5 │ #   #   #         # │
 6 │ #   # # #   # # # # │
 7 │ #           #     # │
 8 │ #   S       #     # │
 9 │ # #     # # # # # # │
   └─────────────────────┘

Right-hand wall following path:
S → up → up → right → right → up → up → left → left → down → G
```

---

## Layout 3: Advanced (Multiple paths)

For students who finish early or want a challenge.

```
Grid: 10×10 (100cm × 100cm)

    0 1 2 3 4 5 6 7 8 9
   ┌─────────────────────┐
 0 │ # # # # # # # # # # │
 1 │ #     #     #     # │
 2 │ # # # #   # # #   # │
 3 │ #         #     G   │
 4 │ #   # # # #   # # # │
 5 │ #   #     #       # │
 6 │ #   #   # # # #   # │
 7 │ #   #         #   # │
 8 │ #   S   # #   #   # │
 9 │ # #     # # # # # # │
   └─────────────────────┘

Multiple valid paths exist.
Right-hand following will work but not optimal.
```

---

## Competition Maze (Final Layout)

Reveal this only during the competition.

```
Grid: 10×10 (100cm × 100cm)

    0 1 2 3 4 5 6 7 8 9
   ┌─────────────────────┐
 0 │ # # # # # # # # # # │
 1 │ #       # #       # │
 2 │ # # #       # # # # │
 3 │ #     # #       G   │
 4 │ #   # # # # #   # # │
 5 │ #   #           # # │
 6 │ # # #   # # # # # # │
 7 │ #       #         # │
 8 │ #   S   #         # │
 9 │ # #     # # # # # # │
   └─────────────────────┘

Estimated completion time:
- Beginner: 60-90 seconds
- Good solution: 30-45 seconds  
- Optimal: 20-30 seconds
```

---

## Modular Wall Pieces

For flexible maze reconfiguration:

### Standard Pieces (cut multiples)

| Piece | Size | Quantity Needed |
|-------|------|-----------------|
| Long wall | 40cm × 18cm | 6 |
| Medium wall | 30cm × 18cm | 4 |
| Short wall | 20cm × 18cm | 6 |
| Corner (L) | 20cm × 20cm × 18cm | 4 |

### Assembly Tips

1. Use velcro strips on wall bottoms for repositioning
2. Mark floor with grid (masking tape) for alignment
3. Keep walls perpendicular for consistent sensor readings

---

## Testing Your Maze

Before the course:

1. **Robot fit test**: Can the robot navigate the narrowest path?
2. **Sensor test**: Can sensors detect all walls?
3. **Corner test**: Can robot turn in corners without collision?
4. **Dead end test**: Can robot recover from dead ends?
5. **Full run**: Does wall-following reach the goal?

Adjust wall positions as needed based on testing.
