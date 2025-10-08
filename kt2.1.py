class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        for i in range(len(self.items)-1, 0, -1):
            if self.items[i].freq < self.items[i-1].freq:
                self.items[i], self.items[i-1] = self.items[i-1], self.items[i]
            else:
                break
    
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.codes = {}
        self.root = self.build_tree()
        if self.root:
            self.build_codes(self.root, "")
    
    def frequency(self):
        freq = {}
        for char in self.text:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq
    
    def build_tree(self):
        if not self.text:
            return None
            
        freq = self.frequency()
        queue = PriorityQueue()
        
        for char, count in freq.items():
            queue.push(Node(char, count))
        
        while queue.size() > 1:
            left = queue.pop()
            right = queue.pop()
            
            merged = Node(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            queue.push(merged)
        
        return queue.pop()
    
    def build_codes(self, node, current_code):
        if node is None:
            return
        
        if node.char is not None:
            self.codes[node.char] = current_code
            return
        
        self.build_codes(node.left, current_code + "0")
        self.build_codes(node.right, current_code + "1")
    
    def encode_text(self):
        encoded = ""
        for char in self.text:
            encoded += self.codes[char]
        return encoded
    
    def calculate_bits(self):
        return len(self.encode_text())
    
    def display_char(self, char):
        if char == ' ':
            return 'ПРОБЕЛ'
        return f"'{char}'"
    
    def print_tree(self):
        if not self.root:
            print("Дерево пустое")
            return
        
        print("\n" + "="*50)
        print("ДЕРЕВО ХАФФМАНА:")
        print("="*50)
        self.print_tree_node(self.root, 0, "")
    
    def print_tree_node(self, node, level, code):
        if node is None:
            return
        
        indent = "  " * level
        
        if node.char is not None:
            char_display = self.display_char(node.char)
            print(f"{indent}{char_display}:{node.freq}({code})")
        else:
            print(f"{indent}*:{node.freq}({code})")
        
        if node.left:
            self.print_tree_node(node.left, level + 1, code + "0")
        if node.right:
            self.print_tree_node(node.right, level + 1, code + "1")
    
    def print_codes(self):
        print("\n" + "="*50)
        print("КОДЫ ХАФФМАНА:")
        print("="*50)
        
        if not self.codes:
            print("Нет кодов для отображения")
            return
        
        codes_list = []
        for char, code in self.codes.items():
            codes_list.append((char, code))
        
        for i in range(len(codes_list)):
            for j in range(i + 1, len(codes_list)):
                if (len(codes_list[i][1]) > len(codes_list[j][1]) or 
                    (len(codes_list[i][1]) == len(codes_list[j][1]) and codes_list[i][1] > codes_list[j][1])):
                    codes_list[i], codes_list[j] = codes_list[j], codes_list[i]
        
        for char, code in codes_list:
            freq = self.text.count(char)
            char_display = self.display_char(char)
            print(f"Символ: {char_display:>8} | Частота: {freq:2d} | Код: {code:8s} | Длина: {len(code)} бит")
    
    def print_statistics(self):
        if not self.text:
            print("Текст пустой")
            return
        
        encoded_text = self.encode_text()
        original_bits = len(self.text) * 8
        compressed_bits = self.calculate_bits()
        print(f"Длина текста: {len(self.text)} символов")
        print(f"Исходный размер (бит): {original_bits}")
        print(f"Закодированный размер (бит): {compressed_bits}")
        print(f"Экономия: {original_bits - compressed_bits} бит")

if __name__ == "__main__":
    
    print("ПРОГРАММА КОДИРОВАНИЯ ХАФФМАНА")
    print("="*50)
    print("Для ввода пробела как символа используйте обычный пробел")
    print("="*50)
    
    alphabet = input("Введите алфавит (включая пробелы): ")
    text = input("Введите текст для кодирования: ")
    
    for char in text:
        if char not in alphabet:
            print(f"Ошибка: символ '{char}' отсутствует в алфавите!")
    
    huffman = HuffmanTree(text)
    huffman.print_tree()
    huffman.print_codes()
    huffman.print_statistics()
