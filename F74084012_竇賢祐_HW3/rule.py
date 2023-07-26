"""
The template of the script for playing the game in the ml mode
"""


def get_command(head, food):
    distance_x = food[0] - head[0]
    distance_y = food[1] - head[1]
    if head[1] == 0:
        if head[0] == 0:
            command = "DOWN"
        else:
            command = "LEFT"
    elif head[0] == 290:
        command = "UP"
    else:
        # if eat:
        #    command = "RIGHT"
        if distance_x < 0 or distance_y < 0:
            command = "RIGHT"
        elif distance_x > distance_y:
            command = "RIGHT"
        else:
            command = "DOWN"
        # if ((head[0] + 10, head[1]) == food) or ((head[0], head[1] + 10) == food):
        #     #print("k")
        #     eat = True

    return command


class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        #self.eat = False
        pass

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        head = scene_info["snake_head"]
        food = scene_info["food"]
        body = scene_info["snake_body"]
        if scene_info["status"] == "GAME_OVER":
            #     print(head)
            #   print(food)
            #  print(body)
            return "RESET"
        #if head == (290, 0):
         #   self.eat = False
        # body_x = []
        # body_y = []
        # for i in range(len(body)):
        #     body_x.append(body[i][0])
        #     body_y.append(body[i][1])
        # command = "DOWN"
        # if food[0] < head[0]:
        #     command = "LEFT"
        # elif food[0] > head[0]:
        #     command = "RIGHT"
        # elif food[1] < head[1]:
        #     command = "UP"
        # elif food[1] > head[1]:
        #     command = "DOWN"
        # print(command , end = '  ')
        command = get_command(head, food)  # ,body,command)
        #print("self",self.eat)
        # command = get_command(head,food,body,command)
        # print(command, head)
        return command

    def reset(self):
        """
        Reset the status if needed
        """
        pass
