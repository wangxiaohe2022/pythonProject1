import os # 导入os包用来读写文件
from PyPDF2 import PdfFileMerger # 导入操作pdf相关的软件包

target_path = 'E:/hebing/pdf/yuanwenjian'    #定义pdf文件存放的文件夹路径 注意：这里采用了相对路径
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]   # 获取指定文件夹下所有pdf文件名
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]   # 拼接文件夹路径和文件名，得到pdf文件的全路径

file_merger = PdfFileMerger()   # 创建存放多个pdf文件的对象
for pdf in pdf_lst:
    file_merger.append(pdf)     # 合并pdf文件

file_merger.write("E:/hebing/pdf/daochu/abc.pdf")  # 将合并的pdf文件写入到指定文件内