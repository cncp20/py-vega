from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "===============")
    print(Fore.LIGHTBLUE_EX, "欢迎使用")
    print(Fore.LIGHTBLUE_EX, "===============")
    print(Fore.LIGHTGREEN_EX, "1.登录系统")
    print(Fore.LIGHTGREEN_EX, "2.退出系统")
    print(Style.RESET_ALL)
    opt = input("请输入编号")
    if opt == "1":
        username = input("请输入用户名")
        password = input("请输入密码")
        result = __user_service.login(username, password)
        print(result)
        if result:
            role = __user_service.get_user_role(username)
            os.system("clear")
            while True:
                if role == "新闻编辑":
                    print("test")
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "2.用户管理")
                    print(Fore.LIGHTRED_EX, "back.退出登录")
                    print(Fore.LIGHTRED_EX, "exit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("请输入编号")
                    if opt == "1":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "2.删除新闻")
                            print(Fore.LIGHTRED_EX, "back.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("请输入编号")
                            if opt == "1":
                                page = 1
                                while True:
                                    os.system("clear")
                                    page_count = __news_service.get_unreview_count()
                                    result = __news_service.get_unreview_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX, "%d.%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "%d/%d" % (page, page_count))
                                    print(Fore.LIGHTRED_EX, "pre.上一页")
                                    print(Fore.LIGHTRED_EX, "next.下一页")
                                    print(Fore.LIGHTRED_EX, "back.返回上一层")
                                    print(Style.RESET_ALL)
                                    opt = input("请输入编号")
                                    if opt == "back":
                                        break
                                    elif opt == "pre" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < page_count:
                                        page += 1
                                    elif int(opt) > 0 and int(opt) < 11:
                                        one = result[int(opt) - 1]
                                        __news_service.update_unreview_news(one[0])
                            if opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    page_count = __news_service.get_all_count()
                                    result = __news_service.get_all_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX, "%d.%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "%d/%d" % (page, page_count))
                                    print(Fore.LIGHTRED_EX, "pre.上一页")
                                    print(Fore.LIGHTRED_EX, "next.下一页")
                                    print(Fore.LIGHTRED_EX, "back.返回上一层")
                                    print(Style.RESET_ALL)
                                    opt = input("请输入编号")
                                    if opt == "back":
                                        break
                                    elif opt == "pre" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < page_count:
                                        page += 1
                                    elif int(opt) > 0 and int(opt) < 11:
                                        one = result[int(opt) - 1]
                                        __news_service.delete_news(one[0])
                            elif opt == "back":
                                break
                    if opt == "2":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "1.新增用户")
                            print(Fore.LIGHTGREEN_EX, "2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "3.删除用户")
                            print(Fore.LIGHTRED_EX, "back.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("请输入编号")
                            if opt == "1":
                                os.system("clear")
                                username = input("请输入用户名")
                                password = input("请输入密码")
                                email = input("请输入电子邮箱")
                                role_id = input("请输入角色")
                                __user_service.insert_user(username, password, email, role_id)
                            elif opt == "back":
                                break
                    if opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print("登录失败, 3秒返回")
            time.sleep(3)               
    elif opt == "2":
        sys.exit(0)
        