#!/usr/bin/python

import sys

pipes = {}
for line in sys.stdin:
  line = line.strip().split('/')
  l = (int(line[0]), int(line[1]))
  pipes[l] = []
  pipes[l[::-1]] = []

for pipe1 in pipes:
  for pipe2 in pipes:
    if pipe1 != pipe2 and pipe1 != pipe2[::-1] and pipe2[0] == pipe1[1]:
      pipes[pipe1].append(pipe2)

bridges = []
for i in range(1, len(pipes)+1):
  if i == 1:
    for pipe in pipes:
      b = []
      if pipe[0] == 0:
        b.append(pipe)
        bridges.append(b)
    continue
  for bridge in bridges:
    if len(bridge) == i-1:
      pipe1 = bridge[-1]
      for pipe2 in pipes[pipe1]:
        b = []
        for br in bridge:
          b.append(br)

        if pipe2 not in b and pipe2[::-1] not in b and 0 not in pipe2:
          b.append(pipe2)
          bridges.append(b)

max_sum = 0
for bridge in bridges:
  s = 0
  for pipe in bridge:
    s += sum(pipe)
  max_sum = max(s, max_sum)

print(max_sum)
