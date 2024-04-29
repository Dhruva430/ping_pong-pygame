# pyright: basic
import random
import pygame

from element import paddle, ping_pong

pygame.init()


def game():
    size = (800,600)
    running = True
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pong = ping_pong(size)
    # pongs = [ping_pong(size) for _ in range(1)]
    pad = paddle(0)
    pad2 = paddle(790)
    score = 0
    font2 = pygame.font.SysFont('Arial.ttf', 32)
    game_over = False
    # li = [pad,pad2]

    while running == True:
        # setting the frame 60
        delta = clock.tick(800) / 1000

        #TODO checking every event in the Queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN:
                game_over = False
        pressed =  pygame.key.get_pressed()
        
        screen.fill((0, 0, 0))
        if pong.position.x < 0:
            pong.position = pygame.Vector2(400,300)
            score += 1
            game_over = True
        if pong.position.x > size[0]:
            pong.position = pygame.Vector2(400,300)
            score += 1
            game_over = True
            
        if not game_over:
            if pressed[pygame.K_s]:
                pad.position.y += 500*delta
            if pressed[pygame.K_w]:
                pad.position.y -= 500*delta
            if pressed[pygame.K_DOWN]:
                pad2.position.y += 500*delta
            if pressed[pygame.K_UP]:
                pad2.position.y -= 500*delta
            pong.update(size, delta)
            pad.update()
            pad2.update()

        if pygame.Rect.colliderect(pong.rect,pad.rect):

            pong.direction.x *= -1
            pong.position.x = pad.rect.right + 10
        if pygame.Rect.colliderect(pong.rect,pad2.rect):
            pong.direction.x *= -1
            pong.position.x = pad2.rect.left - 10 - pong.rect.width
        score_txt = font2.render(f'score {score}', True, (0,255,0))
        screen.blit(score_txt,(10,10))
        
            #region Drawing
        
        pong.draw(screen)
        pad.draw(screen)
        pad2.draw(screen)
            
            #endregion
        

        pygame.display.flip()


if __name__ == "__main__":
    game()
