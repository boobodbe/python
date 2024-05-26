'''
学生信息管理系统7大模块
    录入学生信息模块
    查找学生信息模块
    删除学生信息模块
    修改学生信息模块
    学生成绩排名模块
    统计学生总人数模块
    显示全部学生信息模块
'''
import os.path

filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('请输入菜单序号：\t'))
        if choice in [1,2,3,4,5,6,7,0]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n\t')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息

def menu():
    print('=========================学生信息管理系统================================')
    print('-----------------------------功能菜单-----------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('----------------------------------------------------------------------')

def insert():
    student_list = []
    while True:
        id = input('请输入学生ID(如1000)：\t')
        if not id:
            break
        name = input('请输入学生姓名：\t')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：\t'))
            python = int(input('请输入python成绩：\t'))
            java = int(input('请输入Java成绩：\t'))
        except:
            print('输入无效，请重新输入！')
            continue
        student = {'id':id, 'name':name, 'english':english, 'python':python, 'java':java}
        student_list.append(student)
        answer = input('您还要继续添加学生信息吗？y/n\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完成！！！')

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    while True:
        show()
        choice = input('请输入学生姓名或id：\t')
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as rf:
                student_old = rf.readlines()
        else:
            return '没有找到学生信息文件'
        flag = False
        if student_old:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == choice or d['name'] == choice:
                    print('找到相关学生信息了。')
                    flag = True
                    show_list(d)
                    print('-'*50)
                    break
            if flag == False:
                print('没有找到学生信息。')
        else:
            print('文件列表为空。')
        answer = input('您还要继续查询吗？y/n\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

def show_list(lst):
    if len(lst) == 0:
        print('没有学生信息，无数据显示。')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('id','姓名','英语成绩','python成绩','Java成绩','总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_data.format(lst.get('id'),
                             lst.get('name'),
                             lst.get('english'),
                             lst.get('python'),
                             lst.get('java'),
                             int(lst.get('english'))+int(lst.get('python'))+int(lst.get('java'))))

def delete():
    while True:
        show()
        student_id = input('请输入要删除的学生ID：\t')
        if student_id:
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False # 标记学生信息是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wf:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wf.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print('id为{0}的学生信息已被删除。'.format(student_id))
                    else:
                        print('没有找到id为{0}的学生信息。'.format(student_id))
            else:
                print('没有找到相关学生信息。')
                break
            show()
            answer = input('是否继续删除？y/n\t')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rf:
            student_old = rf.readlines()
    else:
        return '没有找到学生信息文件'
    student_id = input('请输入要修改的学生的id：\t')
    if student_id:
        with open(filename,'w',encoding='utf-8') as wf:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print('找到相关学生信息了，可以进行修改。')
                    while True:
                        try:
                            d['name'] = input('请输入姓名：\t')
                            d['english'] = input('请输入英语成绩：\t')
                            d['python'] = input('请输入python成绩：\t')
                            d['java'] = input('请输入java成绩：\t')
                        except:
                            print('您的输入有误，请重新输入。')
                        wf.write(str(d)+'\n')
                        print('学生信息修改成功。')
                        break
                else:
                    wf.write(str(d)+'\n')
            answer = input('是否要继续修改其他信息：y/n\t')
            if answer == 'y' or answer == 'Y':
                modify()

def sort():
    show()
    student_new = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rf:
            student_list = rf.readlines()
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return '不存在相关文件。'
    choice = input('升序请输入0，降序请输入1：\t')
    if choice == '0':
        flag = False
    elif choice == '1':
        flag = True
    else:
        print('您的是输入有误，请重新输入。')
        return
    mode =  input('请输入排序方式：（1.按英语成绩）（2.按python成绩）（3.按Java成绩）（4.按总成绩）')
    if mode == '1':
        student_new.sort(key=lambda x : int(x['english']),reverse=flag)
    elif mode == '2':
        student_new.sort(key=lambda x : int(x['python']),reverse=flag)
    elif mode == '3':
        student_new.sort(key=lambda x : int(x['java']),reverse=flag)
    elif mode == '4':
        student_new.sort(key=lambda x : int(x['english'])+int(x['python'])+int(x['java']),reverse=flag)
    else:
        print('您的输入有误，请重新输入。')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩'))
    for lst in student_new:
        lst = dict(eval(str(lst)))
        print(format_data.format(lst.get('id'),
                                 lst.get('name'),
                                 lst.get('english'),
                                 lst.get('python'),
                                 lst.get('java'),
                                 int(lst.get('english')) + int(lst.get('python')) + int(lst.get('java'))))

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rf:
            students = rf.readlines()
            if students:
                print('一共有{}名学生。'.format(len(students)))
            else:
                print('还没有录入学生信息。')
    else:
        print('没有学生信息。')

def show():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rf:
            students = rf.readlines()
            if students:
                format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
                format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
                print(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩'))
                for lst in students:
                    lst = dict(eval(lst))
                    print(format_data.format(lst.get('id'),
                                             lst.get('name'),
                                             lst.get('english'),
                                             lst.get('python'),
                                             lst.get('java'),
                                             int(lst.get('english')) + int(lst.get('python')) + int(lst.get('java'))))
            else:
                print('学生信息为空。')
    else:
        print('没有学生信息文件。')


if __name__ == '__main__':
    main()
