from csv import reader

def import_csv_layout(path):
    terrain_map = []
    
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map



print(import_csv_layout(r'C:\Users\gusta\Desktop\zelda_game_python/maps/export/map(0)_floor blocks.csv'))