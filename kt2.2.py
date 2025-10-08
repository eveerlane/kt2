#Перцев Александр ИТ-6 КТ2.2

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = []
    
    def add_row(self, row):
        self.matrix.append(row)
    
    def dijkstra(self, start, end):
        INF = 10**9
        dist = [INF] * self.n
        dist[start] = 0
        visited = [False] * self.n
        
        unvisited = [i for i in range(self.n)]
        
        while unvisited:
            min_dist = INF
            st_point = -1
            
            for i in unvisited:
                if dist[i] < min_dist:
                    min_dist = dist[i]
                    st_point = i
            if st_point == -1 or st_point == end:
                break
            
            unvisited.remove(u)

            for v in range(self.n):
                if self.matrix[st_point][v] != 0 and v in unvisited:
                    new_dist = dist[st_point] + self.matrix[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
        
        return dist[end]

def get_positive_int(prompt, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Ошибка: число должно быть положительным!")
                continue
            if max_value is not None and value > max_value:
                print(f"Ошибка: число не должно превышать {max_value}!")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число!")

def get_matrix_row(n, row_num):
    while True:
        try:
            row_input = input(f"Введите {n} чисел для строки {row_num + 1}: ")
            row = list(map(int, row_input.split()))
            
            if len(row) != n:
                print(f"Ошибка: нужно ввести ровно {n} чисел!")
                continue
            
            if row[row_num] != 0:
                print("Ошибка: на главной диагонали должны быть нули!")
                continue
            
            has_negative = False
            for weight in row:
                if weight < 0:
                    has_negative = True
                    break
            
            if has_negative:
                print("Ошибка: веса ребер не могут быть отрицательными!")
                continue
            
            for weight in row:
                if abs(weight) > 100:
                    print("Ошибка: вес ребра не должен превышать 100 по модулю!")
                    continue
            
            return row
            
        except ValueError:
            print("Ошибка: введите целые числа, разделенные пробелами!")

if __name__ == "__main__":
    print("=" * 50)
    print("ПОИСК КРАТЧАЙШЕГО ПУТИ В ГРАФЕ")
    print("=" * 50)
    
    N = get_positive_int("Введите количество пунктов N (1-100): ", 100)
    
    while True:
        try:
            K = int(input("Введите номер пункта K: "))
            if K < 1 or K > N:
                print(f"Ошибка: номер пункта должен быть от 1 до {N}!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
    
    while True:
        try:
            M = int(input("Введите номер пункта M: "))
            if M < 1 or M > N:
                print(f"Ошибка: номер пункта должен быть от 1 до {N}!")
                continue
            if M == K:
                print("Ошибка: пункты K и M не должны совпадать!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
    
    K -= 1
    M -= 1
    
    print(f"\nВведите матрицу смежности {N}xN:")
    print("Правила:")
    print("- На главной диагонали должны быть нули")
    print("- Веса ребер неотрицательные")
    print("- Веса по модулю не превышают 100")
    print("- 0 означает отсутствие пути")
    print("- Числа вводятся через пробел")
    print("- Каждая строка матрицы вводится отдельно")
    print("- j-ое число в i-ой строке - вес ребра из вершины i в вершину j")
    
    graph = Graph(N)
    
    for i in range(N):
        row = get_matrix_row(N, i)
        graph.add_row(row)
    
    result = graph.dijkstra(K, M)
    
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ:")
    print("=" * 50)
    
    if result == 10**9:
        print(f"Путь из пункта {K+1} в пункт {M+1} не существует!")
    else:
        print(f"Кратчайший путь из пункта {K+1} в пункт {M+1}: {result}")
        
        
'''
==================================================
ПОИСК КРАТЧАЙШЕГО ПУТИ В ГРАФЕ
==================================================
Введите количество пунктов N (1-100): 5
Введите номер пункта K: 1
Введите номер пункта M: 5

Введите матрицу смежности 5xN:
Правила:
- На главной диагонали должны быть нули
- Веса ребер неотрицательные
- Веса по модулю не превышают 100
- 0 означает отсутствие пути
- Числа вводятся через пробел
- Каждая строка матрицы вводится отдельно
- j-ое число в i-ой строке - вес ребра из вершины i в вершину j
Введите 5 чисел для строки 1: 0 10 0 20 0
Введите 5 чисел для строки 2: 20 0 30 0 40
Введите 5 чисел для строки 3: 0 50 0 60 0
Введите 5 чисел для строки 4: 70 0 80 0 90
Введите 5 чисел для строки 5: 0 10 0 20 0

==================================================
РЕЗУЛЬТАТ:
==================================================
Кратчайший путь из пункта 1 в пункт 5: 50
'''
