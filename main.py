def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    
while not at_goal():
    if not right_is_clear() and not wall_in_front():
        move()
        if not wall_in_front() and not right_is_clear():
            turn_left()
            move()
        elif not wall_in_front():
            move_right()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
    elif not front_is_clear() and right_is_clear():
        move_right()
    elif not front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear() and front_is_clear:
        move()
        if front_is_clear():
            move()
        turn_left()
        
    elif not wall_in_front():
        move_right()