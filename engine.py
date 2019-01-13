import tcod
from body import Body
from inputs import handle_keys
from fov import make_fov_map, refresh_fov
from map_objects.dungeon_map import DungeonMap
from render_screen import clear_screen, render_screen


def main():
    w_width = 80
    w_height = 50
    map_width = 80
    map_height = 45
    min_rooms = 20
    max_rooms = 30
    room_max_size = 10
    room_min_size = 6

    fov_algorithm = 0 
    fov_light_walls = True
    fov_radius = 10

    fov_refresh = True


    colors = {
        'dark_wall': tcod.Color(0, 0, 100),
        'dark_ground': tcod.Color(50, 50, 150),
        'light_wall': tcod.Color(130, 110, 50),
        'light_ground': tcod.Color(200, 180, 50)
    }

    player = Body(int(w_width/2), int(w_height/2), '@', tcod.white)
    npc = Body(int(w_width/2 - 5), int(w_height/2 - 5), '@', tcod.yellow)
    all_objects = [npc, player]

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    tcod.console_init_root(w_width, w_height, 'welcome to the dddungeon', False)
    
    window = tcod.console_new(w_width, w_height)

    dungeon_map = DungeonMap(map_width, map_height)
    dungeon_map.make_map(min_rooms, max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    
    fov_map = make_fov_map(dungeon_map)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        if fov_refresh:
            refresh_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_screen(window, all_objects, dungeon_map, fov_map, fov_refresh, w_width, w_height, colors)
        fov_refresh = False
        
        tcod.console_flush()

        clear_screen(window, all_objects)

        action = handle_keys(key)
        move = action.get('move')
        quitgame = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            new_x, new_y = move
            if not dungeon_map.is_blocked(player.x + new_x, player.y + new_y):
                player.move(new_x, new_y)
                fov_refresh = True

        if quitgame:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == '__main__':
    main()