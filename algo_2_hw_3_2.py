import csv
import timeit
from BTrees.OOBTree import OOBTree

# Функція для завантаження даних із CSV
def load_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['ID'] = int(row['ID'])
            row['Price'] = float(row['Price'])
            data.append(row)
    return data

# Функція для додавання товару у OOBTree
def add_item_to_tree(tree, item):
    tree[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}

# Функція для додавання товару у dict
def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}

# Функція для діапазонного запиту у OOBTree
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items(min_price, max_price)]

# Функція для діапазонного запиту у dict
def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]

if __name__ == "__main__":
    filename = r"C:\Users\Elena\Desktop\MasterIT\Tier 1 Math\Algorithm\Algo2\generated_items_data.csv"
    data = load_data(filename)
    
    # Ініціалізація структур даних
    tree = OOBTree()
    dictionary = {}
    
    # Додавання даних
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)
    
    # Визначаємо межі діапазону
    min_price, max_price = 10.0, 50.0  # Замініть на реальні значення
    
    # Вимірюємо продуктивність OOBTree
    time_tree = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    
    # Вимірюємо продуктивність dict
    time_dict = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)
    
    # Вивід результатів
    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")