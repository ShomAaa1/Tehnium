from collections import deque

def enqueue(q: deque, item): #функция добавления элемента в очередь
    q.append(item) # добавляем в конец очереди
    print(f'Добавлен {item}, очередь:', q)


def dequeue(q: deque): # функция извлечения элемента из очереди
    if q: # проверяем, что очередь не пустая
        item = q.popleft() # удаляем из начала очереди
        print(f'Извлечен {item}, очередь:', q)
        return item
    else:
        print('Очередь пуста')
        return None


queue = deque()
enqueue(queue, 'A')
enqueue(queue, 'B')
enqueue(queue, 'C')

dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)