#!/usr/bin/python

import sys

diagram = []
for line in sys.stdin:
  diagram.append(line)

for c, d in enumerate(diagram[0]):
  if d == '|':
    col = c
    break

row = 0
direction = 'down'
count = 0
while True:
  
  curr = diagram[row][col]

  if curr == ' ':
    break
  
  count += 1

  if direction == 'down':
    if curr == '|':
      row += 1
    elif curr == '-':
      row += 1
    elif curr == '+':
      if col+1 < len(diagram[row]) and diagram[row][col+1] != ' ':
        col += 1
        direction = 'right'
      else:
        col -= 1
        direction = 'left'
    else:
      row += 1

  elif direction == 'up':
    if curr == '|':
      row -= 1
    elif curr == '-':
      row -= 1
    elif curr == '+':
      if col+1 < len(diagram[row]) and diagram[row][col+1] != ' ':
        col += 1
        direction = 'right'
      else:
        col -= 1
        direction = 'left'
    else:
      row -= 1

  elif direction == 'left':
    if curr == '|':
      col -= 1
    elif curr == '-':
      col -= 1
    elif curr == '+':
      if row+1 < len(diagram) and diagram[row+1][col] != ' ':
        row += 1
        direction = 'down'
      else:
        row -= 1
        direction = 'up'
    else:
      col -= 1

  elif direction == 'right':
    if curr == '|':
      col += 1
    elif curr == '-':
      col += 1
    elif curr == '+':
      if row+1 < len(diagram) and diagram[row+1][col] != ' ':
        row += 1
        direction = 'down'
      else:
        row -= 1
        direction = 'up'
    else:
      col += 1

print(count)
