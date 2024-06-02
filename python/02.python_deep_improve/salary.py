"""
本模块用来计算公司员工的薪资
"""
company = "BaiDu"

def yearSalary(monthSalary):
    """根据传入的月薪计算年薪"""
    return monthSalary*12
    
def daySalary(monthSalary):
    """根据传入的月薪计算每日的薪资（按照一个月22.5天计算）"""
    return monthSalary/22.5
    
if __name__ == "__main__":
    # 方法测试
    print(yearSalary(3000))
