with open('day03.txt') as myinput:
    wirepaths = myinput.read().split('\n')
wirepath1 = wirepaths[0].split(',')
wirepath2 = wirepaths[1].split(',')

def wireprog(wirepath):
    x = 0
    y = 0
    step = 0
    path = [[0,0]]
    pathstep = [[0,0,0]]
    for i in range(len(wirepath)):
        directionflag = wirepath[i][:1]
        if directionflag == 'R':
            for j in range(int(wirepath[i][1:])):
                x += 1
                step += 1
                path.append([x,y])
                pathstep.append([step,[x,y]])
        if directionflag == 'L':
            for j in range(int(wirepath[i][1:])):
                x += -1
                step += 1
                path.append([x,y])
                pathstep.append([step,[x,y]])
        if directionflag == 'U':
            for j in range(int(wirepath[i][1:])):
                y += 1
                step += 1
                path.append([x,y])
                pathstep.append([step,[x,y]])
        if directionflag == 'D':
            for j in range(int(wirepath[i][1:])):
                y += -1
                step += 1
                path.append([x,y])
                pathstep.append([step,[x,y]])
    return path[1:],pathstep[1:]

wirelist1 = wireprog(wirepath1)
wirelist2 = wireprog(wirepath2)

#Part 1
intersections_set = set(map(tuple, wirelist1[0])) & \
                    set(map(tuple, wirelist2[0]))
intersections = list(map(list, intersections_set))
distances = []
for i in range(len(intersections)):
    distances.append(sum([abs(j) for j in intersections[i]]))
print(min(distances))