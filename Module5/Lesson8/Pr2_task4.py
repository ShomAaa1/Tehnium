from collections import deque

deque1 = deque()
print('Старт:', deque1)
deque1.append('A')
print('После append("A"):', deque1)
deque1.append('B')
print('После append("B"):', deque1)
deque1.appendleft('C')
print('После appendleft("C"):', deque1)
right = deque1.pop()
print(f'После pop() (удалили {right}):', deque1)
left=deque1.popleft()
print(f'После popleft() (удалили {left}):', deque1)