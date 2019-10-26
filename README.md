# Oiram
```
Totally not a clone of Mario

fell like making a level you self?
well it is farely simple, go into the levels folder and begin editing in one of the level images.

these are the factors that can be controlled:

    - the dimensions of the level
    - the background tiles
    - the enemies spawn position
    - the enemies direction
    - the pickups spawn position

the changes are done by changing the colours of the image, here is a overview of what the colour codes means and list of schematics

┌──────────────────────────────────────────────────────────┐
│                                                          │
│                  0100FF = Player spawn                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                    Background tiles                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                   --- description ---                    │
│                                                          │
│        sets the background tile to the given tile        │
│                                                          │
│                  --- colour codes ---                    │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │       Default level Tiles        │           │
│           └──────────────────────────────────┘           │
│                    FFFFFF = SKY                          │
│                    965C10 = DIRT                         │
│                    0FFF0F = GRASSDIRT                    │
│                    AF9A0C = BLOCK_PUSH                   │
│                    DBDBDB = STONE                        │
│                    329913 = GRASS                        │
│                    00FFFF = STONE_UNDERWORLD             │
│                    FFC549 = Bridge                       │
│                    FFC548 = Burned bridge                │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Castle               │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                    FF9900 = castle brick                 │
│                    FF9901 = castle 1                     │
│                    FF9902 = castle 2                     │
│                    FF9903 = castle 3                     │
│                    FF9904 = castle 4                     │
│                    FF9905 = castle 5                     │
│                    B78C35 = castle 6                     │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │            Map tiles             │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                    47B529 = BG                           │
│                    B7B7B7 = H_ROAD                       │
│                    B8B8B8 = V_ROAD                       │
│                                                          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                                                          │
│                     Entity spawns                        │
│                                                          │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                   --- description ---                    │
│                                                          │
│           spawns an entity at the given tile             │
│          and sets the background to a sky tile           │
│                                                          │
│                  --- colour codes ---                    │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Blocks               │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                    00000F = Powerup - Shroom             │
│                    02000F = Powerup - flower             │
│                    03000F = Powerup - empty              │
│                    04000F = Powerup - Star               │
│                    05000F = Sky - Shroom life +          │
│                    06000F = Sky- empty                   │
│                    00010F = Brick - breakable            │
│                    00020F = Brick - coin                 │
│                    006834 = Tube top                     │
│                    80D010 = Tube base                    │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Pickups              │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                    0200FF = Checkpoint                   │
│                    FFC700 = Star                         │
│                    000002 = Shroom                       │
│                    010002 = Shroom life+                 │
│                    FFFF00 = Coin                         │
│                    000005 = flower                       │
│                    FF0C29 = Spring                       │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Enemies              │           │
│           └──────────────────────────────────┘           │
│                   ┌────────────────┐                     │
│                   │   left going   │                     │
│                   └────────────────┘                     │
│                    000001 = Balumba                      │
│                    000003 = Legobro                      │
│                    00000A = Shelly                       │
│                    00000C = Flying Shelly                │
│                                                          │
│                   ┌────────────────┐                     │
│                   │  right going   │                     │
│                   └────────────────┘                     │
│                    010001 = Balumba                      │
│                    010003 = Legobro                      │
│                    01000A = Shelly                       │
│                    01000C = Flying Shelly                │
│                                                          │
│                   ┌────────────────┐                     │
│                   │  interceptors  │                     │
│                   └────────────────┘                     │
│                                                          │
│                    000008 = Fire ghost                   │
│                    00000B = Plant                        │
│                                                          │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                     Schematic list                       │
│                                                          │
└──────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                   --- description ---                    │
│                                                          │
│              List of preprepaired segments               │
│           can be seen in the schematics folder           │
│                                                          │
│                   --- schematics ---                     │
│                                                          │
│ ┌──────────────────────────────────────────────────────┐ │
│                                                          │
│        name: "Ending_1.png"                              │
│        creator: mart368b                                 │
│        description: default ending of a level            │
│                                                          │
│ └──────────────────────────────────────────────────────┘ │
│                                                          │
│ ┌──────────────────────────────────────────────────────┐ │
│                                                          │
│        name: "Ghost_Intercept.png"                       │
│        creator: mart368b                                 │
│        description: basic fire ghost interceptor         │
│                                                          │
│ └──────────────────────────────────────────────────────┘ │
│                                                          │
└──────────────────────────────────────────────────────────┘
```