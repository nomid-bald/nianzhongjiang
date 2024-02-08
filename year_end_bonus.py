# 获取用户输入的整数
nianzhong = float(input("请输入年终："))
salary_sumyear = float(input("请输入明年全年应发工资总额："))
wuxianyijin_sumyear = float(input("请输入明年五险一金扣除金额："))
fujia_sumyear = float(input("请输入明年附加扣除费用："))
jiben_sumyear = float(input("请输入明年基本扣除费用："))

minnianzhong = 0
minsumshuijin = nianzhong
nianzhongtime = nianzhong
nzsl = 0
nzsj = 0
sumsl = 0
sumsj = 0
# 开始循环
while nianzhongtime > 0:
    nianzhong_1 = nianzhongtime - 1
    # 计算单独计税的年终
    if nianzhong_1 / 12 <= 36000 / 12:
        nzshuilv = 0.03
        nzsusuan = 0
    else:
        if 36000 / 12 < nianzhong_1 / 12 <= 144000 / 12:
            nzshuilv = 0.1
            nzsusuan = 210
        else:
            if 144000 / 12 < nianzhong_1 / 12 <= 300000 / 12:
                nzshuilv = 0.2
                nzsusuan = 1410
            else:
                if 300000 / 12 < nianzhong_1 / 12 <= 420000 / 12:
                    nzshuilv = 0.25
                    nzsusuan = 2660
                else:
                    if 420000 / 12 < nianzhong_1 / 12 <= 660000 / 12:
                        nzshuilv = 0.3
                        nzsusuan = 4410
                    else:
                        if 660000 / 12 < nianzhong_1 / 12 <= 960000 / 12:
                            nzshuilv = 0.35
                            nzsusuan = 7160
                        else:
                            if nianzhong_1 / 12 > 960000 / 12:
                                nzshuilv = 0.45
                                nzsusuan = 15160
    # 年终税金
    nzshuijin = nianzhong_1 * nzshuilv - nzsusuan

    # 计算24年应缴税金
    nianzhong_2 = nianzhong - nianzhong_1
    jiaoshui_sumyear = salary_sumyear + nianzhong_2 - fujia_sumyear - jiben_sumyear - wuxianyijin_sumyear
    if jiaoshui_sumyear <= 36000:
        shuilv_salary = 0.03
        susuan_salary = 0
    else:
        if 36000 < jiaoshui_sumyear <= 144000:
            shuilv_salary = 0.1
            susuan_salary = 2520
        else:
            if 144000 < jiaoshui_sumyear <= 300000:
                shuilv_salary = 0.2
                susuan_salary = 16920
            else:
                if 300000 < jiaoshui_sumyear <= 420000:
                    shuilv_salary = 0.25
                    susuan_salary = 31920
                else:
                    if 420000 < jiaoshui_sumyear <= 660000:
                        shuilv_salary = 0.3
                        susuan_salary = 52920
                    else:
                        if 660000 < jiaoshui_sumyear <= 960000:
                            shuilv_salary = 0.35
                            susuan_salary = 85920
                        else:
                            if jiaoshui_sumyear > 960000:
                                shuilv_salary = 0.45
                                susuan_salary = 181920
    shuijin_sumyear = jiaoshui_sumyear * shuilv_salary - susuan_salary
    sumshuijin = shuijin_sumyear + nzshuijin
    if minsumshuijin > sumshuijin:
        minnianzhong = nianzhong_1
        minsumshuijin = sumshuijin
        nzsj = nzshuijin
        nzsl = nzshuilv
        sumsj = shuijin_sumyear
        sumsl = shuilv_salary
    nianzhongtime -= 1

print("第一次发放年终是：", minnianzhong, "时总缴纳税金最小，税金为", minsumshuijin)
print("年终的税率为：", nzsl, ",税金为", nzsj)
print("工资税率：", sumsl, "，税金为", sumsj)
