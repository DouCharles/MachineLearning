import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import  classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit

#試取資料
file = open("..\log\success (1).pickle", "rb")
data = pickle.load(file)
file.close()

print(data)

game_info = data['ml_1P']['scene_info']
game_command = data['ml_1P']['command']
game_info = []
game_command = []
print(game_info)
print(game_command)



import os
dir_path = "..\log"
for file_path in os.listdir(dir_path):
    #print(file_path)
    with open('..\\log\\' + file_path , 'rb') as f:
        data = pickle.load(f)
        #print(data)
        #print("-------------------")
    game_info = game_info + data['ml_1P']['scene_info']
    game_command = game_command + data['ml_2P']['command']
    #game_2P_command = game_2P_command + data['ml_2P']['command']
    #file.close()
# for i in range(2, 4):
#     path = "../log/n3 (" + str(i) + ").pickle"
#     file = open(path, "rb")
#     data = pickle.load(file)
#     game_info = game_info + data['scene_info']
#     game_command = game_command + data['command']
#     file.close()

print('game0 ')
print(game_info[0])
print(len(game_command))
print(len(game_info))


g = game_info[1]
speed_x = game_info[1]['ball_speed'][0]#game_info[2]['ball'][0] - game_info[1]['ball'][0]
speed_y = game_info[1]['ball_speed'][1]#game_info[1]['ball'][1] - game_info[2]['ball'][1]+
blocker = game_info[1]["blocker"][0]
#bricks = len(game_info[1]['bricks'])
if speed_x > 0:
    if speed_y > 0:
        Direction = 0
    else:
        Direction = 1
else:
    if speed_y > 0:
        Direction = 2
    else:
        Direction = 3
Direction = Direction * 50
feature = np.array([g['ball'][0], g['ball'][1], g['platform_2P'][0],blocker,Direction])#,speed_x,speed_y],bricks)
print(feature)

print(game_command[1])
game_command[1] = 0



for i in range(2, len(game_info) - 1):##從這開始改
    print(i)
    g = game_info[i]
    speed_x = game_info[i]['ball_speed'][0]
    speed_y = game_info[i]['ball_speed'][1]
    if speed_x > 0:
        if speed_y > 0:
            Direction = 0
        else:
            Direction = 1
    else:
        if speed_y > 0:
            Direction = 2
        else:
            Direction = 3
    Direction = Direction * 50
    blocker = game_info[i]['blocker'][0]
    feature = np.vstack((feature, [g['ball'][0], g['ball'][1], g['platform_2P'][0],blocker,Direction]))#,speed_x,speed_y])),bricks
    if game_command[i] == "NONE": game_command[i] = 0
    elif game_command[i] == "MOVE_LEFT": game_command[i] = 1
    else: game_command[i] = 2

answer = np.array(game_command[1:-1])

print(feature)
print(feature.shape)
print(answer)
print(answer.shape)




#資料劃分
x_train, x_test, y_train, y_test = train_test_split(feature, answer, test_size=0.3, random_state=1)
#參數區間
param_grid = {'n_neighbors':[1, 2, 3]}
#交叉驗證
cv = StratifiedShuffleSplit(n_splits=2, test_size=0.3, random_state=12)
grid = GridSearchCV(KNeighborsClassifier(n_neighbors = 5),param_grid, cv=cv, verbose=10, n_jobs=-1) #n_jobs為平行運算的數量
grid.fit(x_train, y_train)
grid_predictions = grid.predict(x_test)

#儲存
file = open('P2.pickle', 'wb')
pickle.dump(grid, file)
file.close()


#最佳參數
print(grid.best_params_)
#預測結果
#print(grid_predictions)
#混淆矩陣
print(confusion_matrix(y_test, grid_predictions))
#分類結果
print(classification_report(y_test, grid_predictions))