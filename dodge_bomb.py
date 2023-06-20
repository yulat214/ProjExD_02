import sys
import pygame as pg

from random import randint

WIDTH, HEIGHT = 1600, 900
key_dct = {
    pg.K_UP : (0, -5),
    pg.K_DOWN : (0, 5),
    pg.K_LEFT : (-5, 0),
    pg.K_RIGHT : (5, 0)
}

accs = [a for a in range(1, 11)]


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    cry_img = pg.image.load("ex02/fig/8.png")
    
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    bomb_imgs = []
    
    for r in range(1, 11):
        bomb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bomb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bomb_img.set_colorkey((0, 0, 0))
        bomb_imgs.append(bomb_img)
        
    bomb_img = pg.Surface((20, 20))
    bomb_rct = bomb_img.get_rect()
    r_1, r_2 = (randint(0, WIDTH), randint(0, HEIGHT))
    bomb_rct.center = r_1, r_2
    
    vx, vy = 5, 5
    
    # rotozoom dict
    # 左向きを基準に回転, 右向きは反転->回転
    rt_dct = {
        (0, -5):  pg.transform.flip(pg.transform.rotozoom(kk_img, -90, 2.0), True, False),
        (5, -5):  pg.transform.flip(pg.transform.rotozoom(kk_img, -45, 2.0), True, False),
        (5, 0):   pg.transform.flip(pg.transform.rotozoom(kk_img, 0, 2.0), True, False),
        (5, 5):  pg.transform.flip(pg.transform.rotozoom(kk_img, 45, 2.0), True, False),
        (0, 5):   pg.transform.flip(pg.transform.rotozoom(kk_img, 90, 2.0), True, False),
        (-5, 5):  pg.transform.rotozoom(kk_img, 45, 2.0),
        (-5, 0):  pg.transform.rotozoom(kk_img, 0, 2.0),
        (-5, -5): pg.transform.rotozoom(kk_img, -45, 2.0)
    }
    
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            # colliderectの基準をbombに更新
            if bomb_rct.colliderect(kk_rct):
                screen.blit(cry_img, [bx, by])
                pg.display.update()
                
                print("game over")
                return
    
        key_lst = pg.key.get_pressed()
        move_lst = [0, 0]
        
        for k, v in key_dct.items():
            if key_lst[k]:
                move_lst[0] += v[0]
                move_lst[1] += v[1]
            
        kk_rct.move_ip(move_lst)
        if in_or_out(kk_rct) != (True, True):
            kk_rct.move_ip(-1*move_lst[0], -1*move_lst[1])
            
        # 300フレームに一回加速
        avx, avy = vx*accs[min(tmr//300, 9)], vy*accs[min(tmr//300, 9)]
        bomb_rct.move_ip(avx, avy)
        v, h = in_or_out(bomb_rct)
        if not v:
            vy *= -1
        if not h:
            vx *= -1
            
        screen.blit(bg_img, [0, 0])
        
        # move_lstの値をtupleに変換してからキーとして辞書に渡す
        # 向きが変わるときのみkk_imgを更新
        if move_lst != [0, 0]:
            kk_img = rt_dct[tuple(move_lst)]
        
        screen.blit(kk_img, kk_rct)
        
        # 300フレームごとに拡大
        bomb = bomb_imgs[min(tmr//300, 9)]
        a, b = bomb_rct.center
        bomb_rct = bomb_img.get_rect()
        bomb_rct.center = a,b 
        screen.blit(bomb, bomb_rct)
        
        pg.display.update()
        tmr += 1
        # original -> clock.tick(10)
        clock.tick(50)
        
        bx, by = kk_rct.center
        
        
# 練習問題4
def in_or_out(rct: pg.Rect):
    """_こうかとん, 爆弾のRectが画面外(False)か画面内(True)か判断

    Args:
        rct: rectオブジェクト

    Returns:
        _type_: 真理値のタプル(たて, よこ)
    """
    v, h = True, True
    if  WIDTH < rct.right or rct.left < 0:
        h = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        v = False
    return v, h

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()