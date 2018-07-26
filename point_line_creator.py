import random

def create_points_from_line(m, b, num_points, noise):
    counter = 0
    points = []
    while counter <= num_points:
        x = random.randint(-90, 90) 
        y = (m * x) + b
        updated_noise = random.randrange(-1, 1, 1) * noise
        points.append(((x + updated_noise),(y + updated_noise))) 
        counter += 1
    return points
