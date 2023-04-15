from PIL import Image, ImageDraw, ImageFont

# 定义常量
CARD_WIDTH, CARD_HEIGHT = 50, 70
IMG_RESOLUTION = 300

# 定义花色和数字
suits = ["s", "h", "c", "d"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
jokers = ["大王", "小王"]
# 创建画布
canvas_width = CARD_WIDTH
canvas_height = CARD_HEIGHT
canvas = Image.new("RGB", (canvas_width, canvas_height), (0, 128, 0))

# 加载字体
font = ImageFont.truetype("font\\msyh.ttf", size=20)

# 绘制每张牌
for i, suit in enumerate(suits):
    for j, rank in enumerate(ranks):
        # 创建新的画布
        if i == 0:
            card_canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), (0, 0, 0))
        if i == 1:
            card_canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), (255, 0, 0))
        if i == 2:
            card_canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), (163, 148, 128))
        if i == 3:
            card_canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), (255, 153, 18))
        draw = ImageDraw.Draw(card_canvas)

        # 绘制牌面
        draw.text((0, 0), rank, font=font, fill=(255, 255, 255))
        draw.text((0, 20), suit, font=font, fill=(255, 255, 255))

        # 保存图片
        filename = f"images\\{suit}_{rank}.png"
        card_canvas.save(filename, dpi=(IMG_RESOLUTION, IMG_RESOLUTION))
#单独保存大小王
font_joker = ImageFont.truetype("font\\msyh.ttf", size=20)
for i, joker in enumerate(jokers):
    card_joker = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), (160, 32, 240))
    draw_joker = ImageDraw.Draw(card_joker)
    draw_joker.text((0, 0), joker, font=font_joker, fill=(255, 255, 255))
    filename_joker = f"images\\{joker}.png"
    card_joker.save(filename_joker, dpi=(IMG_RESOLUTION, IMG_RESOLUTION))
print("保存完成！")
