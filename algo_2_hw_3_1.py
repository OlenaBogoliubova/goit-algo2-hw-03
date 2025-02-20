import networkx as nx
import pandas as pd

def build_logistics_graph():
    G = nx.DiGraph()
    
    # Додавання ребер із пропускною здатністю
    edges = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 2", "Склад 3", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    return G

def compute_terminal_flows(G, terminal):
    """
    Обчислює потоки від конкретного термінала до магазинів
    """
    flow_values = {}
    for sink in [f"Магазин {i}" for i in range(1, 15)]:
        max_flow_value, flow_dict = nx.maximum_flow(G, terminal, sink)
        flow_values[sink] = max_flow_value

    return flow_values

if __name__ == "__main__":
    G = build_logistics_graph()
    
    # Обчислюємо потоки для кожного термінала
    terminal1_flows = compute_terminal_flows(G, "Термінал 1")
    terminal2_flows = compute_terminal_flows(G, "Термінал 2")

    # Формуємо таблицю
    data = []
    for store in range(1, 15):
        data.append(["Термінал 1", f"Магазин {store}", terminal1_flows[f"Магазин {store}"]])
        data.append(["Термінал 2", f"Магазин {store}", terminal2_flows[f"Магазин {store}"]])

    df = pd.DataFrame(data, columns=["Термінал", "Магазин", "Фактичний Потік (одиниць)"])
    
    # Виводимо таблицю результатів
    print(df.to_string(index=False))  # Виведе таблицю у вигляді тексту
