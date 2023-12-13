import pygame
import random
import time

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("피자 만들기 게임")

# 이미지 로드
dough_image = pygame.image.load("pizza_dough.png")

# 피자와 재료 설정
pizzas = {
    "페페로니": ["도우", "페페로니", "치즈", "올리브"],
    "새우": ["도우", "치즈", "새우", "올리브"],
    "하와이안": ["도우", "올리브", "파인애플", "치즈"],
    "베이컨": ["도우", "베이컨", "치즈", "올리브"],
    "고구마": ["도우", "고구마", "치즈", "올리브"],
}

pizza_names = list(pizzas.keys())

# 이미지 파일명을 확인하고 수정
ingredient_images = {
    "도우": pygame.image.load("pizza_dough.png"),
    "페페로니": pygame.image.load("pepperoni.png"),
    "치즈": pygame.image.load("cheese.png"),
    "올리브": pygame.image.load("olive.png"),
    "파인애플": pygame.image.load("pineapple.png"),
    "새우": pygame.image.load("shrimp.png"),
    "베이컨": pygame.image.load("bacon.png"),
    "고구마": pygame.image.load("goma.png"),
}

# 게임 루프
def game_loop():
    total_pizzas = 10  # 총 만들 피자 개수
    pizza_time = 10  # 피자 하나당 만드는 시간 (초)
    ingredient_limit = 10  # 피자당 최대 재료 개수
    start_time = 0
    pizza_count = 0
    total_earnings = 0  # 총 수익

    current_pizza = random.choice(list(pizzas.keys()))
    current_price = 10000
    ingredients = []
    current_toppings = ["치즈", "베이컨", "페페로니", "올리브", "파인애플", "새우", "고구마"]
    current_topping_index = 0  # 현재 선택된 토핑 인덱스
    topping_counts = {"치즈": 0, "베이컨": 0, "페페로니": 0, "올리브": 0, "파인애플": 0, "새우":0, "고구마":0}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not start_time:
                    start_time = time.time()
                else:
                    x, y = pygame.mouse.get_pos()
                    if len(ingredients) < ingredient_limit:
                        # 마우스 클릭한 위치에 현재 선택된 토핑 추가
                        ingredients.append((x, y, current_toppings[current_topping_index]))
                        topping_counts[current_toppings[current_topping_index]] += 1
                        # 토핑이 제시된 피자의 토핑과 일치하는지 확인
                        if (
                            current_toppings[current_topping_index] not in pizzas[current_pizza]
                        ):
                            current_price -= 1000  # 틀린 토핑 선택 시 가격 차감
                    else:
                        print("재료 개수 초과! 다음 피자로 넘어갑니다.")
                        # 피자 개수 증가
                        pizza_count += 1
                        total_earnings += current_price  # 현재 피자의 가격을 총 수익에 추가
                        if pizza_count >= total_pizzas:
                            print("모든 피자 완성! 게임 종료")
                            print(f"총 수익: {total_earnings}원")
                            return
                        # 다음 피자로 넘어가기
                        current_pizza = random.choice(list(pizzas.keys()))
                        current_price = 10000
                        ingredients = []
                        current_topping_index = 0  # 토핑 인덱스 초기화
                        topping_counts = {"치즈": 0, "베이컨": 0, "페페로니": 0, "올리브": 0, "파인애플": 0, "새우":0, "고구마":0}
                        start_time = time.time()  # 다음 피자 시작 시간 초기화
            elif event.type == pygame.KEYDOWN:
                # 키보드 입력 처리
                if event.key == pygame.K_c:
                    current_topping_index = 0  # 치즈 선택
                elif event.key == pygame.K_b:
                    current_topping_index = 1  # 베이컨 선택
                elif event.key == pygame.K_p:
                    current_topping_index = 2  # 페페로니 선택
                elif event.key == pygame.K_o:
                    current_topping_index = 3  # 올리브 선택
                elif event.key == pygame.K_g:
                    current_topping_index = 4  # 고구마 선택
                elif event.key == pygame.K_s:
                    current_topping_index = 5  #새우 선택
                elif event.key == pygame.K_f:
                    current_topping_index = 6  # 파인애플 선택

        elapsed_time = time.time() - start_time
        remaining_time = pizza_time - elapsed_time

        if start_time and remaining_time <= 0:
            print("시간 초과! 다음 도우로 넘어갑니다.")
            pizza_count += 1
            total_earnings += current_price  # 현재 피자의 가격을 총 수익에 추가
            if pizza_count >= total_pizzas:
                print("모든 피자 완성! 게임 종료")
                print(f"총 수익: {total_earnings}원")
                return
            # 다음 피자로 넘어가기
            current_pizza = random.choice(list(pizzas.keys()))
            current_price = 10000
            ingredients = []
            current_topping_index = 0  # 토핑 인덱스 초기화
            topping_counts = {"치즈": 0, "베이컨": 0, "페페로니": 0, "올리브": 0}
            start_time = time.time()  # 다음 피자 시작 시간 초기화

        screen.fill((255, 255, 255))  # 배경색
        
        price_font = pygame.font.Font(None,24)
        # 도우 그리기
        screen.blit(dough_image, (screen_width // 2 - 50, screen_height // 2 - 50))
        current_price_text = price_font.render(f"pizza price: {current_price}원",True,(0,0,0))
        screen.blit(current_price_text,(screen_width// 2 - 60, screen_height// 2 - 90))


        # 피자 정보 표시
        font = pygame.font.Font(None, 36)
        pizza_info = font.render(f"만들어야 할 피자: {current_pizza}", True, (0, 0, 0))
        screen.blit(pizza_info, (10, 10))

        # 피자 횟수와 남은 시간 표시
        status_text = font.render(f"피자 횟수: {pizza_count + 1}/{total_pizzas} | 남은 시간: {max(0, int(remaining_time))}초", True, (0, 0, 0))
        screen.blit(status_text, (10, 50))

        # 현재 선택된 토핑 표시
        topping_text = font.render(f"현재 토핑: {current_toppings[current_topping_index]}", True, (0, 0, 0))
        screen.blit(topping_text, (10, 90))

        # 게임 시작 전에는 시작 버튼을 표시
        if not start_time:
            start_button_rect = pygame.Rect(300, 400, 200, 100)
            pygame.draw.rect(screen, (0, 255, 0), start_button_rect)
            start_text = font.render("게임 시작", True, (255, 255, 255))
            screen.blit(start_text, (350, 450))

        # 재료 그리기
        for ingredient in ingredients:
            x, y, ingredient_name = ingredient
            # 현재 선택된 토핑 그리기
            screen.blit(ingredient_images[ingredient_name], (x, y))

        pygame.display.update()

    pygame.quit()

# 게임 실행
game_loop()