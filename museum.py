import heapq
import itertools

# 각 전시실의 관람시간 (작품 당 시간 1만큼 걸린다고 설정)
viewing_time = {
    'A Room': 20,
    'B Room': 27,
    'C Room': 17,
    'D Room': 8,
    'E Room': 6,
    'F Room': 13,
}
# 층별 전시실 및 엘리베이터 정보
room_to_floor_and_elevator = {
    'A Room': ('1F', '1F Elevator'),
    'B Room': ('2F', '2F Elevator'),
    'C Room': ('2F', '2F Elevator'),
    'D Room': ('3F', '3F Elevator'),
    'E Room': ('3F', '3F Elevator'),
    'F Room': ('3F', '3F Elevator'),
    '1F Elevator': ('1F', '1F Elevator'),
    '2F Elevator': ('2F', '2F Elevator'),
    '3F Elevator': ('3F', '3F Elevator'),
}
def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}  # 이전 노드 기록

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight + viewing_time.get(neighbor, 0)

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # 이전 노드를 기록
                heapq.heappush(heap, (distance, neighbor))
    # 최단 경로 찾기
    path = []
    current_node = end
    while current_node is not None:  # 시작 노드까지 거슬러 올라가며 경로 생성
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]  #경로를 역순으로 생성

    return distances[end] if distances[end] != float('infinity') else None, path if path[0] == start else None
def find_shortest_path(graph, exhibition_rooms, start_point, end_point):
    # 모든 전시실의 순서를 고려한 경로
    all_paths = list(itertools.permutations(exhibition_rooms))

    # 각 경로에 대해 총 거리를 계산 후 가장 짧은 경로 선택
    shortest_distance = float('infinity')
    shortest_path = None
    for path in all_paths:
        total_distance = 0
        current_point = start_point
        current_path = [start_point]
        for room in path:
            # 현재 위치와 목표 전시실이 같은 층에 있는지 확인
            if room_to_floor_and_elevator[current_point][0] != room_to_floor_and_elevator[room][0]:
                # 같은 층에 없는 경우, 엘리베이터를 이용
                elevator = room_to_floor_and_elevator[room][1]
                distance, _ = dijkstra(graph, current_point, elevator)
                total_distance += distance if distance is not None else float('infinity')
                current_point = elevator
                if elevator not in current_path:
                    current_path.append(elevator)

            # 이제 해당 방으로 이동
            distance, _ = dijkstra(graph, current_point, room)
            if distance is None:  # 경로가 존재하지 않으면 계산을 중단
                break
            total_distance += distance
            current_point = room
            if room not in current_path:
                current_path.append(room)

        else:  # 모든 전시실을 방문한 후에는 끝점으로 돌아옴
            if room_to_floor_and_elevator[current_point][0] != room_to_floor_and_elevator[end_point][0]:
                # 현재 위치와 끝점이 같은 층에 없는 경우, 엘리베이터를 이용
                elevator = room_to_floor_and_elevator[end_point][1]
                distance, _ = dijkstra(graph, current_point, elevator)
                total_distance += distance if distance is not None else float('infinity')
                current_point = elevator
                if elevator not in current_path:
                    current_path.append(elevator)

            # 이제 끝점으로 이동 / 시작점 종료점 중복 제거
            if current_point != end_point:
                distance, _ = dijkstra(graph, current_point, end_point)
                total_distance += distance if distance is not None else float('infinity')
                if end_point not in current_path:
                    current_path.append(end_point)

            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = current_path

    return shortest_distance, shortest_path


# 미술관 그래프
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
exhibition_rooms = ['A Room', 'B Room', 'C Room', 'D Room', 'E Room', 'F Room']

# 사용자 입력 받기
start_point = input("관람을 시작할 전시실을 입력해주세요: ")
end_point = input("관람을 마칠 전시실을 입력해주세요: ")

if start_point not in exhibition_rooms or end_point not in exhibition_rooms:
    print("입력하신 전시실이 존재하지 않습니다. 다시 입력해주세요.")
else:
    # 최단 거리와 경로 계산
    shortest_distance, shortest_path = find_shortest_path(graph, exhibition_rooms, start_point, end_point)

    # 결과 출력
    if shortest_distance is not None and shortest_path is not None:
        print(f"전시실을 모두 관람하는 최단 경로: {' -> '.join(shortest_path)}")
        print(f"최단 거리(관람시간 포함): {shortest_distance}")
    else:
        print("전시실을 모두 관람하는 경로가 존재하지 않습니다.")
