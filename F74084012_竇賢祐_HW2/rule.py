"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.frame = 0
        self.frame_cnt = 0
        self.c = 1
        self.pre_blocker = 0

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            print(scene_info["ball_speed"])
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            self.frame = scene_info["frame"]
            return "SERVE_TO_RIGHT"
        else:
            ballX = scene_info["ball"][0]
            ballY = scene_info["ball"][1]
            ball_Speed_X = scene_info["ball_speed"][0]
            ball_Speed_Y = scene_info["ball_speed"][1]
            blocker_speed = scene_info["blocker"][0] - self.pre_blocker
            blockerX = scene_info["blocker"][0]
            blockerY = scene_info["blocker"][1]
            plat1X = scene_info["platform_1P"][0]
            plat2X = scene_info["platform_2P"][0]
            self.frame_cnt = scene_info["frame"]
            """slide = ball_Speed_Y/ball_Speed_X
            if ballY < blockerY:
                for i in range(30):
                    ballY += ball_Speed_Y
                    ballX += ball_Speed_X
                    if ballX <= 0 or ballX >= 195:
                        ball_Speed_X = -ball_Speed_X
                    if ballY <= 80 and self.side == "2P":
                        break
            if ballY > blockerY + 20 :
                for i in range(30):
                    ballY += ball_Speed_Y
                    ballX += ball_Speed_X
                    if ballX <= 0 or ballX >= 195:
                        ball_Speed_X = -ball_Speed_X
                    if ballY >= 415 and self.side == "1P":
                        break

            if self.side == "2P" and scene_info["ball"][1] < blockerY:
                if ballX > plat2X + 23 :
                    return "MOVE_RIGHT"
                elif ballX < plat2X + 17:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            elif self.side == "2P" and scene_info["ball"][1] > blockerY:
                if plat2X < 80 :
                    return "MOVE_RIGHT"
                elif plat2X > 120:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            elif self.side == "1P" and scene_info["ball"][1] > blockerY:
                if ballX > plat1X + 23:
                    return "MOVE_RIGHT"
                elif ballX < plat1X + 17:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            elif self.side == "1P" and scene_info["ball"][1] < blockerY:
                if plat1X < 80 :
                    return "MOVE_RIGHT"
                elif plat1X > 120:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            """
            # if self.side == "1P":
            #     print(blockerX,end = "  ")
            for i in range(200):
                if ((self.frame_cnt - self.frame) // 100) == self.c:
                    if ball_Speed_Y < 0:
                        ball_Speed_Y -= 1
                    else:
                        ball_Speed_Y += 1
                    if ball_Speed_X < 0:
                        ball_Speed_X -= 1
                    else:
                        ball_Speed_X += 1
                    self.c += 1
                self.frame_cnt += 1
                ballX += ball_Speed_X
                ballY += ball_Speed_Y
                # if self.side == "1P":
                #     print(blockerX, end = '  ')
                if blocker_speed != 0:
                    blockerX += blocker_speed
                    if blockerX >= 170:
                        blockerX = 170
                        blocker_speed = -blocker_speed
                    elif blockerX <= 0:
                        blockerX = 0
                        blocker_speed = -blocker_speed
                # hit the blocker bottom
                if blockerX - 5 < ballX <= blockerX + 30 and ballY <= blockerY + 20 < (ballY - ball_Speed_Y) and ball_Speed_Y < 0 and \
                        blockerX - (blockerY + 20 - (ballY - ball_Speed_Y))\
                          <= (ballX - ball_Speed_X) <= blockerX + 30 + (blockerY + 20 - (ballY - ball_Speed_Y)):
                    #print("bottom")
                    ball_Speed_Y = -ball_Speed_Y
                    ballY = blockerY + 20

                    # hit the blocker up
                elif blockerX - 5 < ballX <= blockerX + 30 and ballY + 5 >= blockerY > (ballY + 5 - ball_Speed_Y) and ball_Speed_Y > 0 and \
                        blockerX - (blockerY - (ballY - ball_Speed_Y))\
                          <= (ballX - ball_Speed_X) <= blockerX + 30 + (blockerY - (ballY - ball_Speed_Y)):
                    #print("upper")
                    ball_Speed_Y = -ball_Speed_Y
                    ballY = blockerY - 5
                # hit the blocker right
                elif ballX <= blockerX + 30 < (ballX - ball_Speed_X) and blockerY - 5 <= ballY <= blockerY + 20 and ball_Speed_X < 0 and blockerX + 30 < 195:
                    #print("right")
                    ball_Speed_X = -ball_Speed_X
                    ballX = blockerX + 30
                # hit the blocker left
                elif ballX + 5 >= blockerX > (ballX - ball_Speed_X) and blockerY - 5 <= ballY <= blockerY + 20 and ball_Speed_X > 0 and blockerX > 5:
                    #print("left")
                    ball_Speed_X = -ball_Speed_X
                    ballX = blockerX - 5



                else:
                    if ballX >= 195:
                        ballX = 195
                        ball_Speed_X = -ball_Speed_X
                    elif ballX <= 0:
                        ballX = 0
                        ball_Speed_X = -ball_Speed_X
                    if ballY <= 80:
                        ballY = 80
                        ball_Speed_Y = -ball_Speed_Y
                    elif ballY >= 415:
                        ballY = 415
                        ball_Speed_Y = -ball_Speed_Y
                    if (ballY >= 415 and self.side == "1P") or (ballY <= 80 and self.side == "2P"):
                        break

            # if self.side == "1P":
            #     print("----")
            if self.side == "1P":
                self.pre_blocker = scene_info["blocker"][0]
                if ballX > plat1X + 21:
                    return "MOVE_RIGHT"
                elif ballX < plat1X + 15:
                    return "MOVE_LEFT"
                else:
                    return "NONE"

            if self.side == "2P": #ballY < 80:
                self.pre_blocker = scene_info["blocker"][0]
                if ballX > plat2X+ 21:
                    return "MOVE_RIGHT"
                elif ballX < plat2X + 15:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            #return "MOVE_LEFT" """
    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
