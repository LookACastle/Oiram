﻿# Oiram
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
│                                                          │
│                0x0100FF = Player spawn                   │
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
│                  0xFFFFFF = SKY                          │
│                  0x965C10 = DIRT                         │
│                  0x0FFF0F = GRASSDIRT                    │
│                  0xAF9A0C = BLOCK_PUSH                   │
│                  0xDBDBDB = STONE                        │
│                  0x329913 = GRASS                        │
│                  0x00FFFF = STONE_UNDERWORLD             │
│                  0xFFC549 = Bridge                       │
│                  0xFFC548 = Burned bridge                │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Castle               │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                  0x0099FF = Castle brick                 │
│                  0x0199FF = CASTLE_1                     │
│                  0x0299FF = CASTLE_2                     │
│                  0x0399FF = CASTLE_3                     │
│                  0x0499FF = CASTLE_4                     │
│                  0x0599FF = CASTLE_5                     │
│                  0x0699FF = CASTLE_6                     │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │            Map tiles             │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                  0x47B529 = BG                           │
│                  0xB7B7B7 = H_ROAD                       │
│                  0xB8B8B8 = V_ROAD                       │
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
│                  0x00000F = Powerup - Shroom             │
│                  0x02000F = Powerup - flower             │
│                  0x03000F = Powerup - empty              │
│                  0x04000F = Powerup - Star               │
│                  0x05000F = Sky - Shroom life +          │
│                  0x06000F = Sky- empty                   │
│                  0x00010F = Brick - breakable            │
│                  0x00020F = Brick - coin                 │
│                  0x006834 = Tube top                     │
│                  0x80D010 = Tube base                    │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Pickups              │           │
│           └──────────────────────────────────┘           │
│                                                          │
│                  0x0200FF = Checkpoint                   │
│                  0xFFC700 = Star                         │
│                  0x000002 = Shroom                       │
│                  0x010002 = Shroom life+                 │
│                  0xFFFF00 = Coin                         │
│                  0x000005 = flower                       │
│                                                          │
│           ┌──────────────────────────────────┐           │
│           │             Enemies              │           │
│           └──────────────────────────────────┘           │
│                   ┌────────────────┐                     │
│                   │   left going   │                     │
│                   └────────────────┘                     │
│                  0x000001 = Balumba                      │
│                  0x000003 = Legobro                      │
│                                                          │
│                   ┌────────────────┐                     │
│                   │  right going   │                     │
│                   └────────────────┘                     │
│                  0x010001 = Balumba                      │
│                  0x010003 = Legobro                      │
│                                                          │
│                   ┌────────────────┐                     │
│                   │  interceptors  │                     │
│                   └────────────────┘                     │
│                                                          │
│                  0x000008 = Fire ghost                   │
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

