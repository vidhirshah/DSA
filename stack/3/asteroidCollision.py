def asteroidCollision( asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        if a > 0:
            stack.append(a)
        else:
            while len(stack) != 0 and a < 0 and stack[-1] > 0:
                if -(a) > stack[-1]:
                    stack.pop()
                    continue
                elif -(a) == stack[-1]:
                    stack.pop()
            else:
                stack.append(a)

    return stack
    

asteroids = [-2,1,1,-2]
print(asteroidCollision(asteroids))