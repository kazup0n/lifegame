# -*- coding: utf8 -*-
import random
import time

def init_cells(k):
    return [random.choices([True, False], k=k) for _ in range(k)]

def is_alive(cells, y, x):
    return cells[y][x]

def num_lives_of_neighbors(cells, y, x):
    h = K-1
    w = K-1
    lives = 0
    for dy in range(-1, 2):
        if y+dy > h or y+dy < 0:
            continue
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if x+dx > w or x+dx < 0:
                continue
            #print('{}({},{})'.format(cells[y+dy][x+dx], y+dy, x+dx))
            if is_alive(cells, y+dy, x+dx):
                lives += 1
    return lives

def next_state(cells, y, x):
    cell_alive = is_alive(cells, y, x)
    lives = num_lives_of_neighbors(cells, y, x)
    # 誕生 死んでいるセルに隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。
    if not cell_alive and lives == 3:
        return True
    # 生存 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する。
    if cell_alive and lives in [2, 3]:
        return True
    # 過疎 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する。
    if cell_alive and lives <= 1:
        return False
    # 過密 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する。
    if cell_alive and lives >= 4:
        return False
    return False

def next_gen(cells):
    next_cells = init_cells(K)
    for y in range(0, K):
        for x in range(0, K):
            next_cells[y][x] = next_state(cells, y, x)
    return next_cells

def print_cells(cells):
    print(chr(27) + "[2J")
    for y in range(0, K):
        for x in range(0, K):
            print('🐈' if cells[y][x] else '.', end='')
        print('')

GENERATIONS = 100
K=15

cells = init_cells(K)

for g in range(GENERATIONS):
    print_cells(cells)
    print('{}/{}'.format(g, GENERATIONS))
    time.sleep(0.5)
    cells = next_gen(cells)



