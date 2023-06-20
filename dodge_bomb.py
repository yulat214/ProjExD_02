import sys
import pygame as pg

from random import randrange

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    
    # 練習問題3, こうかとん設定
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    bomb = pg.Surface((20, 20))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    bomb.set_colorkey((0, 0, 0))
    bomb_rct = bomb.get_rect()
    r_1, r_2 = (randrange(WIDTH), randrange(HEIGHT))
    bomb_rct.center = r_1, r_2

    vx = 5
    vy = 5
    
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        # 練習問題3, 移動量
        key_lst = pg.key.get_pressed()
        move_lst = [0, 0]
        if key_lst[pg.K_UP]: move_lst[1] -= 5
        if key_lst[pg.K_DOWN]: move_lst[1] += 5
        if key_lst[pg.K_LEFT]: move_lst[0] -= 5
        if key_lst[pg.K_RIGHT]: move_lst[0] += 5
            
        kk_rct.move_ip(move_lst)
        bomb_rct.move_ip(vx, vy)
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        
        screen.blit(bomb, bomb_rct)
        
        pg.display.update()
        tmr += 1
        # original -> clock.tick(10)
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()