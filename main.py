import pygame
import time

pygame.init()

window_size = (800, 600)
# Создаём окно
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image1 = pygame.image.load("resource/apple.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("resource/lemon.png")
image_rect2 = image2.get_rect()

speed = 5
run = True

# В pygame всё происходит в игровом цикле
while run:
    # В pygame чаще всего создаётся цикл для перебора всех событий в программе
    # Каждое событие сохраняется в event
    for event in pygame.event.get():
        # Задаём выход из цикла в случае нажатия на 'X', иначе программа зависнет
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX
            image_rect1.y = mouseY
            image_rect1.x = mouseX - 20
            image_rect1.y = mouseY - 20

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_rect1.x -= speed
        if keys[pygame.K_RIGHT]:
            image_rect1.x += speed
        if keys[pygame.K_UP]:
            image_rect1.y -= speed
        if keys[pygame.K_DOWN]:
            image_rect1.y += speed

    if image_rect1.colliderect(image_rect2):
        print("Произошло столкновение")
        time.sleep(1)

    screen.fill((0, 255, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    # Обновляем содержимое экрана (также можно использовать update)
    pygame.display.flip()

pygame.quit()


