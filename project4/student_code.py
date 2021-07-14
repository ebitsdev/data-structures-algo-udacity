from queue import PriorityQueue
import math

def shortest_path(M, start, goal):
    # Create a priority queue to use
    rt_queue = PriorityQueue()
    # Add 0 as the first value to the priority queue
    rt_queue.put(start, 0)

    prev = {start: None }
    # Set 0 as the starting point
    starting_point = {start: 0}

    while not rt_queue.empty():
        current = rt_queue.get()
        # Check if current point/value is the goal
        if current == goal:
            # If it is then build the route the path
            build_rt(prev, start, goal)
        # Look for node items
        for n_item in M.roads[current]:
            # Update the starting point
            starting_point_up = starting_point[current] + utility_m(M.intersections[current], M.intersections[n_item])
            # Check if the node item is not in the starting point or if the updated starting_point is less than the starting object
            if n_item not in starting_point or starting_point_up < starting_point[n_item]:
                starting_point[n_item] = starting_point_up

                all_values = starting_point_up + utility_m(M.intersections[current],
                            M.intersections[n_item])
                # Update the queue
                rt_queue.put(n_item, all_values)
                # Set previous node to the current node
                prev[n_item] = current

    return build_rt(prev, start, goal)

# Utility function
def utility_m(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

# Build the route using previous, start point, and goal
def build_rt(prev, start, goal):
    current = goal
    route = [current]
    
    while current != start:
        current = prev[current]
        route.append(current)
    route.reverse()

    return route