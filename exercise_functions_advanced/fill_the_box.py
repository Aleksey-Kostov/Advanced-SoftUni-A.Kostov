def fill_the_box(hight, length, width, *args):
    volume = hight * length * width
    cubs_left = 0
    for element in args:
        if element == 'Finish':
            break
        if element > volume:
            element -= volume
            cubs_left += element
            volume = 0
        else:
            volume -= element

    if volume > 0:
        return f'There is free space in the box. You could put {volume} more cubes.'
    else:
        return f'No more free space! You have {cubs_left} more cubes.'
