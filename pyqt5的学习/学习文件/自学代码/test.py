import pygame
import sys

# 初始化Pygame
pygame.init()

# 棋盘大小
BOARD_SIZE = 15
BOARD_WIDTH = 40
CHESS_RADIUS = BOARD_WIDTH // 2 - 2

# 游戏窗口大小
SCREEN_WIDTH = BOARD_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = BOARD_SIZE * BOARD_WIDTH

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 创建窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("五子棋游戏")

# 游戏运行标志
running = True

# 记录棋盘状态
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
curr_player = 1


# 棋盘绘制函数
def draw_board():
    screen.fill((210, 180, 140))
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (BOARD_WIDTH // 2, BOARD_WIDTH // 2 + i * BOARD_WIDTH),
                         (SCREEN_WIDTH - BOARD_WIDTH // 2, BOARD_WIDTH // 2 + i * BOARD_WIDTH))
        pygame.draw.line(screen, BLACK, (BOARD_WIDTH // 2 + i * BOARD_WIDTH, BOARD_WIDTH // 2),
                         (BOARD_WIDTH // 2 + i * BOARD_WIDTH, SCREEN_HEIGHT - BOARD_WIDTH // 2))

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 1:
                pygame.draw.circle(screen, BLACK,
                                   (BOARD_WIDTH // 2 + i * BOARD_WIDTH, BOARD_WIDTH // 2 + j * BOARD_WIDTH),
                                   CHESS_RADIUS)
            elif board[i][j] == 2:
                pygame.draw.circle(screen, WHITE,
                                   (BOARD_WIDTH // 2 + i * BOARD_WIDTH, BOARD_WIDTH // 2 + j * BOARD_WIDTH),
                                   CHESS_RADIUS)

    pygame.display.update()


# 处理事件
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                i = (x - BOARD_WIDTH // 2) // BOARD_WIDTH
                j = (y - BOARD_WIDTH // 2) // BOARD_WIDTH
                if i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE or board[i][j] != 0:
                    continue
                board[i][j] = curr_player
                draw_board()
                if check_win(curr_player, i, j):
                    show_winner(curr_player)
                else:
                    switch_player()


# 切换玩家
def switch_player():
    global curr_player
    if curr_player == 1:
        curr_player = 2
    else:
        curr_player = 1


# 检查胜利条件
def check_win(player, x, y):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        for i in range(1, 5):
            new_x = x + dx * i
            new_y = y + dy * i
            if new_x < 0 or new_x >= BOARD_SIZE or new_y < 0 or new_y >= BOARD_SIZE or board[new_x][new_y] != player:
                break
            count += 1
        else:
            return True
    return False


# 显示胜利信息
def show_winner(player):
    if player == 1:
        winner = "黑棋"
        color = BLACK
    else:
        winner = "白棋"
        color = WHITE

    font = pygame.font.SysFont(None, 48)
    text = font.render(f"{winner}获胜！", True, color)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()


# 游戏循环
while running:
    handle_events()
