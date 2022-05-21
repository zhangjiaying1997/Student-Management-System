import function
def main():
    while True:
        function.menum()
        choice=int(input('请输入要选择的功能(0-7):'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用!!!')
                    break   #退出登陆
                else:
                    continue
            elif choice==1:
                function.insert()
            elif choice==2:
                function.search()
            elif choice==3:
                function.delete()
            elif choice==4:
                function.modify()
            elif choice==5:
                function.sort()
            elif choice==6:
                function.total()
            elif choice==7:
                function.show()

main()
