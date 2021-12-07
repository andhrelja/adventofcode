import numpy as np

input_directions = [
    {
        'value': 1,
        'from': (1,0),
        'to': (4,3)
    },
    {
        'value': 1,
        'from': (4,3),
        'to': (1,0)
    },
    {
        'value': 2,
        'from': (8,0),
        'to': (5,3)
    },
    {
        'value': 2,
        'from': (5,3),
        'to': (8,0)
    },
    {
        'value': 3,
        'from': (4,4),
        'to': (1,7)
    },
    {
        'value': 3,
        'from': (1,7),
        'to': (4,4)
    },
    {
        'value': 4,
        'from': (5,4),
        'to': (8,7)
    },
    {
        'value': 4,
        'from': (8,7),
        'to': (5,4)
    }
]

input_shape = (10, 10)
matrix = np.full(shape=input_shape, fill_value=0)

for direction in input_directions:
    y1, x1 = direction['from']
    y2, x2 = direction['to']
    
    if x1 == x2:
        # vertical
        if y1 > y2:
            # right - left
            line = range(y1, y2, -1)
        else:
            line = range(y1, y2)
        
        for i in line:
            matrix[x1][i] = direction['value']
        
    elif y1 == y2:
        # horizontal
        if x1 > x2:
            # down - up
            line = range(x1, x2, -1)
        else:
            line = range(x1, x2)
        
        for i in line:
            matrix[i][y1] = direction['value']
        
    elif x1 == y1 and x2 == y2:
        # main diagonal
        if x1 > x2:
            # right - left
            line = range(x1, x2, -1)
        else:
            line = range(x1, x2)
        
        for i in line:
            matrix[i][i] = direction['value']
        
    elif x1 == y2 and x2 == y1:
        # main diagonal 
        if x1 > x2:
            # right - left
            line = range(x1, x2, -1)
            for i in line:
                matrix[x1-i][y1+i] = direction['value']
        else:
            line = range(x1, x2)
            for i in line:
                matrix[x1+i][y1-i] = direction['value']
        
    else:
        if x1 > x2:
            line = range((x1 - x2)+1)
            if y1 > y2:
                # (3, 4) -> (0, 1)
                for i in line:
                    matrix[x1-i][y1-i] = direction['value']
            else:
                # (3, 5) -> (0, 8)
                for i in line:
                    matrix[x1-i][y1+i] = direction['value']
        else:
            line = range((x2 - x1)+1)
            if y1 > y2:
                # (0, 8) -> (3, 5)
                for i in line:
                    matrix[x1+i][y1-i] = direction['value']
            else:
                # (0, 1) -> (3, 4)
                for i in line:
                    matrix[x1+i][y1+i] = direction['value']
        
print(matrix)

"""
if x1 == x2:
    # vertical
    if y1 > y2:
        # right - left
    else:
        # left - right
    
elif y1 == y2:
    # horizontal
    if x1 > x2:
        # down - up
    else:
        # up - down
    
elif x1 == y1 and x2 == y2: # (0, 0) -> (9, 9)
    # main diagonal
    if x1 > x2:
        # right - left
    else:
        # left - right
    
elif x1 == y2 and x2 == y1: # (0, 9) -> (9, 0)
    # main diagonal 
    if x1 > x2:
        # right - left
    else:
        # left - right
    
else:
    if x1 > x2:
        if y1 > y2:
            # southeast -> northwest
        else:
            # southwest -> northeast
    else:
        if y1 > y2:
            # northeast -> southwest
        else:
            # nortwest -> southeast
"""