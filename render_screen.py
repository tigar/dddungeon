import tcod

def render_screen(window, all_objects, dungeon_map, fov_map, fov_refresh, w_width, w_height, colors):
    # Draw the tiles
    if fov_refresh:
        for y in range(dungeon_map.height):
            for x in range(dungeon_map.width):
                wall = dungeon_map.tiles[x][y].block_sight
                
                if tcod.map_is_in_fov(fov_map, x, y):
                    if wall:
                        tcod.console_set_char_background(window, x, y, colors.get('light_wall'), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(window, x, y, colors.get('light_ground'), tcod.BKGND_SET)
                    dungeon_map.tiles[x][y].explored = True
                elif dungeon_map.tiles[x][y].explored:
                    if wall:
                        tcod.console_set_char_background(window, x, y, colors.get('dark_wall', tcod.BKGND_SET))
                    else:
                        tcod.console_set_char_background(window, x, y, colors.get('dark_ground', tcod.BKGND_SET))



    # Draw all the things
    for body in all_objects:
        draw_body(window, body, fov_map)
    tcod.console_blit(window, 0, 0, w_width, w_height, 0, 0, 0)

def clear_screen(window, all_objects):
    for body in all_objects:
        clear_body(window, body)

def draw_body(window, body, fov_map):
    if tcod.map_is_in_fov(fov_map, body.x, body.y):
        tcod.console_set_default_foreground(window, body.color)
        tcod.console_put_char(window, body.x, body.y, body.char, tcod.BKGND_NONE)

def clear_body(window, body):
    tcod.console_put_char(window, body.x, body.y, ' ', tcod.BKGND_NONE)