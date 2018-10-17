from graphics import *
from math import *
import numpy as np
COLOR_BLACK=-1 
COLOR_WHITE=1 
COLOR_NONE=0
GRID_WIDTH=40

class Window():
    def __init__ (self,chessboard_size):
        self.pieces = []
        self.chessboard_size = chessboard_size
        self.GRAPH_WIDTH = GRID_WIDTH * (chessboard_size + 1)
        self.GRAPH_HEIGHT = GRID_WIDTH * (chessboard_size + 1)
        self.window = self.draw_window()
        self.number = 0


    def draw_window(self):
        """
        绘制棋盘
        """
        ROW = COLUMN = self.chessboard_size
        GRAPH_WIDTH = GRID_WIDTH * (self.chessboard_size + 1)
        GRAPH_HEIGHT = GRID_WIDTH * (self.chessboard_size + 1)
        # 绘制画板
        win = GraphWin("Go Bang", GRAPH_HEIGHT, GRAPH_WIDTH)
        win.setBackground("sandybrown")
        # 绘制列
        i1 = 0
        i = 0
        while i1 <= GRID_WIDTH * COLUMN:
            i1 = i1 + GRID_WIDTH
            l = Line(Point(i1, GRID_WIDTH), Point(i1, GRID_WIDTH * COLUMN))
            num = Text(Point(i1,GRID_WIDTH-20),i)
            i += 1
            if i<16:
                num.draw(win)
            l.draw(win)
        # 绘制行
        i2 = 0
        i = 0
        while i2 <= GRID_WIDTH * ROW:
            i2 = i2 + GRID_WIDTH
            l = Line(Point(GRID_WIDTH, i2), Point(GRID_WIDTH * ROW, i2))
            num = Text(Point(GRID_WIDTH-20,i2),i)
            if i<15:
                num.draw(win)
            i +=1
            l.draw(win)
        return win
    

    def refresh(self):
        self.window.flush()

    # 删除指定位置的子和子的序号
    def remove(self,pos):
        '''位置为一个(x,y)元组'''
        m = GRID_WIDTH * (pos[0]+1) *1.0
        n = GRID_WIDTH * (pos[1]+1) *1.0
        items_to_delete = []
        for item in self.window.items:
            if(type(item) is Text):
                x = item.getAnchor().getX() 
                y = item.getAnchor().getY()
                if m==x and n==y:
                    self.number -=1
                    items_to_delete.append(item)
                
            elif(type(item) is Circle):
                x = item.getCenter().getX() 
                y = item.getCenter().getY()
                if m==x and n==y:
                    if item.getRadius() == 12:
                        items_to_delete.append(item)
                    
        for item in items_to_delete:
            item.undraw()
        
        
    # 在指定位置画一个小红点
    def target(self,pos):
        '''位置为一个(x,y)元组,可以用来表示搜索后的最优点'''
        (self.red_point(pos)).draw(self.window)

    # 在指定位置显示一个小小的数字（打分专用）    
    def display_number(self,pos,num):
        '''位置为一个(x,y)元组，数字可以是对该位置的打分'''
        piece = Text(Point(GRID_WIDTH * (pos[0]+1) ,GRID_WIDTH * (pos[1]+1)), int(num))
        piece.setSize(9)
        piece.setTextColor('black')
        piece.setStyle('bold')
        piece.draw(self.window)

    # 关闭窗口    
    def close(self):
        self.window.close()

    # 在指定位置显示一个一个棋子和数字（表示下子的顺序）
    def add(self, color,pos,num=' '):
        ''' 颜色和模板中的定义一样，位置为一个(x,y)元组，数字可以是（最大搜索深度-当前深度）'''
        self.number+=1
        (self.a_piece(color,pos)).draw(self.window)
        (self.order(pos,num)).draw(self.window)

    # 初始化棋盘    
    def initiate(self, chessboard):
        '''初始化棋盘,直接传入numpy的棋盘（格式和self.chessboard一样） '''
        black_list = np.where(chessboard == COLOR_BLACK)
        white_list = np.where(chessboard == COLOR_WHITE)
        black_list = list(zip(black_list[0], black_list[1]))
        white_list = list(zip(white_list[0], white_list[1]))
        for black_pos in black_list:
            self.a_piece(COLOR_BLACK,black_pos).draw(self.window)
        for white_pos in white_list:
            (self.a_piece(COLOR_WHITE,white_pos)).draw(self.window)
        self.window.flush()


    
    def a_piece(self,color,pos):
            piece = Circle(Point(GRID_WIDTH * (pos[0]+1) ,GRID_WIDTH * (pos[1]+1)), 12)
            if color is COLOR_BLACK:
                piece.setFill('black')
            elif color is COLOR_WHITE:
                piece.setFill('white')
            return piece

    def red_point(self,pos):
            piece1 = Circle(Point(GRID_WIDTH * (pos[0]+1) ,GRID_WIDTH * (pos[1]+1)), 6)
            piece1.setFill('red')
            return piece1
    
    # 生成一个数字
    def order(self,pos,num):
        piece = Text(Point(GRID_WIDTH * (pos[0]+1) ,GRID_WIDTH * (pos[1]+1)), num)
        piece.setTextColor('red')
        return piece
        



 

