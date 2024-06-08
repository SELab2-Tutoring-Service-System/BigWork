import pymysql
from select_ import select_for_stu_search

def stu_search(subject, stage, time, gender):
    res = ""
    # 手机号,密码

    result = select_for_stu_search(subject, stage, time, gender)
    print("查询结果:", result)
    
    if result == ():
        res = "无满足条件的家教,还有些其他推荐"
        result = []
        result += select_for_stu_search(subject, stage, None, gender)
        res = result
        print("中间查询",res)
        if len(result) == 0:
            result += select_for_stu_search(subject, stage, time, None)
            res = result
            print("中间查询",res)
            if len(result) == 0:
                result += select_for_stu_search(subject, stage, None, None)
                res = result
                print("中间查询",res)
                if len(result) == 0:
                    res = "暂无满足条件或条件相似的家教"
                else:
                    res = result
                    for dict in res:
                        dict["TR_s"] = dict["TR_s"].strftime("%Y-%m-%d %H:%M:%S")
                        dict["TR_e"] = dict["TR_e"].strftime("%Y-%m-%d %H:%M:%S")
    else:
        res = result
        for dict in res:
            dict["TR_s"] = dict["TR_s"].strftime("%Y-%m-%d %H:%M:%S")
            dict["TR_e"] = dict["TR_e"].strftime("%Y-%m-%d %H:%M:%S")

    return res


if __name__ == '__main__':
    pass