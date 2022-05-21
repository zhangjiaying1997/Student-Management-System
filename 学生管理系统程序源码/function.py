import os
filename='Student.txt'
flags = False


def menum():
    print(30 * '=' + '学生信息管理系统' + 30 * '=')
    print(33 * '-' + '功能菜单' + 33 * '-')
    print(3 * '\t' + '0.退出系统' + 7 * '\t' + '1.录入学生信息')
    print(3 * '\t' + '2.查找学生信息' + 6 * '\t' + '3.删除学生信息')
    print(3 * '\t' + '4.修改学生信息' + 6 * '\t' + '5.对学生成绩排序')
    print(3 * '\t' + '6.统计学生总人数' + 6 * '\t' + '7.显示所有学生信息')
    print(32*'-'+32*'-')
    print(72*'-')

def insert():
    Student_list=[]
    while True:
        St_name=input('请输入学生的姓名:')

        try:
            St_ID=int(input('请输入学生的ID:'))
        except:
            print('输出的ID不是编号，请重写输入!')
            continue

        if not St_name or  not St_ID:
            break

        try:
            english=float(input('请输入英语成绩:'))
            python=float(input('请输入python成绩:'))
            java=float(input('请输入java成绩:'))
        except:
            print('输入无效，输入的不是数字类型，请重新输入!')
            continue
        student={'St_ID':St_ID,'St_name':St_name,'english':english,'python':python,'java':java}
        Student_list.append(student)
        answer=input('是否继续添加?y/n\n')
        if answer=='Y' or answer=='y':
            continue
        else:
            break
    save(Student_list)
    show()
    print('学生信息录入完毕!')

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2:')
            if mode=='1':
                id=input('请输入要查找学生ID:')
            elif mode=='2':
                name=input('请输入要查找学生姓名:')
            else:
                print('输入出错，请重写输入!')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                str=rfile.readlines()
                for item in str:
                    d=dict(eval(item))
                    if id!='':
                        if d['St_ID']==int(id):
                            student_query.append(d)
                    elif name!='':
                        if d['St_name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input('是否要继续查询?Y/N\n')
            if answer=='Y' or answer=='y':
                continue
            else:
                break
        else:
            print('尚未保存学生信息!')
            return





def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示!')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','java成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    for item in lst:
        #print(int(item.get('english')),type(int(item.get('english'))))
        print(format_data.format(item.get('St_ID'),
                                 item.get('St_name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))




def delete():
    show()
    while True:
        try:
            st_id=int(input('请输入删除学生ID'))
        except:
            print('输入错误，请重写输入ID!')
            continue
        if  st_id:
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    st_old=file.readlines()
            else:
                st_old=[]
            flags=False
            if st_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in st_old:
                        d=eval(item)
                        if d['St_ID']!=st_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flags=True
                    if flags==True:
                        print(f'id为{st_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到{st_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续删除?Y/N')
            if answer=='Y' or answer=='y':
                continue
            else:
                break



def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            st_old=rfile.readlines()
    else:
        return
    if not st_old:
        print('没有录入学生信息，请返回录入学生信息!')
    else:
        try:
            st_id=int(input('请输入要修改学生的id:'))
        except:
            print('输入非法，请重写输入id!')
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in st_old:
                d=dict(eval(item))
                if d['St_ID']==st_id:
                    print('找到学生信息，可以修改他的相关信息了!')
                    while True:
                        try:
                            d['St_name']=input('请输入姓名:')
                            d['english']=input('请输入英语成绩:')
                            d['python']=input('请输入python成绩:')
                            d['java']=input('请输入java成绩:')
                        except:
                            print('输入有误，请重写输入!')
                        else:
                            break
                    wfile.write(str(d)+'\n')
                    print('修改成功!')
                else:
                    wfile.write(str(d)+'\n')
                    print('找不到学生信息或者输入有误!')
            answer=input('是否继续修改其他学生信息?Y/N\n')
            if answer=='y' or answer=='Y':
                modify()







def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            st_lst=rfile.readlines()
        stu_new=[]
        for item in st_lst:
            d=dict(eval(item))
            stu_new.append(d)
    else:
        return
    asc_or_desc=input('请选择(0.升序 1.降序):')
    if asc_or_desc=='0':
        asc_or_desc=False
    elif asc_or_desc=='1':
        asc_or_desc=True
    else:
        print('您的输入有误!请重新输入!')
        sort()
    mode=input('请选择排序方式(1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序 4.按总成绩排序):')
    if mode=='1':
        stu_new.sort(key=lambda x :int(x['english']),reverse=asc_or_desc)
    elif mode=='2':
        stu_new.sort(key=lambda x :int(x['python']),reverse=asc_or_desc)
    elif mode=='3':
        stu_new.sort(key=lambda x: x['java'], reverse=asc_or_desc)
    elif mode=='4':
        stu_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_desc)
    else:
        print('您的输入有误，请重新输入!')
        sort()
    show_student(stu_new)



def total():
    i=0
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            str=rfile.readlines()
            for item in str:
                i+=1
            if i:
                print('一共有%d名学生' % i)
                i=0
            else:
                print('还没有录入任何学生信息')
def show():
    st_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            str=rfile.readlines()
            for item in str:
                st_lst.append(eval(item))
            if st_lst:
                show_student(st_lst)



def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')




