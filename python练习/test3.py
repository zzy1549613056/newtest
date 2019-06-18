#!/usr/local/bin/python3
import os
def printPath(path,st):
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path,x)) and ('Pictures' not in x):
            new_path = os.path.join(path,x)
            printPath(new_path,st)
        else:
            if st in x:
                p_path = os.path.join(path,x)
                print(p_path)

if __name__ == '__main__':
    path = os.path.abspath('.')
    path = os.path.dirname(path)
    # print(path)
    printPath(path,'zzy') 
      
#  TIPS:
# 在判断isdir()/isfile()的时候，既可以传绝对路径，又可以传相对路径

# 如果传相对路径，需要根据当前目录判断，即当前目录+相对路径是否存在

# 默认情况下，当前目录是命令行启动的目录，在程序中也可以用chdir()切换当前目录           




