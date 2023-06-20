import sys
import pygame as pg

from random import randrange

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    
    # 以下練習問題1, 設定
    bomb = pg.Surface((20, 20))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    bomb.set_colorkey((0, 0, 0))
    bomb_rct = bomb.get_rect()
    r_1, r_2 = (randrange(WIDTH), randrange(HEIGHT))
    bomb_rct.center = r_1, r_2
    
    # 練習問題2, 移動量設定
    vx = 5
    vy = 5
    
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        # 練習問題2, 移動
        bomb_rct.move_ip(vx, vy)
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        
        # 練習問題1,表示
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