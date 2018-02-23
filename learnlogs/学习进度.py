import os
lines_sum = 0
file_num = 0
def search_file(start_dir):
    global lines_sum,file_num
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[-1]
        if ext == '.py':
            lines = stat_code(each_file)
            lines_sum += lines
            file_num += 1
        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)

def stat_code(file_name):
    lines = 0
    with open (file_name,'rb') as f:
        for each_line in f:
            lines += 1
    return lines


search_file(os.curdir)
print('学习进度：\n今天共编写%d个文件，%d行代码'\
          % (file_num,lines_sum))
