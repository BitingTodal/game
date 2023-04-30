import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from wall import Wall
from support import *



class Level:
    def __init__(self):

        
        
        #sprite group set up
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()
    
    def create_map(self):
        layout = {
            'boundary': import_csv_layout(r'C:\Users\gusta\Desktop\zelda_game_python/maps/export/map(0)_floor blocks.csv')
        }
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacles_sprites],'invisible')

         
        self.player = Player((704,704),[self.visible_sprites],self.obstacles_sprites)
                

                

    def run(self):
        #update and draw ze gameo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):


        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating floor
        self.floor_surf = pygame.image.load(r'C:\Users\gusta\Desktop\zelda_game_python/maps/map(0).png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (-1024,-1024))

    def custom_draw(self,player):

        #henter forskyvningen
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #tegne gulvet
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        #for Sprite in self.sprites():
        for Sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = Sprite.rect.topleft - self.offset
            self.display_surface.blit(Sprite.image,offset_pos)




        
   