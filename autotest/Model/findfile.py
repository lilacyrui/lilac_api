#coding = utf-8
import  os
from jbhautotest.UIautotest.Model.path import report_path

def getfile():
    result_dir = report_path()
   # print(result_dir)
    lists = os.listdir(result_dir)
    #print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    #print(('最新的文件为：'+ lists[-1]))
    file = os.path.join(result_dir,lists[-1])
    #print(file)
    return file

if __name__ == '__main__':
    print(getfile())