import pygame
import random
import time
pygame.init()
pygame.mixer.init()
tutorial_music = pygame.mixer.music.load("tutorial_music.mp3")
gameplay_music = pygame.mixer.Sound("gameplay_music.mp3")
pygame.mixer.music.set_volume(0.5)
gameplay_music.set_volume(0.5)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Making 10,000Won pizza game")
pizza_dough_image = pygame.image.load("pizza_dough.png")
dough_rect = pizza_dough_image.get_rect()
screen.blit(pizza_dough_image, (screen_width // 2 - dough_rect.width // 2, screen_height // 2 - dough_rect.height // 2))
pizzas = {
    "pepperoni pizza": ["도우", "pepperoni", "cheese", "olive"],
    "shrimp pizza": ["도우", "cheese", "shrimp", "olive"],
    "hawaiian pizza": ["도우", "olive", "fineapple", "cheese"],
    "bacon pizza": ["도우", "bacon", "cheese", "olive"],
    "sweet potato pizza": ["도우", "goguma", "cheese", "olive"],
}
pizza_names = list(pizzas.keys())
ingredient_images = {
    "도우": pygame.image.load("pizza_dough.png"),
    "pepperoni": pygame.image.load("pepperoni.png"),
    "cheese": pygame.image.load("cheese.png"),
    "olive": pygame.image.load("olive.png"),
    "pineapple": pygame.image.load("pineapple.png"),
    "shrimp": pygame.image.load("shrimp.png"),
    "bacon": pygame.image.load("bacon.png"),
    "goguma": pygame.image.load("goma.png"),
}
font = pygame.font.Font(None, 45)
def main_menu():
    tutorial_button_rect = pygame.Rect(screen_width // 2 - 260 , screen_height // 2 + 55, 230, 120)
    game_start_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 95, 250, 130)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if tutorial_button_rect.collidepoint(x, y):
                    print("튜토리얼 버튼 클릭됨")
                    game_tutorial()  # 튜토리얼 실행
                elif game_start_button_rect.collidepoint(x, y):
                    print("게임 시작 버튼 클릭됨")
                    game_loop()  # 게임 루프 실행
        screen.fill((255, 255, 255))
        pygame.draw.ellipse(screen, (200, 17, 31), tutorial_button_rect)
        pygame.draw.ellipse(screen, (255, 242, 222), tutorial_button_rect, width=2)
        tutorial_text = pygame.font.Font(None, 45).render("튜토리얼 시작", True, (255, 255, 255))
        text_rect = tutorial_text.get_rect(center=tutorial_button_rect.center)
        screen.blit(tutorial_text, text_rect.topleft)
        pygame.draw.ellipse(screen, (200, 17, 31), game_start_button_rect)
        pygame.draw.ellipse(screen, (255, 242, 222), game_start_button_rect, width=2)
        game_start_text = pygame.font.Font(None, 45).render("게임 시작", True, (255, 255, 255))
        text_rect = game_start_text.get_rect(center=game_start_button_rect.center)
        screen.blit(game_start_text, text_rect.topleft)
        pygame.display.update()
def game_tutorial():
    pygame.mixer.music.play(-1)
    tutorial_button_rect = pygame.Rect(screen_width // 2 - 260 , screen_height // 2 + 55, 230, 120)
    tutorial_bg = pygame.image.load("tu.png")
    tutorial_image2 = pygame.image.load("to.png")
    tutorial_image3 = pygame.image.load("ri.png")
    tutorial_image4 = pygame.image.load("al.png")
    tutorial_image5 = pygame.image.load("sul.png")
    tutorial_button_clicked = False
    while not tutorial_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if tutorial_button_rect.collidepoint(x, y):
                    tutorial_button_clicked = True
        pygame.mixer.music.stop()
        screen.blit(tutorial_bg, (0, 0))
        pygame.draw.ellipse(screen, (200, 17, 31), tutorial_button_rect)
        pygame.draw.ellipse(screen, (255, 242, 222), tutorial_button_rect, width=2)
        tutorial_text = font.render("tutorial start", True, (255, 255, 255))
        text_rect = tutorial_text.get_rect(center=tutorial_button_rect.center)
        screen.blit(tutorial_text, text_rect.topleft)
        pygame.display.update()
        pygame.time.delay(100)
    screen.fill((255, 255, 255))
    pygame.display.update()
    screen.blit(tutorial_image2, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)  
    screen.blit(tutorial_image3, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)  # 1초 대기
    screen.blit(tutorial_image4, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)  # 1초 대기
    screen.blit(tutorial_image5, (0, 0))
    pygame.display.update()
    game_start_button_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 95, 250, 130)
    pygame.draw.ellipse(screen, (200, 17, 31), game_start_button_rect)
    pygame.draw.ellipse(screen, (255, 242, 222), game_start_button_rect, width=2)
    game_start_text = font.render("Game Start", True, (255, 255, 255))
    text_rect = game_start_text.get_rect(center=game_start_button_rect.center)
    screen.blit(game_start_text, text_rect.topleft)
    pygame.display.update()
    start_button_clicked = False
    while not start_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if game_start_button_rect.collidepoint(x, y):
                    start_button_clicked = True
    screen.fill((255, 255, 255))
    pygame.display.update()
def game_loop():
    gameplay_music.play()
    total_pizzas = 10 # 총 만들 피자 개수
    pizza_time = 10  # 피자 하나당 만드는 시간 (초)
    ingredient_limit = 10  # 피자당 최대 재료 개수
    start_time = 0
    pizza_count = 0
    total_earnings = 0  # 총 수익
    current_pizza = random.choice(list(pizzas.keys()))
    current_price = 10000
    ingredients = []
    current_toppings = ["cheese", "bacon", "pepperoni", "olive", "pineapple", "shrimp", "goguma"]
    current_topping_index = 0  # 현재 선택된 토핑 인덱스
    topping_counts = {"cheese": 0, "bacon": 0, "pepperoni": 0, "olive": 0, "fineapple": 0, "shrimp": 0, "goguma": 0}
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
                        ingredients.append((x, y, current_toppings[current_topping_index]))
                        topping_counts[current_toppings[current_topping_index]] += 1
                        if current_toppings[current_topping_index] not in pizzas[current_pizza]:
                            current_price -= 1000
                        else:
                            if topping_counts[current_toppings[current_topping_index]] == 10:
                                current_price = 5000
                            elif topping_counts[current_toppings[current_topping_index]] >= 2:
                                current_price = 7000
                            elif topping_counts[current_toppings[current_topping_index]] == 3:
                                current_price = 10000
                    else:
                        print("재료 개수 초과! 다음 피자로 넘어갑니다.")
                        current_price -= (ingredient_limit - len(ingredients)) * 1000
                        pizza_count += 1
                        total_earnings += current_price  # 현재 피자의 가격을 총 수익에 추가
                        if pizza_count >= total_pizzas:
                            print("모든 피자 완성! 게임 종료")
                            show_result(total_earnings)
                            return
                        current_pizza = random.choice(list(pizzas.keys()))
                        current_price = 10000
                        ingredients = []
                        current_topping_index = 0  # 토핑 인덱스 초기화
                        topping_counts = {"cheese": 0, "bacon": 0, "pepperoni": 0, "olive": 0, "pineapple": 0, "shrimp": 0, "goguma": 0}
                        start_time = time.time()  # 다음 피자 시작 시간 초기화
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 'c':
                    current_topping_index = 0  # 치즈 선택
                elif event.unicode == 'b':
                    current_topping_index = 1  # 베이컨 선택
                elif event.unicode == 'p':
                    current_topping_index = 2  # 페페로니 선택
                elif event.unicode == 'o':
                    current_topping_index = 3  # 올리브 선택
                elif event.unicode == 'g':
                    current_topping_index = 6  # 고구마 선택
                elif event.unicode == 's':
                    current_topping_index = 5  # 새우 선택
                elif event.unicode == 'f':
                    current_topping_index = 4  # 파인애플 선택
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_loop()
        elapsed_time = time.time() - start_time
        remaining_time = pizza_time - elapsed_time
        if start_time and remaining_time <= 0:
            print("시간 초과! 다음 도우로 넘어갑니다.")
            current_price -= (ingredient_limit - len(ingredients)) * 1000
            pizza_count += 1
            if pizza_count >= total_pizzas:
                print("모든 피자 완성! 게임 종료")
                show_result(total_earnings)
                return
            current_pizza = random.choice(list(pizzas.keys()))
            current_price = 10000
            ingredients = []
            current_topping_index = 0  # 토핑 인덱스 초기화
            topping_counts = {"cheese": 0, "bacon": 0, "pepperoni": 0, "olive": 0, "pineapple": 0, "shrimp": 0, "goguma": 0}
            start_time = time.time()  # 다음 피자 시작 시간 초기화
        screen.fill((255, 255, 255))  # 배경색
        price_font = pygame.font.Font(None, 24)
        dough_image = pygame.image.load("pizza_dough.png")
        dough_rect = dough_image.get_rect()
        screen.blit(dough_image, (screen_width // 2 - dough_rect.width // 2, screen_height // 2 - dough_rect.height // 2))
        price_text = price_font.render(f"price: {current_price}Won", True, (0, 0, 0))
        screen.blit(price_text, (10, screen_height - 30))
        font = pygame.font.Font(None, 36)
        pizza_info = font.render(f"make: {current_pizza}", True, (0, 0, 0))
        screen.blit(pizza_info, (10, 10))
        status_text = font.render(
            f"number of pizza: {pizza_count + 1}/{total_pizzas} | remaining time: {max(0, int(remaining_time))}second",
            True, (0, 0, 0))
        screen.blit(status_text, (10, 50))
        topping_text = font.render(f"current toppings: {current_toppings[current_topping_index]}", True,
                                   (0, 0, 0))
        screen.blit(topping_text, (10, 90))
        for ingredient in ingredients:
            x, y, ingredient_name = ingredient
            screen.blit(ingredient_images[ingredient_name], (x, y))
        pygame.display.update()
def show_result(total_earnings):
    result_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Result")
    font = pygame.font.Font(None, 36)
    feedback_text = None
    if total_earnings <= 50000:
        feedback_text = font.render("Game Over! You need more practice.", True, (255, 0, 0))
    elif total_earnings <= 70000:
        feedback_text = font.render("Not bad, but you can do better!", True, (255, 165, 0))
    elif total_earnings <= 90000:
        feedback_text = font.render("Almost there! Keep practicing.", True, (255, 255, 0))
    else:
        feedback_text = font.render("Congratulations! You've successfully completed the game!", True, (0, 255, 0))
    result_screen.fill((255, 224, 133))  # 배경색 변경
    result_screen.blit(feedback_text, (20, 100))
    total_earnings_text = font.render(f"Total Earnings: {total_earnings}", True, (255, 255, 255))  # 흰색으로 변경
    result_screen.blit(total_earnings_text, (20, 150))
    restart_button_rect = pygame.Rect(300, 400, 200, 100)
    pygame.draw.ellipse(result_screen, (203, 0, 34), restart_button_rect)  # 타원형 모양, 지정한 RGB 값 사용
    pygame.draw.ellipse(result_screen, (255, 242, 222), restart_button_rect, width=2)  # 외곽선 색 (FFF2DE)
    restart_text = font.render("Restart", True, (255, 255, 255))
    text_rect = restart_text.get_rect(center=restart_button_rect.center)
    result_screen.blit(restart_text, text_rect.topleft)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(x, y):
                    game_loop()    
main_menu()                    
game_tutorial()                    
game_loop()