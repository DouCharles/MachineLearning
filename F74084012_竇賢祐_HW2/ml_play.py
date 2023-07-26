"""
The template of the script for the machine learning process in game pingpong
"""
"""
ml_play 程式只能交一份，且檔名為 ml_play.py
"""
import os
import pickle

import numpy as np

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side


        # load your "1P" and "2P" model here
        # 可以是一個檔案或是兩個檔案，但相對路徑要放好 (路徑請用相對路徑，並放在相同目錄底下)
        
        # sample 1: (如果 "1P", "2P" 是分開 train)
        self.model_1 = "P1.pickle"
        self.model_2 = "P2.pickle"
        if self.side == "1P":
            with open(os.path.join(os.path.dirname(__file__), self.model_1), 'rb') as f:
                self.model = pickle.load(f)
        else:
            with open(os.path.join(os.path.dirname(__file__), self.model_2), 'rb') as f:
                self.model = pickle.load(f)
        
        # sample 2: (如果 "1P", "2P" train 成一個 model)
        # self.model = "1P" and "2P" pickle


    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """

        # 如果是兩個 model 可以在程式中用 side 去判斷要用哪個 model
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
            return command
        else:
        # sample 1: (如果 "1P", "2P" 是分開 train)
            if self.side == "1P":
                # 使用 model 1 預測
                Ball_x = scene_info["ball"][0]
                Ball_y = scene_info["ball"][1]
                Ball_speed_x = scene_info["ball_speed"][0]
                Ball_speed_y = scene_info["ball_speed"][1]
                Platform = scene_info["platform_1P"][0]
                blocker = scene_info["blocker"][0]
                if Ball_speed_x > 0:
                    if Ball_speed_y > 0:
                        Direction = 0
                    else:
                        Direction = 1
                else:
                    if Ball_speed_y > 0:
                        Direction = 2
                    else:
                        Direction = 3
                Direction = Direction * 50
                x = np.array([Ball_x, Ball_y, Platform, blocker,Direction]).reshape((1, -1))  # ,  Ball_speed_x, Ball_speed_y, Direction,
                y = self.model.predict(x)
                # print(y)
                if y == 0:
                    command = "NONE"
                elif y == 1:
                    command = "MOVE_LEFT"
                elif y == 2:
                    command = "MOVE_RIGHT"
                else:
                    command = "NONE"
                return command
            else:

                Ball_x = scene_info["ball"][0]
                Ball_y = scene_info["ball"][1]
                Ball_speed_x = scene_info["ball_speed"][0]
                Ball_speed_y = scene_info["ball_speed"][1]
                Platform = scene_info["platform_2P"][0]
                blocker = scene_info["blocker"][0]
                if Ball_speed_x > 0:
                    if Ball_speed_y > 0:
                        Direction = 0
                    else:
                        Direction = 1
                else:
                    if Ball_speed_y > 0:
                        Direction = 2
                    else:
                        Direction = 3
                Direction = Direction * 50
                x = np.array([Ball_x, Ball_y, Platform, blocker,Direction]).reshape(
                    (1, -1))  # ,  Ball_speed_x, Ball_speed_y, Direction,
                y = self.model.predict(x)
                # print(y)
                if y == 0:
                    command = "NONE"
                elif y == 1:
                    command = "MOVE_LEFT"
                elif y == 2:
                    command = "MOVE_RIGHT"
                else:
                    command = "NONE"
                return command
            # 使用 model 2 預測

        """  
        sample 2: (如果 "1P", "2P" train 成一個 model)
        # 直接使用 model 預測
        """

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
