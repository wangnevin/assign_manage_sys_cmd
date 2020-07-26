from service.user_service import UserService
from service.role_service import RoleService
from service.type_service import TypeService
from service.assign_service import AssignService
from colorama import  Fore, Style
from getpass import getpass
from datetime import datetime
import time
import sys
import os

__user_service = UserService()
__role_service = RoleService()
__type_service = TypeService()
__assign_service = AssignService()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t================================")
    print(Fore.LIGHTBLUE_EX, "\n\t      欢迎使用作业管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t================================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登陆系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号: ")

    if opt == "1":
        username = input("\n\t用户名: ")
        password = getpass("\n\t密码: ")
        result = __user_service.login(username, password)

        if result == True:
            role = __role_service.search_role(username)
            print(Fore.LIGHTGREEN_EX, "\n\t登陆成功（身份：{}）".format(role))
            print(Style.RESET_ALL)
            time.sleep(1)

            if role == "学生":
                while True:
                    os.system("cls")
                    print(Fore.LIGHTGREEN_EX, "\n\t1.提交作业")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑作业")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号: ")

                    if opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
                    elif opt == "1":
                        os.system("cls")
                        student_id = __user_service.search_id(username)
                        title = input("\n\t作业标题: ")
                        result = __type_service.search_list()
                        for i in range(len(result)):
                            one = result[i]
                            print("\n\t{}.{}".format(i+1, one[1]))
                        opt = input("\n\t类型编号: ")
                        type_id = result[int(opt)-1][0]
                        file_path = input("\n\t输入文件路径: ")
                        f = open(file_path, 'r', encoding='utf-8')
                        content = f.read()
                        f.close()
                        is_commit = input("\n\t是否提交(Y/N): ")
                        if is_commit == "Y" or is_commit == "y":
                            __assign_service.insert(title, username, type_id, content)
                            print("\n\t提交成功（3秒自动返回）")
                            time.sleep(3)
                            continue
                    elif opt == "2":
                        page = 1
                        while True:
                            os.system("cls")
                            result = __assign_service.search_list(page)
                            count_page = __assign_service.search_count_page()
                            for i in range(len(result)):
                                one = result[i]
                                print("\n\t{}.\t{}\t{}\t{}".format(i+1, one[1], one[2], one[3]))
                            print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                            print(Fore.LIGHTBLUE_EX, "\n\t{}/{}".format(page, count_page))
                            print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号: ")
                            if opt == "back":
                                break
                            elif opt == "prev" and page > 1:
                                page = page - 1
                            elif opt == "next" and page < count_page:
                                page = page + 1
                            elif opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                                os.system("cls")
                                assign_id = result[int(opt)-1][0]
                                title = result[int(opt)-1][1]
                                type = result[int(opt)-1][2]
                                print("\n\t新闻原标题: {}".format(title))
                                new_title = input("\n\t新标题: ")
                                print("\n\t新闻原类型: {}".format(type))
                                result = __type_service.search_list()
                                for i in range(len(result)):
                                    one = result[i]
                                    print("\n\t{}.{}".format(i + 1, one[1]))
                                opt = input("\n\t类型编号: ")
                                type_id = result[int(opt) - 1][0]
                                file_path = input("\n\t输入文件路径: ")
                                f = open(file_path, 'r', encoding='utf-8')
                                content = f.read()
                                f.close()
                                is_commit = input("\n\t是否提交(Y/N): ")
                                if is_commit == "Y" or is_commit == "y":
                                    __assign_service.update(assign_id, new_title, type_id, content)
                                    __assign_service.delete_cache(assign_id)
                                    print("\n\t提交成功（3秒自动返回）")
                                    time.sleep(3)
                                    continue

            elif role == "教师":
                while True:
                    os.system("cls")
                    print(Fore.LIGHTGREEN_EX, "\n\t1.作业管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.学生管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号: ")

                    if opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
                    elif opt == "1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.批改作业")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除作业")
                            print(Fore.LIGHTRED_EX, "\n\t----------------------")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号: ")

                            if opt == "back":
                                break
                            elif opt == "1":
                                page = 1
                                while True:
                                    os.system("cls")
                                    result = __assign_service.search_unreview_list(page)
                                    count_page = __assign_service.search_unreview_count_page()

                                    for i in range(len(result)):
                                        one = result[i]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{}.\t{}\t{}".format(i+1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号: ")

                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page = page - 1
                                    elif opt == "next" and page < count_page:
                                        page = page + 1
                                    elif opt in ['1','2','3','4','5','6','7','8','9','10']:
                                        os.system("cls")
                                        assign_id = result[int(opt)-1][0]
                                        title = result[int(opt)-1][1]
                                        type = result[int(opt)-1][2]
                                        username = result[int(opt)-1][3]
                                        content_id = __assign_service.search_content_id(assign_id)
                                        content = __assign_service.get_content(content_id)
                                        create_time = str(datetime.now())
                                        content_lines = content.split("\n")
                                        print(Fore.LIGHTGREEN_EX, "\n\t学生姓名: {}".format(username))
                                        print(Fore.LIGHTGREEN_EX, "\n\t作业题目: {}".format(title))
                                        print(Fore.LIGHTGREEN_EX, "\n\t作业科目: {}".format(type))
                                        print(Fore.LIGHTGREEN_EX, "\n\t=====================================\n")
                                        print(Style.RESET_ALL)
                                        for line in content_lines:
                                            print("\t{}".format(line))
                                        print(Fore.LIGHTGREEN_EX, "\n\t=====================================\n")
                                        print(Style.RESET_ALL)
                                        is_commit = input("\n\t是否审批(Y/N):")
                                        if is_commit == "Y" or is_commit == "y":
                                            __assign_service.update_unreview_assign(assign_id)
                                            __assign_service.cache_assign(assign_id, title, username, type, content, create_time)

                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    result = __assign_service.search_list(page)
                                    count_page = __assign_service.search_count_page()

                                    for i in range(len(result)):
                                        one = result[i]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t{}.\t{}\t{}\t{}".format(i + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号: ")

                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page = page - 1
                                    elif opt == "next" and page < count_page:
                                        page = page + 1
                                    elif opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                                        assign_id = result[int(opt) - 1][0]
                                        __assign_service.delete_assign(assign_id)
                                        __assign_service.delete_cache(assign_id)

                    elif opt == "2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加学生信息")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改学生信息")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除学生信息")
                            print(Fore.LIGHTRED_EX, "\n\t----------------------")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号: ")

                            if opt == "back":
                                break
                            elif opt == "1":
                                os.system("cls")
                                username = input("\n\t学生姓名: ")
                                password = getpass("\n\t密码: ")
                                password2 = getpass("\n\t再次输入密码: ")
                                if password != password2:
                                    print(Fore.LIGHTRED_EX, "\n\t两次密码输入不一致（3秒自动返回）")
                                    print(Style.RESET_ALL)
                                    time.sleep(3)
                                    continue
                                email = input("\n\t邮箱: ")
                                is_commit = input("\n\t是否保存(Y/N): ")
                                if is_commit in ["Y", "y"]:
                                    __user_service.insert(username, password, email)
                                    print("\n\t保存成功（3秒自动返回）")
                                    time.sleep(3)
                                    continue
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    result = __user_service.search_list(page)
                                    count_page = __user_service.search_count_page()
                                    for i in range(len(result)):
                                        one = result[i]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{}.\t{}".format(i+1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号: ")

                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page = page - 1
                                    elif opt == "next" and page < count_page:
                                        page = page + 1
                                    elif opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        username = result[int(opt)-1][1]
                                        email = result[int(opt)-1][2]
                                        print("\n\t原用户名: {}".format(username))
                                        new_username = input("\n\t新用户名: ")
                                        new_password = getpass("\n\t新密码: ")
                                        new_password2 = getpass("\n\t再次输入新密码: ")
                                        if new_password != new_password2:
                                            print(Fore.LIGHTRED_EX, "\n\t两次密码输入不一致（3秒自动返回）")
                                            print(Style.RESET_ALL)
                                            time.sleep(3)
                                            continue
                                        print("\n\t原邮箱: {}".format(email))
                                        new_email = input("\n\t新邮箱: ")
                                        is_commit = input("\n\t是否保存(Y/N): ")
                                        if is_commit in ["y", "Y"]:
                                            __user_service.update(user_id, new_username, new_password, new_email)
                                            print("\n\t保存成功（3秒自动返回）")
                                            time.sleep(3)
                                            continue
                            elif opt == "3":
                                page = 1
                                while True:
                                    os.system("cls")
                                    result = __user_service.search_list(page)
                                    count_page = __user_service.search_count_page()
                                    for i in range(len(result)):
                                        one = result[i]
                                        print(Fore.LIGHTBLUE_EX, "\n\t{}.\t{}".format(i + 1, one[1], one[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t{}/{}".format(page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t--------------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号: ")

                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page = page - 1
                                    elif opt == "next" and page < count_page:
                                        page = page + 1
                                    elif opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        __user_service.delete_user(user_id)

        elif result == False:
            print(Fore.LIGHTRED_EX, "\n\t登录失败（3秒自动返回）")
            print(Style.RESET_ALL)
            time.sleep(3)
            continue

    elif opt == "2":
        sys.exit(0)

