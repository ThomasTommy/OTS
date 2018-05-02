# 2018.05.01
# By ThomasTommy.
# Omiga_Unit_Para_1.0.py

# 实现从OnigaLand导出的设备文件中获得指定的设备参数.
# 下一步,自动将每一个设备写成一个类.
# 通过ProcessName.UnitName.Parameter.Value的形式调用.

# Load Package.
import re
import numpy as np

# 要读取的Unit文件,从OmigaLand导出.
# 此处的Test_DB.txt为例子.
File = 'Test_DB.txt'


# 打开文件.
with open(File) as f:
    # Line_Num: 记录所在行.
    Line_Num = 0

    # 生成类的新文件New_File
    with open(New_File,'w') as New_f:

    # 逐行读取.
    for s in f:
        line_num += 1
        # 每个Unit都有ID编号,格式为 0-9999,
        # re_s = \s\d{1,4},找出Unit的编号.
        pattern = re.compile(r'\s\d{1,4}')
        result = pattern.findall(s,0,5)

        # 如果result非空,则为Unit首行,
        # 以空格为分隔符,分8次,
        # 分别得到:
        # ID: s[4], Unit编号.
        # Name: s[5], UnitName.
        # Model: s[7], Model Liborary.
        # Notes: s[8], Unit Notes.
        if len(result):
            s_list = s.split(' ',8)
            ID = s_list[4]
            Name = s_list[5]
            Model = s_list[7]
            Notes = s_list[8]

            New_s = 'class Block_' + Name + ':\n\t'
            New_f.write(New_s)

        # 如果result为空,则为Unit参数行.
        # 根据参数行前面不同的符号,分为三种情况.
        else:
            # 1.General Parameters:
            #   Unit创建时所设置的参数,
            #   导出文件中,这些参数名字前面都有*与其他参数区分,
            #   re_s = ^\s{7}\*.*,即起始7个空格1个*的行,就是General Parameters.
            #   该行非空,则提取数据,
            #   分别得到:
            #   Genepara_Name
            #   Genepara_Value
            #   Genepara_Notes
            pattern = re.compile(r'^\s{7}(\*.*)')
            Genepara = pattern.findall(s)
            if len(Genepara):
                Genepara_list = Genepara[0].split()
                Genepara_Name = Genepara_list[0]
                Genepara_Value = Genepara_list[1]
                Genepara_Notes = ' '.join(Genepara_list[2:])

            # 2.Pripara Parameters:
            #   Unit的主要参数,值均为单值,
            #   re_s = ^\t[^\s].*,即起始1个\t后面不能是符号的行,就是Primary Parameters.
            #   该行非空,则提取数据,
            #   分别得到:
            #   Pripara_Name
            #   Pripara_Value
            #   Pripara_Notes
            pattern = re.compile(r'^\t([^\s].*)')
            Pripara = pattern.findall(s)
            if len(Pripara):
                Pripara_list = Pripara[0].split()
                Pripara_Name = Pripara_list[0]
                Pripara_Value = Pripara_list[1]
                Pripara_Notes = ' '.join(Pripara_list[2:])

            # 3.Pripara Parameters List:
            #   Unit的主要参数中的多值参数,例如组分,系数,值均为列表,
            #   先要提取出列表的参数名字,数值元组和注释,
            #   这一行的主要特征是数值元组在括号内,
            #   re_s = \(\d+|\d+\,\d+\),数值元组可以是一维元组,也可以是1*2的元组(*,*).
            pattern = re.compile(r'^\t(\w+)\s+\((\d+|\d+\,\d+)\)\s+(.*)')
            Priparalist = pattern.findall(s)

            #   如果该行非空,则提取数据,
            #   分别得到:
            #   Priparalist_Name
            #   Priparalist_Tuple
            #   Priparalist_Notes
            if len(Priparalist):
                Priparalist_Name = Priparalist[0][0]
                Priparalist_Tuple = Priparalist[0][1]
                Priparalist_Notes = Priparalist[0][2]

                #   并新建变量Priparalist_Value = [],
                #   准备读取数据列表中的数据到Priparalist_Value.
                Priparalist_Value = []
                
                #   数据列表中的数据又分为三种情况:
                #   1) 如果Priparalist_Name == 'EQN',
                #      证明该多值参数为CalCu模块中的程序,
                #      所对应的Tuple为程序行数,
                #      所对应的Value为程序内容,
                #      并规定此种情况为k=1.
                if Priparalist_Name == 'EQN':
                    Priparalist_Lines = int(Priparalist_Tuple)
                    Priparalist_Value_Start = Line_Num
                    Priparalist_Value_End = Line_Num + Priparalist_Lines
                    k = 1

                #   2) 如果Priparalist_Tuple中出现',',
                #      证明该多值参数的Value为n维矩阵,
                #      所对应的Tuple为矩阵的(*,*),
                #      所对应的Value一般是精馏塔的塔板组成,
                #      并规定此种情况为k=2.
                elif ',' in Priparalist_Tuple:
                    Priparalist_Value_Lines = int(Priparalist_Tuple.split(',')[0])
                    Priparalist_Value_Columns = int(Priparalist[0][1].split(',')[1])
                    Priparalist_Lines = Priparalist_Value_Lines * (Priparalist_Value_Columns // 10 + Priparalist_Value_Columns % 10)
                    Priparalist_Value_Start = Line_Num
                    Priparalist_Value_End = Line_Num + Priparalist_Lines
                    k = 2

                #   3) 最后一种情况是Tuple是一维元组,
                #      证明该多值参数的Value为一维矩阵,
                #      所对应的Tuple为矩阵的列,
                #      所对应的Value为矩阵的值,
                #      并规定此种情况为k=3.
                else:
                    Priparalist_Value_Columns = int(Priparalist_Tuple)
                    Priparalist_Lines = Priparalist_Value_Columns // 10 + Priparalist_Value_Columns % 10
                    Priparalist_Value_Start = Line_Num
                    Priparalist_Value_End = Line_Num + Priparalist_Lines
                    k = 3

                #   至此,获得三种情况的Priparalist_Lines,即Value所对应的Line_Num,
                #   目的是获得更好得获得对应的Value.
                #   开始尝试在对应的Line_Num内寻找对应的Value.
                try:
                    #   如果进行到Value所对应的Priparalist_Lines,则读取数据,
                    #   re_s = '^\t\s{9}(.*)',即起始1个\t,9个\s的行就是Priparalist_Value所在的行.
                    if Line_Num > Priparalist_Value_Start & Line_Num < Priparalist_Value_End + 1:
                        pattern = re.compile(r'^\t\s{9}(.*)')
                        _Priparalist_Value = pattern.findall(s)

                        #   由于数据列表中的数据分为三种情况,
                        #   则读取数据也要分三种情况分别读取,
                        #   前面所标记的k值就是分别对应三种不同的情况.

                        #   1) k=1时,
                        #      所对应的Value为程序内容,
                        if k == 1:
                            Priparalist_Value.append(Pripara_x_value[0])

                            #   如果此时所在行已经到Priparalist_Value的最后一行,
                            #   则整理获得最终的Priparalist_Value.
                            if Line_Num == Priparalist_Value_End:
                                Priparalist_Value = '\n'.join(Priparalist_Value)

                        #   1) k=2时,
                        #      所对应的Value为n维矩阵,
                        if k == 2:
                            for v in _Priparalist_Value[0].split():
                                Priparalist_Value.append(float(v))

                            #   如果此时Priparalist_Value已经读完了矩阵中所有的数,即Len = Lines * Columns,
                            #   则需要把Priparalist_Value从1维矩阵转化为Lines * Columns矩阵.
                            #   此时获得最终的Pripara_Value
                                if len(Priparalist_Value) == Priparalist_Value_Lines * Priparalist_Value_Columns:
                                    Priparalist_Value = np.array(Priparalist_Value)
                                    Priparalist_Value = Priparalist_Value.reshape(Priparalist_Value_Lines,Priparalist_Value_Columns)

                        #   1) k=3时,
                        #      所对应的Value为一维矩阵,
                        if k == 3:
                            for v in _Priparalist_Value[0].split():
                                Priparalist_Value.append(float(v))

                                #   如果此时Pripara_Value已经读完了矩阵中的所有的数，即Len = Columns,
                                #   此时获得最终的Pripara_Value.
                                if len(Priparalist_Value) == Priparalist_Value_Columns:
                                    print(Priparalist_Value)
                # 如果不在Pripara_Value所对应的行,
                # 则继续循环. 
                except:
                    continue

    # 读完关闭文件夹.
    f.close()