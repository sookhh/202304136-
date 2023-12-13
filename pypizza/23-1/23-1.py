import pygame
import sys
import random
import time

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("토핑 선택 게임")

# 색상 정의
white = (255, 255, 255)

# 이미지 로드 (png 형식으로 변경)
pizza_dough = pygame.image.load("pizza_dough.png")
bacon_img = pygame.image.load("bacon.png")
cheese_img = pygame.image.load("cheese.png")
pepperoni_img = pygame.image.load("pepperoni.png")
veggies_img = pygame.image.load("veggies.png")

# 토핑 리스트
topping_list = []

# 게임 시작 여부
game_started = False

# 피자 종류 및 토핑 종류
pizza_types = {
    "베이컨 피자": [bacon_img, cheese_img],
    "치즈 피자": [cheese_img, veggies_img],
    "페퍼로니 피자": [pepperoni_img, cheese_img],
    "야채 피자": [veggies_img, cheese_img]
}
selected_pizza = ""
current_toppings = []

# 피자별 성공 조건
pizza_success_conditions = {
    "베이컨 피자": [bacon_img, cheese_img],
    "치즈 피자": [cheese_img],
    "페퍼로니 피자": [pepperoni_img, cheese_img],
    "야채 피자": [veggies_img, cheese_img]
}

# 폰트 설정
font = pygame.font.Font(None, 36)

# 제한 시간
time_limit = 15
start_time = 0

# 피자당 최대 가격
max_pizza_price = 10000

# 현재 피자의 가격
current_pizza_price = 0

# 1판당 15초의 시간 안에 20개의 토핑을 올릴 수 있도록 설정
time_limit_per_game = 15
total_pizza_games = 10
current_pizza_game = 0
max_toppings_per_game = 20

class Topping:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# 게임 설명서
instruction_text = [
    "게임 설명:",
    "1. 각 피자에 필요한 토핑을 추가하여 피자를 완성하세요.",
    "2. 베이컨 피자: 베이컨과 치즈 토핑",
    "   치즈 피자: 치즈 토핑만",
    "   페퍼로니 피자: 페퍼로니와 치즈 토핑",
    "   야채 피자: 야채와 치즈 토핑",
    "3. 게임 시작 버튼을 클릭하면 타이머가 시작됩니다.",
    "4. 주어진 시간 내에 피자를 완성하세요.",
    "5. 마우스로 클릭하여 토핑을 추가하거나 키보드로 토핑을 변경하세요.",
    "6. 1, 2, 3, 4 키로 피자를 선택하세요."
]

# 현재 선택된 토핑
current_selected_topping = None

# 게임 루프
running = True
while running:
    screen.fill(white)

    if not game_started:
        if topping_list:
            # 게임 종료 시 성공 또는 실패 여부 표시
            success = all(topping.image in current_toppings for topping in topping_list)
            result_text = font.render("성공!" if success else "실패!", True, (0, 0, 0))
            screen.blit(result_text, (screen_width // 2 - result_text.get_width() // 2, 250))
        else:
            # 게임 시작 버튼
            start_button = pygame.Rect(300, 300, 200, 100)
            pygame.draw.rect(screen, (0, 255, 0), start_button)
            start_text = font.render("게임 시작", True, (0, 0, 0))
            screen.blit(start_text, (340, 340))

            # 게임 설명서 표시
            for i, line in enumerate(instruction_text):
                line_text = font.render(line, True, (0, 0, 0))
                screen.blit(line_text, (10, 10 + i * 30))

            # 이벤트 처리 (게임 시작 버튼 클릭)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if start_button.collidepoint(x, y):
                        game_started = True
                        selected_pizza = random.choice(list(pizza_types.keys()))
                        current_toppings = pizza_types[selected_pizza]
                        start_time = time.time()
    else:
        # 현재 시간 계산
        current_time = int(time.time() - start_time)

        # 남은 시간 계산
        remaining_time = max(time_limit - current_time, 0)

        # 배경에 도우 이미지 표시
        screen.blit(pizza_dough, (0, 0))

        # 토핑 이미지 표시
        for topping in topping_list:
            screen.blit(topping.image, topping.rect.topleft)

        # 피자 종류 표시
        pizza_text = font.render(selected_pizza, True, (0, 0, 0))
        screen.blit(pizza_text, (screen_width // 2 - pizza_text.get_width() // 2, 10))

        # 남은 시간 표시
        time_text = font.render(f"남은 시간: {remaining_time}초", True, (0, 0, 0))
        screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, 50))

        # 피자의 가격 표시
        price_text = font.render(f"피자 가격: {current_pizza_price}원", True, (0, 0, 0))
        screen.blit(price_text, (screen_width // 2 - price_text.get_width() // 2, 90))

        # 현재 게임의 남은 시간 표시
        current_game_time = max(time_limit_per_game - current_time % time_limit_per_game, 0)
        game_time_text = font.render(f"현재 게임 남은 시간: {current_game_time}초", True, (0, 0, 0))
        screen.blit(game_time_text, (screen_width // 2 - game_time_text.get_width() // 2, 130))

        # 이벤트 처리 (마우스 클릭, 키보드 입력)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if len(topping_list) < max_toppings_per_game:
                    # 토핑 추가
                    topping_image = current_selected_topping or random.choice(current_toppings)
                    topping_list.append(Topping(topping_image, x, y))
                    # 토핑이 제시된 피자의 토핑과 일치하는지 확인
                    if topping_image not in pizza_success_conditions[selected_pizza]:
                        current_pizza_price -= 500  # 틀린 토핑 선택 시 가격 차감
            elif event.type == pygame.KEYDOWN:
                # 키보드 입력 처리 (1, 2, 3, 4 키로 피자 변경)
                if event.key == pygame.K_1:
                    selected_pizza = "베이컨 피자"
                    current_toppings = pizza_types[selected_pizza]
                    current_selected_topping = None
                elif event.key == pygame.K_2:
                    selected_pizza = "치즈 피자"
                    current_toppings = pizza_types[selected_pizza]
                    current_selected_topping = None
                elif event.key == pygame.K_3:
                    selected_pizza = "페퍼로니 피자"
                    current_toppings = pizza_types[selected_pizza]
                    current_selected_topping = None
                elif event.key == pygame.K_4:
                    selected_pizza = "야채 피자"
                    current_toppings = pizza_types[selected_pizza]
                    current_selected_topping = None
                elif event.key == pygame.K_b:
                    current_selected_topping = bacon_img
                elif event.key == pygame.K_c:
                    current_selected_topping = cheese_img
                elif event.key == pygame.K_p:
                    current_selected_topping = pepperoni_img
                elif event.key == pygame.K_v:
                    current_selected_topping = veggies_img

        # 게임 종료 조건
        if current_time >= time_limit or len(topping_list) >= max_toppings_per_game:
            current_pizza_game += 1
            # 최대 가격에서 현재 가격을 차감하여 피자 가격 계산
            current_pizza_price = max_pizza_price
            topping_list = []  # 토핑 초기화
            if current_pizza_game >= total_pizza_games:
                # 각 판의 피자 가격 합산
                total_earnings = max_pizza_price * total_pizza_games - current_pizza_price
                success = all(topping.image in pizza_success_conditions[selected_pizza] for topping in topping_list)
                print(f"게임 종료! {'성공!' if success else '실패!'} 총 수익: {total_earnings}원")
                game_started = False
                current_pizza_game = 0
                topping_list = []
                current_pizza_price = max_pizza_price  # 피자 가격 초기화

    # 화면 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()
sys.exit()
