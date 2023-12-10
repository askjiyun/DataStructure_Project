# DataStructure_Project

## 사회적 약자들이 편리하게 관람할 수 있는 미술관 최적의 경로 탐색 ##
서울시립미술관 도면을 바탕으로 유모차 및 휠체어 이용방문객을 위한 미술관 지도를 재구성하여 보다 이용객들이 관람하기에 편리한 최단 경로 탐색해주는 알고리즘 작성

# museum.py 
- 새롭게 정의한 서울시립미술관 그래프를 바탕으로 유모차 및 휠체어 이용방문객들을 위한 전시실 관람 최단 경로 탐색 알고리즘 
- 계단이 아닌 엘리베이터를 무조건 이용해야 한다는 조건을 추가하여 알고리즘 작성
- 관람을 시작하고 싶은 전시실과 마지막으로 관람하고 싶은 전시실을 방문객에게 입력받아 최단 경로 탐색
- 최단경로 탐색을 위해 다익스트라 알고리즘 사용 -> 우선순위 큐 최소 힙을 사용하여 최단 거리와 최단 경로 탐색
- 최단 경로 출력을 위해 역추적을 통해 최단 경로 생성
- 완전 탐색을 통해서 모든 가능한 순서의 방문 경로를 생성해 가장 최적의 경로를 탐색 -> 다익스트라만으로는 부족
- 외판원 문제 TSP 알고리즘 + 다익스트라 알고리즘을 결합하여 문제 해결
- 
*외판원 문제 참고자료
https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search
https://buyandpray.tistory.com/52
https://dhalsdl12.tistory.com/17

# museumSolution.py
- museum.py import 하여 편의시설 추가 고려하여 탐색하는 알고리즘
- 이용객에게 관람을 시작할 전시실, 끝마칠 전시실, 방문하고 싶은 편의시설을 입력받아 기존 최단 경로에서 수유실, SeMA Cafe등 추가로 이용하고 싶은 편의시설을 고려한 최단 경로를 탐색해줍니다.
- find_shortest_path에 편의시설 경로만 추가한 코드 작성

# newMuseumMap.py
![image](https://github.com/askjiyun/DataStructure_Project/assets/104126233/ff0c63c9-b98c-42db-83e8-04a3f6e2ea33)

- 층별 도면 바탕으로 재구성한 Museum Graph 
- 거리를 일정 비율로 줄여서 가중치를 낮춰 임의 설정
- 주제 맞게 휠체어 이용객이나 어린이 방문객이 실제로 관람 경로에 있을 장소들만 선택하여 미술관 지도를 간략하게 생성
- 노드와 간선의 개수가 많아지면 알고리즘 탐색 시간이 늘어나 디버깅 시간 오래 걸리는 것 고려
- 층별 전시실 및 엘리베이터, 층별 화장실, 놀이방&수유실, SeMA Cafe, Rest Area만 고려

#서울시립미술관 서소문본관 층별 도면

![museum1F](https://github.com/askjiyun/DataStructure_Project/assets/104126233/52cb371c-37d2-495a-9af5-91b71f215da8)

![museum2F](https://github.com/askjiyun/DataStructure_Project/assets/104126233/29d64a0b-827c-43e4-b5ef-bf437317bdee)

![museum3F](https://github.com/askjiyun/DataStructure_Project/assets/104126233/58ac0b8b-2597-40b9-9398-7d373dfb0907)

# 층별 도면과 실제 방문 당시 전시 중이었던 작품들 데이터 수집하여 문제 설정에 맞는 새로운 Graph 생성
1층 전시실 : A Room으로 설정 ( 20작품 전시 )
2층 천경자 전시실 : B Room  (27개 작품)
2층 가나아트 컬렉션 전시실 : C Room -> 방문 당시 7080 도시현실 전시 중 (17개 작품) 
2층 전시실 : D Room (8개 작품)
3층 전시실 왼쪽 : E Room (6개 작품)
3층 전시실 오른쪽 : F Room (13개 작품) 

