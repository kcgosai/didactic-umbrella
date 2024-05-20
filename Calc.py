from collections import deque

def find_steps(A, B, C):
    if B <= A <= C:
        return [f"{A} is already within the range {B}-{C}"]

    operations = ['+', '-', '*', '/']
    queue = deque([(A, [])])
    visited = set([A])

    while queue:
        current, steps = queue.popleft()
        
        for number in range(1, 10):
            for operation in operations:
                if operation == '+':
                    next_value = current + number
                elif operation == '-':
                    next_value = current - number
                elif operation == '*':
                    next_value = current * number
                elif operation == '/' and number != 0:
                    next_value = current / number
                
                if next_value not in visited:
                    visited.add(next_value)
                    new_steps = steps + [f"{current} {operation} {number} = {next_value}"]
                    
                    if B <= next_value <= C:
                        return new_steps
                    
                    queue.append((next_value, new_steps))
    
    return ["No solution found"]

# Example usage
A = 10
B = 15
C = 20
steps = find_steps(A, B, C)
for step in steps:
    print(step)
