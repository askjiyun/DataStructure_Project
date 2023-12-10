import itertools
from museum import dijkstra, exhibition_rooms, graph, room_to_floor_and_elevator

# 층별 전시실 및 엘리베이터 정보
room_to_floor_and_elevator = {
    'A Room': ('1F', '1F Elevator'),
    'B Room': ('2F', '2F Elevator'),
    'C Room': ('2F', '2F Elevator'),
    'D Room': ('3F', '3F Elevator'),
    'E Room': ('3F', '3F Elevator'),
    'F Room': ('3F', '3F Elevator'),
    'Rest Area': ('1F', '1F Elevator'),
    'SeMA Cafe': ('1F', '1F Elevator'),
    'Nursing Room': ('1F', '1F Elevator'),
    '1F Restroom': ('1F', '1F Elevator'),
    '2F Restroom': ('2F', '2F Elevator'),
    '3F Restroom': ('3F', '3F Elevator'),
    '1F Elevator': ('1F', '1F Elevator'),
    '2F Elevator': ('2F', '2F Elevator'),
    '3F Elevator': ('3F', '3F Elevator'),
}

#museum.py에서 선택한 편의시설 고려하여 최단 경로 탐색
def find_shortest_path(graph, exhibition_rooms, start_point, end_point, selected_facilities):
    all_nodes = list(graph.keys())
    #편의시설 추가 탐색하는 코드
    facilities = [facility.strip() for facility in selected_facilities.split(",")]

    for facility in facilities:
        if facility not in all_nodes:
            return None, None

    all_stops = exhibition_rooms + facilities
    shortest_distance = float('infinity')
    shortest_path = None

    for path in itertools.permutations(all_stops):
        total_distance = 0
        current_point = start_point
        current_path = [start_point]
        for node in path:
            # 현재 위치와 목표 전시실이 같은 층에 있는지 확인
            if room_to_floor_and_elevator[current_point][0] != room_to_floor_and_elevator[node][0]:
                # 같은 층에 없는 경우, 엘리베이터를 이용
                elevator = room_to_floor_and_elevator[node][1]
                distance, _ = dijkstra(graph, current_point, elevator)
                total_distance += distance if distance is not None else float('infinity')
                current_point = elevator
                if elevator not in current_path:
                    current_path.append(elevator)

            # 이제 해당 방으로 이동
            distance, _ = dijkstra(graph, current_point, node)
            if distance is None:  # 경로가 존재하지 않으면 계산을 중단
                break
            total_distance += distance
            current_point = node
            if node not in current_path:
                current_path.append(node)
        else:
            distance, _ = dijkstra(graph, current_point, end_point)
            if distance is not None:
                total_distance += distance
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = current_path

    return shortest_distance, shortest_path


# 사용자 입력 받기
start_room = input("관람을 시작할 전시실을 입력해주세요: ")
end_room = input("관람을 마칠 전시실을 입력해주세요: ")
selected_facilities = input("방문하고 싶은 편의시설을 입력하세요 (쉼표로 구분): ")

# 최단 거리와 경로 계산
shortest_distance, shortest_path = find_shortest_path(graph, exhibition_rooms, start_room, end_room, selected_facilities)

# 결과 출력
if shortest_distance is not None and shortest_path is not None:
    print(f"선택한 편의시설을 포함한 최단 경로: {' -> '.join(shortest_path)}")
    print(f"최단 거리(관람시간 포함): {shortest_distance}")
else:
    print("경로를 찾을 수 없습니다.")





