# Physical Maze Construction Guide

This guide provides instructions for building the physical maze used in Labs 4 and 5.

## Design Requirements

| Parameter | Value | Reason |
|-----------|-------|--------|
| Overall size | 100cm × 100cm | Fits on a table or floor space |
| Wall height | 15-20cm | Taller than Alvik sensor (~10cm) |
| Path width | 15-20cm | Alvik is ~10cm wide, need clearance |
| Wall thickness | 1-2cm | Sturdy but not space-consuming |

## Materials Options

### Option 1: Foam Board (Recommended for Portability)

**Materials:**
- 4-6 sheets of foam board (20" × 30" or similar)
- Hot glue gun and glue sticks
- Box cutter or craft knife
- Ruler and pencil
- Duct tape (for reinforcement)

**Pros:** Lightweight, easy to cut, inexpensive
**Cons:** Less durable, can tip over

**Cost estimate:** $20-30

### Option 2: Cardboard (Budget Option)

**Materials:**
- Large cardboard boxes (appliance boxes work great)
- Box cutter
- Packing tape
- Weights or tape to secure to floor

**Pros:** Free/very cheap, easy to modify
**Cons:** Not durable, can collapse

**Cost estimate:** $0-10

### Option 3: Wood (Most Durable)

**Materials:**
- 1/4" plywood sheet (4' × 8')
- 1×4 lumber for wall supports
- Wood screws
- Wood glue
- Paint (optional)

**Pros:** Very durable, reusable for years
**Cons:** Heavier, requires tools, more expensive

**Cost estimate:** $50-80

### Option 4: PVC Pipe Frame with Fabric

**Materials:**
- 1/2" PVC pipes
- PVC connectors (elbows, tees)
- Dark fabric or felt
- Zip ties

**Pros:** Modular, reconfigurable, lightweight
**Cons:** Walls may flex, more complex assembly

**Cost estimate:** $40-60

## Recommended Design: Foam Board Maze

### Cut List

| Piece | Dimensions | Quantity | Purpose |
|-------|------------|----------|---------|
| Base (optional) | 100cm × 100cm | 1 | Foundation |
| Outer walls | 100cm × 18cm | 4 | Perimeter |
| Long internal | 40cm × 18cm | 2-3 | Internal walls |
| Short internal | 25cm × 18cm | 2-3 | Internal walls |
| Supports | 10cm × 18cm | 8-10 | Wall feet |

### Assembly Instructions

#### Step 1: Prepare the Base
- Use a large piece of cardboard, plywood, or work directly on the floor
- Mark the 100cm × 100cm perimeter with tape

#### Step 2: Cut Outer Walls
```
Cut 4 pieces: 100cm × 18cm

For entrance gap (south wall):
- Cut into two pieces: 35cm and 35cm
- Leave 30cm gap in the middle for entrance

For exit gap (west wall):
- Cut into two pieces: 40cm and 40cm  
- Leave 20cm gap for exit
```

#### Step 3: Create Wall Supports
```
Cut L-shaped supports from foam board:
    ┌────┐
    │    │ 18cm
    │    │
    └────┴────┐
         10cm │ 10cm
              │
              └────
              
Glue to bottom of each wall section
```

#### Step 4: Assemble Outer Walls
1. Place outer walls on the base/floor
2. Use hot glue at corners
3. Add supports at each corner and every 30cm

#### Step 5: Add Internal Walls
```
Suggested maze layout (view from above):

    ┌─────────────────────┐
    │                     │
    │    ┌─────┐          │
    │    │     │    EXIT  │
    │    │     └─────     │
    │    │          │     │
    │    └──────────┘     │
    │                     │
    │ ENTRANCE            │
    └──────   ────────────┘
    
Internal walls create at least 2 turns
but should be solvable with wall-following
```

#### Step 6: Secure to Floor
- Use painter's tape to secure base to floor
- Or add weights inside wall supports

## Maze Layout Options

### Layout 1: Simple (2-3 turns)
Good for initial testing

```
┌────────────────────┐
│                    │
│   ┌────────────┐   │
│   │            │ E │
│   │   ┌────┐   X   │
│   │   │    │   I   │
│   │   │    │   T   │
│   └───┘    └───────┤
│                    │
│  ENTRANCE          │
└────────  ──────────┘
```

### Layout 2: Medium (4-5 turns)
Good for the competition

```
┌────────────────────┐
│        │           │
│   ┌────┘   ┌───┐   │
│   │        │   │ E │
│   │   ┌────┤   │ X │
│   │   │    │   │ I │
│   └───┤    └───┘ T │
│       │            │
│  ENTRANCE          │
└────────  ──────────┘
```

### Layout 3: Challenging
For advanced students

```
┌────────────────────┐
│   │       │        │
│   │   ┌───┘   ┌──┐ │
│   │   │       │  │E│
│   └───┤   ┌───┘  │X│
│       │   │      │I│
│   ┌───┴───┤   ┌──┘T│
│   │       │   │    │
│   │  ENTRANCE      │
└───┴────  ──────────┘
```

## Tips for Success

### Stability
- Wider bases = more stable walls
- Consider weighting the bottom of walls with coins or washers
- Secure outer walls to each other at corners

### Sensor Compatibility
- Walls must be detectable by ToF sensor
- Avoid glossy/reflective surfaces (can confuse sensor)
- Matte surfaces work best

### Adjustability
- Don't glue internal walls initially
- Test with robot first
- Adjust path width if robot has trouble

### Line Following Track (Optional)
- Add black electrical tape line from entrance to exit
- Use white poster board as base
- Good for testing line sensors

## Start and Goal Markers

### Start Position
- Mark with green tape or paper
- Robot front wheels should touch this line
- Clear view into maze entrance

### Goal Position
- Mark with red tape or paper
- Large enough for robot to clearly enter
- Consider adding a "finish line" to detect completion

## Pre-Course Checklist

- [ ] All walls cut to size
- [ ] Supports attached to walls
- [ ] Outer walls assembled
- [ ] Internal walls positioned (not glued)
- [ ] Maze tested with robot
- [ ] Start marker placed
- [ ] Goal marker placed
- [ ] Maze secured to floor
- [ ] Extra tape/glue available for repairs
- [ ] Backup wall pieces ready

## Troubleshooting

**Robot knocks over walls:**
- Add more weight to wall bases
- Widen supports
- Tape walls to floor

**Robot can't detect walls:**
- Check wall height (must be above sensor level)
- Avoid shiny materials
- Test sensor readings in maze

**Path too narrow:**
- Remove/reposition internal walls
- Increase gap at entrance/exit

**Robot gets stuck in corners:**
- Round internal corners slightly
- Increase path width at turns
