from math import sqrt

def dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)

def entity_pos(room_pos, entity_pos, dim):
    r_x, r_y = room_pos
    e_x, e_y = entity_pos
    dim_x, dim_y = dim

    res_x = dim_x * r_x + e_x if r_x % 2 == 0 else dim_x * r_x + (dim_x - e_x)
    res_y = dim_y * r_y + e_y if r_y % 2 == 0 else dim_y * r_y + (dim_y - e_y)

    return (res_x, res_y)

def solution(dim, you, trainer, dist):
    dim_x, dim_y = dim
    m_x, m_y = you

    num_rooms_above_x = (dist + m_y) // dim_y + 1
    num_rooms_below_x = (dist - m_y) // dim_y + 1
    num_rooms_left_y = (dist - m_x) // dim_x + 1
    num_rooms_right_y = (dist + m_x) // dim_x + 1

    w = (num_rooms_right_y + num_rooms_left_y) * dim_x + 1
    h = (num_rooms_above_x + num_rooms_below_x) * dim_y + 1

    x_offset = num_rooms_left_y * dim_x
    y_offset = num_rooms_below_x * dim_y

    matrix = [[0] * h for _ in range(w)]
    for i in range(-num_rooms_left_y, num_rooms_right_y):
        for j in range(-num_rooms_below_x, num_rooms_above_x):
            tv_x, tv_y = entity_pos(trainer, [i, j], dim)
            mv_x, mv_y = entity_pos(you, [i, j], dim)
            matrix[tv_x + x_offset][tv_y + y_offset] = 1
            matrix[mv_x + x_offset][mv_y + y_offset] = 2

    hits = 0
    shots_taken = set()
    for i in range(-num_rooms_left_y, num_rooms_right_y):
        for j in range(-num_rooms_below_x, num_rooms_above_x):
            t_x, t_y = entity_pos(trainer, [i, j], dim)
            if dist([t_x, t_y], you) > dist:
                continue
            delta_y = t_y - m_y
            delta_x = t_x - m_x
            d = gcd(delta_y, delta_x)
            delta_y = int(delta_y / d)
            delta_x = int(delta_x / d)
            if (delta_y, delta_x) in shots_taken:
                continue
            shots_taken.add((delta_y, delta_x))
            ray_x, ray_y = m_x + x_offset, m_y + y_offset
            while 0 <= ray_x < w and 0 <= ray_y < h:
                ray_x += delta_x
                ray_y += delta_y
                entity = matrix[ray_x][ray_y]
                if entity == 1:
                    hits += 1
                    break
                elif entity == 2:
                    break
    return hits
 
