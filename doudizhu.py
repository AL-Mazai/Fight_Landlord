import pygame
import random

# 画布大小
WIDTH, HEIGHT = 1200, 600
# 牌大小
CARD_WIDTH, CARD_HEIGHT = 50, 70
# 边距
MARGIN_X, MARGIN_Y = 80, 20

# 花色和数字
suits = ["s", "h", "c", "d"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
jokers = ["大王", "小王"]
# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("斗地主")

# 加载牌
card_images = {}
for suit in suits:
    for rank in ranks:
        card_images[f"{suit}_{rank}"] = pygame.image.load(f"images\\{suit}_{rank}.png")
for joker in jokers:
    card_images[f"{joker}"] = pygame.image.load(f"images\\{joker}.png")
# 设置三个玩家
player1 = []
player2 = []
player3 = []
players = [player1, player2, player3]
# 设置地主：随机选择
landlord = random.choice([player1, player2, player3])
# 设置当前玩家：初始化为地主
current_player = landlord
# 创建一副牌
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f"{suit}_{rank}")
for joker in jokers:
    deck.append(f"{joker}")
# 洗牌
random.shuffle(deck)
# 三张地主牌
landlord_cards = deck[-3:]
# 发牌
for i in range(51):
    if i % 3 == 0:
        player1.append(deck[i])
    elif i % 3 == 1:
        player2.append(deck[i])
    else:
        player3.append(deck[i])


# 绘制玩家的牌
def draw_cards(player, x, y):
    for index, card in enumerate(player):
        rect = pygame.Rect(x + index * CARD_WIDTH + index, y, CARD_WIDTH, CARD_HEIGHT)
        screen.blit(card_images[card], rect)


landlord.extend(deck[-3:])


# 玩家事件
def event_loop():
    global current_player, landlord
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 切换到下一个玩家
                if current_player == player1:
                    current_player = player2
                elif current_player == player2:
                    current_player = player3
                else:
                    current_player = player1
                current_player.pop()


# 点击次数
click_count = {"landlord": False}
while True:
    # 绘制界面
    screen.fill((0, 128, 0))
    # 花色说明
    font = pygame.font.Font("font/msyh.ttf", 30)
    text_rule = font.render("s:黑桃,h:红心,c:梅花,d:方块", True, 'yellow')
    screen.blit(text_rule, (400, MARGIN_Y))

    # 排序
    player1.sort()
    player2.sort()
    player3.sort()

    # 绘制玩家的牌
    font_players = pygame.font.Font("font/msyh.ttf", 20)
    draw_cards(player1, MARGIN_X, MARGIN_Y * 4)
    draw_cards(player2, MARGIN_X, MARGIN_Y * 8)
    draw_cards(player3, MARGIN_X, MARGIN_Y * 12)
    # 玩家标注
    for i, player in enumerate(players):
        if player is not landlord:
            text_player = font_players.render(f"农民{i + 1}", True, 'yellow')
            screen.blit(text_player, (MARGIN_X // 6 + 5, MARGIN_Y * (i + 1) * 4 + MARGIN_Y))
        else:
            text_player = font_players.render("地主", True, 'yellow')
            screen.blit(text_player, (MARGIN_X // 6 + 5, MARGIN_Y * (i + 1) * 4 + MARGIN_Y))
    # 绘制地主牌
    text_landlord = font_players.render("地主牌", True, 'yellow')
    screen.blit(text_landlord, (MARGIN_X // 6, MARGIN_Y * 20))
    if landlord is not None:
        for i, landlord_card in enumerate(landlord_cards):
            rect1 = pygame.Rect(MARGIN_X + i * CARD_WIDTH + i, MARGIN_Y * 20, CARD_WIDTH, CARD_HEIGHT)
            screen.blit(card_images[landlord_card], rect1)
    # 更新屏幕
    pygame.display.flip()
    #################################开始斗地主######################################
    player_name = "地主"
    if len(current_player) != 0:
        if current_player is landlord:
            player_name = "地主"
        elif current_player is player1:
            player_name = "农民1"
        elif current_player is player2:
            player_name = "农民2"
        elif current_player is player3:
            player_name = "农民3"
        selection = input(f"{player_name}请选择，出牌请按1，“过”请按任意键：")
        if selection == '1':
            card = input("请您出牌：")
            if card in current_player:
                current_player.remove(card)
            else:
                while card not in current_player:
                    card = input(f"您没有“{card}”这张牌,请重新选择：")
                current_player.remove(card)
            print(f"上一个玩家“{player_name}”出的牌是“{card}”")
        else:
            print(f"上一个玩家“{player_name}”选择“过”！")
        # 切换当前玩家
        if len(current_player) != 0:
            if current_player == player1:
                current_player = player2
            elif current_player == player2:
                current_player = player3
            elif current_player == player3:
                current_player = player1
    else:
        if current_player is landlord:
            print("地主赢！")
        else:
            print("农民赢！")
        break
    ####################################################################################
# 关闭窗口
for event in pygame.event.get():
    if event.type == pygame.QUIT:  # 退出游戏
        pygame.quit()
        exit()
