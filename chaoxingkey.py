# 适用于超星学习通新版考试完成页面提取问题和答案保存为txt
# 记得修改主函数path路径，存放html文件
from bs4 import BeautifulSoup

# 分析单个页面，提取题目和问题
# 返回（题目数量，题目标题于列表title，题目选项于列表choice，答案于列表key）且一一对应
def getData (html):
    #分析页面
    soup = BeautifulSoup (html, "html.parser")

    # 获取标题，存于列表title
    title_raw = soup.find_all ("h3", class_="mark_name colorDeep")       #查找标签h3和指定class类
    title = []
    for i in title_raw:
        title.append(i.get_text().strip())      #标题添加到title列表中
    for i in range(len(title)):         #去除标题前的题号，防止在字典中无法匹配的问题
        flag = title[i].index('.')
        title[i] = title[i][flag+2:]

    # 获取选项，存于列表choice
    choice_raw = soup.find_all (class_="mark_letter colorDeep")
    choice = []
    for i in choice_raw:
        i = i.get_text()
        choice.append(i.strip('\n'))        # 把每题选项放入choice列表中，去除前后\n

    for i in range(len(choice)):        # choice列表每项元素按照ABCD选项划分
        choice[i] = choice[i].split('\n')   #choice为二维列表


    # 获取答案，存于列表key
    key_raw = soup.find_all(class_="colorGreen marginRight40 fl")
    key = []
    for i in key_raw:
        t = i.get_text()
        # t = t[6:]          # 去除“正确答案: ”字样， 仅保留ABCD
        key.append(t)

    return (len(title), title, choice, key)



# 区分单选题和多选题
# 单选题放于title_single, choice_single, key_single
# 多选题放于title_multiple, choice_multiple, key_multiple
def devideQuesion (title_len, title, choice, key):
    title_single = []
    choice_single = []
    key_single = []
    title_multiple = []
    choice_multiple = []
    key_multiple = []

    # 遍历题目
    for i in range(title_len):
        # 判断为单选题
        if "单选题" in title[i]:
            title_single.append(title[i])
            choice_single.append(choice[i])
            key_single.append(key[i])
            continue

        # 判断为多选题
        if "多选题" in title[i]:
            title_multiple.append(title[i])
            choice_multiple.append(choice[i])
            key_multiple.append(key[i])
            continue

    return (title_single, choice_single, key_single, title_multiple, choice_multiple, key_multiple)



# 讲题目插入字典question
def addDic (question, title_len, title, choice, key):
    for i in range(title_len):
        # 题目去重，防止再次添加至字典中
        # 如果存在则跳过
        if title[i] in question:
            continue
        else:
            # 否则插入字典
            t = []
            t.append(key[i])            # 添加临时列表，使答案ABCD为一个整体元素
            question[title[i]] = tuple(choice[i]) + tuple(t)    # 添加答案到元组最后一个元素

    return question



# 将题目输出至文本文档（字典，文件标识符）
def outPut (question_dic, f):
    for q in question_dic.items():          # 遍历题
        f.writelines(q[0])                  # 将标题输出
        f.writelines("\n")                  # 输出换行
        for i in q[1]:                      # 遍历字典的值
            f.writelines(i)                 # 输出值，答案在最后一行
            f.writelines("\n")              # 换行
        f.writelines("\n\n")                # 每题后加两行空行





if __name__ == '__main__':

    # 请输入html存放路径
    path = ["key/1/key.html","key/2/key2.html"]
    question_single = {}  # 单选题目总字典
    question_multiple = {}  # 多选题目总字典

    # 遍历提取path中的html存于question字典
    for i in range(len(path)):
        title_len = 0       # 页面标题数目
        with open(path[i], 'r', encoding='utf-8') as html:
            title_len, title, choice, key = getData(html)               # 获取题目选项答案总数据
        title_single, choice_single, key_single, title_multiple, choice_multiple, key_multiple = devideQuesion(title_len, title, choice, key)      # 划分单选多选
        print("文件{}题目总数：{}".format(path[i],title_len))
        print("单选题数量：{}".format(len(title_single)),end='\t')
        print("多选题数量：{}".format(len(title_multiple)))

        question_single = addDic(question_single, len(title_single), title_single, choice_single, key_single)                   # 单选添加到字典中
        question_multiple = addDic(question_multiple, len(title_multiple), title_multiple, choice_multiple, key_multiple)       # 单选添加到字典中
        print("累计题目数量：{}".format(len(question_single)+len(question_multiple)))

    print("\n累计题目数量：")
    print("单选:{}".format(len(question_single)),end='\t')
    print("多选:{}".format(len(question_multiple)))
    print("正在输出至文件txt...")
    f_single = open("question_single.txt", 'w+', encoding='utf-8')          # 创建单选文件
    outPut(question_single,f_single)                                        # 输出至txt

    f_multiple = open("question_multiple.txt", 'w+', encoding='utf-8')      #创建多选文件
    outPut(question_multiple, f_multiple)
    print("输出完成，程序退出。")
    f_single.close()
    f_multiple.close()
