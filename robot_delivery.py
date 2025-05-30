def solution(points, routes):
    
    field=[[0] * 101 for _ in range(101)] #field 초기화 
    
    for route in routes:  #routes를 실좌표로 바꿈
        route[0] = points[route[0] - 1]
        route[1] = points[route[1] - 1]
    
    num_of_robots = len(routes)
    
    possible_accidents = 0
    
    robots_location = [routes[i][0] for i in range(num_of_robots)] #로봇별 위치 초기화
    for i in range(num_of_robots):    #필드 상의 위치 초기화
        r_r = robots_location[i][0]
        r_c = robots_location[i][1]
        if field[r_r][r_c] == 1:
            possible_accidents += 1
            field[r_r][r_c] += 1
        else:
            field[r_r][r_c] += 1
    
    sequence = [[] * num_of_robots] #로봇별 이동방법 
    for r in range(num_of_robots):
        for p in range(r):
            if p == len(routes[r]) - 1:
                break
            r_move = routes[r][p+1][0] - routes[r][p][0]
            c_move = routes[r][p+1][1] - routes[r][p][1]
            sequence[r].append([r_move, c_move]) 
    si = [[0] for _ in range(num_of_robots)]
    finished = [0] * num_of_robots #일을 끝낸 로봇의 수
    time = 0
    
    while(1):
        ind = 0
        for i in range(num_of_robots):
            ind += finished[i]
        if ind == num_of_robots:
            break
        for i in range(num_of_robots):
            if si[i] > len(sequence[i]):
                finished[i] = 1
                continue
            r_r = robots_location[i][0]
            r_c = robots_location[i][1]
            if sequence[i][si[i]][0] > 0:
                sequence[i][si[i]][0] -= 1
                field[r_r][r_c] -= 1
                if field[r_r+1][r_c] == 1:
                    possible_accidents += 1
                    field[r_r+1][r_c] += 1
                else:
                    field[r_r+1][r_c] += 1
            elif sequence[i][si[i]][0] > 0:
                sequence[i][si[i]][0] += 1
                field[r_r][r_c] -= 1
                if field[r_r+1][r_c] == 1:
                    possible_accidents += 1
                    field[r_r+1][r_c] -= 1
                else:
                    field[r_r+1][r_c] -= 1
            else:
                if sequence[i][si[i]][1] > 0:
                    sequence[i][si[i]][1] -= 1
                    field[r_r][r_c] -= 1
                    if field[r_r][r_c+1] == 1:
                        possible_accidents += 1
                        field[r_r][r_c+1] += 1
                    else:
                        field[r_r][r_c+1] += 1
                elif sequence[i][si[i]][1] < 0:
                    sequence[i][si[i]][1] += 1
                    field[r_r][r_c] -= 1
                    if field[r_r][r_c+1] == 1:
                        possible_accidents += 1
                        field[r_r][r_c+1] -= 1
                    else:
                        field[r_r][r_c+1] -= 1
                else:
                    si[i] += 1
            
    answer = possible_accidents
    return answer

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [2, 4]]

solution(points, routes)