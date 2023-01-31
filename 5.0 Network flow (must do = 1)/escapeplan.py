
def bpm(graph, u, matchR, seen):

    for v in range(len(graph[0])):

        if graph[u][v] and not seen[v]:

            seen[v] = True

            if matchR[v] == -1 or bpm(graph, matchR[v],
                                      matchR, seen):
                matchR[v] = u
                return True
    return False


# Returns the maximum flow and residual graph from s to t in the given graph
def ford_fulkerson(graph):
    matchR = [-1] * len(graph[0])

    result = 0
    for i in range(len(graph)):


        seen = [False] * len(graph[0])


        if bpm(graph, i, matchR, seen):
            result += 1

    return result


def calculate_distance(x1, y1, x2, y2):
    dist = pow(x1 - x2, 2) + pow(y1 - y2, 2)
    return dist


def initial_setup():
    scenario = [5, 10, 20]
    t = 1
    while True:

        total_robots = int(input())
        if total_robots == 0:
            break

        print("Scenario " + str(t))

        robots = []

        for r in range(total_robots):
            word = input().strip().split()  # [0] start [1] end
            newW = [float(x) / 10 for x in word]
            robots.append(newW)

        total_hide_spots = int(input())
        hide_spots = []

        for h in range(total_hide_spots):
            word = input().strip().split()  # [0] start [1] end
            newW = [float(x) / 10 for x in word]
            hide_spots.append(newW)

        for s in range(len(scenario)):

            graph = [[0 for _ in range(total_hide_spots)]
                     for _ in range(total_robots)]

            for x in range(total_robots):
                for y in range(total_hide_spots):
                    if calculate_distance(robots[x][0], robots[x][1], hide_spots[y][0],
                                          hide_spots[y][1]) <= (scenario[s] * scenario[s]):
                        # generate arch between robot and hide spot
                        graph[x][y] = 1
            max_path = ford_fulkerson(graph)
            print("In " + str(scenario[s]) + " seconds " + str(max_path) + " robot(s) can escape")
        t = t + 1
        print("")


initial_setup()
