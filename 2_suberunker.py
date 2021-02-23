# 전체 정리 (게임 개발 프레임)
import pygame
from random import *

# --------------------------------------------------------------------------------
# 기본 초기화 (반드시 해야하는 것들)

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥피하기 게임")

# FPS
clock = pygame.time.Clock()       

# --------------------------------------------------------------------------------
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 이미지 불러오기
background = pygame.image.load("C:/JB/Coding/Python/Practice/inflearn_lecture/resources/resized_background.jpg")
character = pygame.image.load("C:/JB/Coding/Python/Practice/inflearn_lecture/resources/one_puppy.png")
ddong = pygame.image.load("C:/JB/Coding/Python/Practice/inflearn_lecture/resources/one_ddong.png")

# 캐릭터, 똥 정보
character_width = character.get_width()
character_height = character.get_height()
ddong_width = ddong.get_width()
ddong_height = ddong.get_height()

# 캐릭터 배치
character_xpos = screen_width/2 - character_width/2
character_ypos = screen_height - character_height

# 캐릭터 속도
character_speed = 15

# 캐릭터 이동 좌표
# to_x = 0
to_x_LEFT = 0
to_x_RIGHT = 0

# # 똥 만들기, 배치 (랜덤)
# ddong_xpos = randint(0, screen_width - ddong_width)
# ddong_ypos = -ddong_height

# 똥 속도
ddong_speed = 20

# 똥 이동 좌표
to_y = ddong_speed

# 똥 여러개
ddongs = []

# Font
game_font = pygame.font.Font(None, 40)
ddong_count = 0

# [이벤트 루프]
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치 정의 (이동, 경계값 처리 등)
        # 키 다운
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT += character_speed

            elif event.key == pygame.K_SPACE:
                ddong_xpos = randint(0, screen_width - ddong_width)
                ddong_ypos = -ddong_height
                ddongs.append([ddong_xpos, ddong_ypos])
                ddong_count += 1
            
        # 키 업
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x_LEFT = 0
            if event.key == pygame.K_RIGHT:
                to_x_RIGHT = 0
            
    # 캐릭터 이동
    character_xpos += to_x_LEFT + to_x_RIGHT
 
    # 경계선
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos + character_width > screen_width:
        character_xpos = screen_width - character_width
    
    # 똥 이동
    # ddong_ypos += to_y
    ddongs = [[d[0], d[1] + ddong_speed] for d in ddongs]

    # 바닥에 닿은 똥 없애기
    ddongs = [[d[0], d[1]] for d in ddongs if d[1] < screen_height]

    # # 똥 다시 생성
    # if ddong_ypos > screen_height:
    #     ddong_xpos = randint(0, screen_width - ddong_width)
    #     ddong_ypos = -ddong_height

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    # ddong_rect = ddong.get_rect()
    # ddong_rect.left = ddong_xpos
    # ddong_rect.top = ddong_ypos

    # if character_rect.colliderect(ddong_rect):
    #     print("Game Over")
    #     running = False

    for d in ddongs:
        ddong_rect = ddong.get_rect()
        ddong_rect.left = d[0]
        ddong_rect.top = d[1]
        if character_rect.colliderect(ddong_rect) :
            running = False
            break
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_xpos, character_ypos))
    # screen.blit(ddong, (ddong_xpos, ddong_ypos))
    for d in ddongs:
        screen.blit(ddong, (d[0], d[1]))

    # 똥 개수 출력
    ddong_counter = game_font.render("Poop : {0}".format(ddong_count), True, (0,0,0))
    screen.blit(ddong_counter, (10, 10))

    pygame.display.update()

msg = pygame.font.Font(None, 65).render("Game Over", True, (255,175,0))
msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2 - 100))
screen.blit(msg, msg_rect)

pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
