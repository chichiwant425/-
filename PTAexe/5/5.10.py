class Circle:
    def SetCenter(self,x,y):  #设置圆心坐标方法
        self.x=x
        self.y=y
    def SetRadius(self,r):  #设置半径方法
        self.r = r
    def PrintInfo(self):#输入 圆的相关信息
        print('x={:.2f},y={:.2f},r={:.2f}'.format(self.x,self.y,self.r))
    def GetArea(self): # 计算圆面积
        return self.r**2*3.14

if __name__=='__main__':
    c=Circle() #创建Circle类对象c
    x=eval(input()) #输入圆心的x坐标
    y=eval(input()) #输入圆心的y坐标
    r=eval(input()) #输入半径
    c.SetCenter(x,y) #设置圆心
    c.SetRadius(r) #设置半径
    c.PrintInfo() #输出圆的圆心和半径信息（均保留2位小数）
    print('%.2f'%c.GetArea()) #输出圆的面积（保留2位小数）