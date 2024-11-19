import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 背景画像Surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")  
    kk_img = pg.transform.flip(kk_img, True, False)  # こうかとんを左右反転させる
    kk_rct = kk_img.get_rect()  # こうかとんRectを取得する
    kk_rct.center = 300, 200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()

        m_x, m_y = -1, 0  # デフォルトで左に移動（背景と同じ速度）
        
        if key_lst[pg.K_UP]:
            m_y = -1  # 上方向
        if key_lst[pg.K_DOWN]:
            m_y = 1  # 下方向
        if key_lst[pg.K_RIGHT]:
            m_x = 1  # 右方向
        
        kk_rct.move_ip(m_x, m_y)  # 1回だけ移動を適用

        x = -(tmr%3200)
        screen.blit(bg_img,  [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)  # screen Surfaceにこうかとん画像Surfaceを貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()