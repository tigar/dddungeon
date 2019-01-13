import tcod

def make_fov_map(dungeon_map):
    fov_map = tcod.map_new(dungeon_map.width, dungeon_map.height)

    for y in range(dungeon_map.height):
        for x in range(dungeon_map.width):
            tcod.map_set_properties(fov_map, x, y, not dungeon_map.tiles[x][y].block_sight, not dungeon_map.tiles[x][y].blocked)

    return fov_map

def refresh_fov(fov_map, x, y, radius, light_walls=True, algorithm=0):
    tcod.map_compute_fov(fov_map, x, y, radius, light_walls, algorithm)
