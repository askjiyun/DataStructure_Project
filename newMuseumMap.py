import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A Room': {'Rest Area': 8, 'SeMA Cafe': 7, 'Nursing Room': 2, '1F Restroom': 4, '1F Elevator': 3},
    'Rest Area': {'A Room': 8, 'SeMA Cafe': 1, 'Nursing Room': 3, '1F Restroom': 10, '1F Elevator': 2},
    'SeMA Cafe': {'A Room': 7, 'Rest Area': 1, 'Nursing Room': 2, '1F Restroom': 4, '1F Elevator': 1},
    'Nursing Room': {'A Room': 2, 'Rest Area': 3, 'SeMA Cafe': 2, '1F Restroom': 2, '1F Elevator': 1},
    '1F Restroom': {'A Room': 4, 'Rest Area': 10, 'SeMA Cafe': 4, 'Nursing Room': 2, '1F Elevator': 3},
    '1F Elevator': {'A Room': 3, 'Rest Area': 2, 'SeMA Cafe': 1, 'Nursing Room': 1, '1F Restroom': 3,'2F Elevator': 1},

    '2F Elevator': {'2F Restroom': 6, 'B Room': 2, 'C Room': 3, 'D Room': 7,'1F Elevator': 1,'3F Elevator': 1},
    '2F Restroom': {'2F Elevator': 6, 'B Room': 8, 'C Room': 9, 'D Room': 4},
    'B Room': {'2F Elevator': 2, '2F Restroom': 8, 'C Room': 1, 'D Room': 3},
    'C Room': {'2F Elevator': 3, '2F Restroom': 9, 'B Room': 1, 'D Room': 2},
    'D Room': {'2F Elevator': 7, '2F Restroom': 4, 'B Room': 3, 'C Room': 2},

    '3F Elevator': {'3F Restroom': 6, 'E Room': 4, 'F Room': 7,'2F Elevator': 1, '1F Elevator': 1},
    '3F Restroom': {'3F Elevator': 6, 'E Room': 8, 'F Room': 2},
    'E Room': {'3F Elevator': 4, '3F Restroom': 8, 'F Room': 3},
    'F Room': {'3F Elevator': 7, '3F Restroom': 2, 'E Room': 3},
}

# 그래프 생성
G = nx.Graph()

# 노드 및 엣지 추가
for node, edges in graph.items():
    G.add_node(node)
    for edge, weight in edges.items():
        G.add_edge(node, edge, weight=weight)

# 노드 및 엣지 위치 정의
pos = nx.spring_layout(G, k =0.1, seed=30)

# 노드 크기 설정
node_size = [G.degree(node) * 200 for node in G.nodes()]  # 연결된 엣지의 수에 따라 노드 크기 설정

# 엣지 가중치 표시
edge_labels = {(node, edge): weight['weight'] for node, edge, weight in G.edges(data=True)}

# 그래프 그리기
plt.figure(figsize=(15, 10))
# 노드 그리기 (노드 색상을 연결된 엣지의 수에 따라 변경)
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_size, cmap='viridis')
# 노드 레이블 그리기
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
# 엣지 그리기
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
# 엣지 레이블 (가중치) 그리기
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Museum Map")
plt.axis('off')
plt.show()