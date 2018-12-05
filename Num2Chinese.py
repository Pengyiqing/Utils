# 亿位以下的自然数
def num2Chinese(d):
    if 100000000 > d > 0:
        num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        kin = ['十', '百', '千', '万']
        num_str = list(str(d))
        num_str.reverse()
        Chinese_str = ""
        for index, i in enumerate(num_str):
            if index!=0:
                if i != "0":
                    Chinese_str = num[int(i)] + kin[(index%4)-1] + Chinese_str
                elif Chinese_str:
                    if index==4 :
                        if Chinese_str[0]!="零":
                            Chinese_str = kin[3] + "零" + Chinese_str
                        else:
                            Chinese_str = kin[3] + Chinese_str
                    if not(Chinese_str[0] in ["零", "万"] and i=="0"):
                        Chinese_str = num[int(i)] + Chinese_str

            else:
                if i != "0":
                    Chinese_str = num[int(i)] + Chinese_str
        if Chinese_str[:2] == "一十":
            Chinese_str = Chinese_str[1:]
        return Chinese_str
