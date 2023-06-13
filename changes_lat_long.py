# import random


# def changes_in_lat_log(n):
#      random_digits = ''.join([str(random.randint(0, 10)) for i in range(13)])
#      n_modified = n[:-9] + random_digits
#      return  n_modified


# def main():
#     y = 41.73128821377282
#     number =  changes_in_lat_log(y)
#     print('number',number)
    


# if __name__ == '__main__':
#     main()

 # this is a convert to a string , for our use the float 
import random

def changes_in_lat_log(n):
    random_digits = ''.join([str(random.randint(0, 10)) for i in range(13)])
    n_str = str(n)  # Convert the float to a string
    n_modified = n_str[:-9] + random_digits
    return n_modified


def main():
    y = 41.73128821377282
    number = changes_in_lat_log(y)
    print('number', number)


if __name__ == '__main__':
    main()





"""   this was the function call. 
        def create_moving_object_list(amount: int, object_types: List):
    
            Args:
            amount (int): amount of random objects to generate

        Returns:
            list: contains all of the moving objects for the Cognata formula.
    
        global starting_point
        # if amount >= 1200:
        #     amount = 1199
        list = []
        points = pick_random_point(1199)
        try:
            i = 0
            while i < amount:
                coords = points[i]
                # adding here for changes in the lat and log -> to get barrels in the mid of the lane (not only on lines).
                coords[0] = changes_in_lat_log(coords[0]) ###$$$$$$$$$$$$$$$$$ the call for our cahnges in the lat and long #### $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
                coords[1] = changes_in_lat_log(coords[1])

                dist = distance.distance((starting_point[0][0], starting_point[0][1]),(coords[0], coords[1])).meters # Distance between barrel and starting location

                if(dist > MIN_DISTANCE_GENERATION and dist < MAX_DISTANCE_GENERATION):
                    list.append(create_moving_object(f'Moving object #{i}', f'moving_object_{i}', float(coords[0]), float(coords[1]), (random.choice(object_types))))
                    # print(f'Moving object #{i}', f'moving_object_{i}', coords[0], coords[1])
                else: amount = amount+1
                i = i+1
        except IndexError:
            pass
        return list

        ************************************************************************************************************************************
        # the function in the page it self . 
        def changes_in_lat_log(n):
            random_digits = ''.join([str(random.randint(0, 10)) for i in range(13)])
            n_modified = n[:-9] + random_digits
            return  n_modified


"""
