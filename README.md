# GUI使用说明
基于graphics图形库实现
![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
1. 首先下载graphics图形包：[graphics.py](http://mcsp.wartburg.edu/zelle/python/graphics.py)   
  
2. 将下载好的py文件放入python的第三方库文件夹中:       **\Programs\Python\Python36-32\Lib\site-packages
  
3. 在你的AI.py中import这个库的Windows类
    >import numpy as np  
    >import random  
    >import time  
    > **from GUI import Window**

4. 在go()函数中初始化window：
    >**self.window = Window(self.chessboard_size)**  
    >**self.window.initiate(self.chessboard)**#会直接显示self.chessboard棋盘  


* 要显示接下来的每一步（显示博弈树展开的具体过程）或者显示每个位置的打分：
    * 在minmax函数中（假设你使用了博弈树搜索方法）：
        * 在展开下一层搜索前，在“模拟下子”的地方调用add（）函数：
            ```
            minmax(self,who,,depth,alpha,beta)
                for next_step in possible_Moves:
                    self.black_List.append(next_step)
                    self.chessboard[next_step[0]][next_step[1]]=self.ori_color
                    
                    # 绘制该棋子
            >>>>>>  self.window.add(self.color,next_step,self._max_depth-depth+1)

                    # 角色变换
                    self.color = -self.color

                    # 展开下一层搜索
                    score = self.minimaxWithDepth(-who,depth-1,alpha,beta)
                    
                    # 该子节点搜索完后,移除该棋子
            >>>>>>  self.window.remove(next_step)
            ```
    * 在对某一个点打分的地方, 调用  
        ```
        def getPossibleMoves(self):
            possible = []

            # 初始化一个临时窗口
        >>  temp_win = Window(self.chessboard_size)
        >>  temp_win.initiate(self.chessboard)

            # 对棋盘中的每个空位
            for item in self.blank_list:

                # 判断该位置周围两个内是否有子(这只是我的写法而已)
                if self.is_neighbour(item):

                    # 打分
                    score = self.getScore(item)
                    possible.append((item,int(score)))

                    # 在临时窗口中显示这个数字
        >>          temp_win.display_number(item,score)
        
            # (可关可不关,关掉的话就必须调试在这打断点才能看到窗口)关闭这个临时窗口
        >>  temp_win.close()
        ```
