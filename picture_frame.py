def create_picture_frame(width, height, char):
    """
    creates frame of given width and height using given character
    """
    try: 
        w = int(width)
    except:
        print ('invalid')
        return []

    try:
        h = int(height)
    except:
        print ('invalid')
        return []

    if not (w > 2 and h > 2):
        print ('invalid!')
        return []
    
    picture_frame = []
    firstlastline = []

    for i in range(w):
        firstlastline.append(char)
    picture_frame.append(firstlastline)

    for i in range(h - 2):
        middleline = []
        middleline.append(char)
        for j in range (w - 2):
            middleline.append(" ")
        middleline.append(char)
        picture_frame.append(middleline)
    
    picture_frame.append(firstlastline)

    return picture_frame


def print_picture_frame(picture_frame):
    """
    prints frame of given width and height using given character
    
    print_picture_frame(create_picture_frame(5, 5, #))
    #####
    #   #
    #   #
    #   #
    #####

    print_picture_frame(create_picture_frame(8, 4, &))
    &&&&&&&&
    &      &
    &      &
    &&&&&&&&
    """
    for line in picture_frame:
        for character in line:
            print(character, end="")
        print("")

if __name__ == "__main__":
    width = input('enter a width: ')
    height = input('enter a height: ')
    char = input('enter a character: ')
    print_picture_frame(create_picture_frame(width, height, char))




