# conding = utf - 8
import matplotlib.pyplot as plt


def distribution(ls, need):
    key = 0
    for i in range(len(ls)):
        if ls[i][0] > need > ls[i][0] // 2 and ls[i][1] == 0:
            ls[i][1] = 1  # 1为已分配绿色 0为未分配蓝色
            return ls
    if len(ls) == 1:
        while True:
            if need > ls[key][0] // 2 and ls[key][1] == 0:
                ls[key][1] = 1
                break
            else:
                if ls[key][0] // 2 == 64:
                    ls.append([])
                    ls[-1].append(ls[key][0] // 2)
                    ls[-1].append(1)
                    ls[key][0] = ls[key][0] // 2
                    break
                ls.append([])
                ls[-1].append(ls[key][0] // 2)
                ls[-1].append(0)
                ls[key][0] = ls[key][0] // 2
            key += 1
        return ls
    else:
        t = 1025
        for i in range(len(ls)):
            if t > ls[i][0] > need and ls[i][1] != 1:
                t = ls[i][0]
                f = i
        if ls[f][0] == 64:
            ls[f][1] = 1
            return ls
        while True:
            ls.insert(f + 1, [])
            ls[f + 1].append(ls[f][0] // 2)
            ls[f + 1].append(0)
            ls[f][0] = int(ls[f][0] / 2)
            if ls[f + 1][0] >= need > ls[f + 1][0] // 2:
                ls[f + 1][1] = 1
                return ls
            f += 1
            if ls[f][0] == 64:
                ls[f][1] = 1
                return ls


def recovery(ls, number):
    ls[number][1] = 0
    flag = 0
    for i in range(len(ls)):
        if ls[i][1] != 0:
            flag = 1
    if flag == 0:
        ls = [[1024, 0]]
        return ls
    while True:
        if number < len(ls) - 1:
            if ls[number - 1][1] == 0 and ls[number - 1][0] == ls[number][0]:
                ls[number - 1][0] = ls[number - 1][0] * 2
                del ls[number]
                number -= 1
            elif ls[number + 1][1] == 0 and ls[number + 1][0] == ls[number][0]:
                ls[number][0] = ls[number][0] * 2
                del ls[number + 1]
            else:
                break
        else:
            if ls[number - 1][1] == 0 and ls[number - 1][0] == ls[number][0]:
                ls[number - 1][0] = ls[number - 1][0] * 2
                del ls[number]
                number -= 1
            else:
                break
    return ls


ls = [[1024, 0]]
if __name__ == '__main__':
    while True:
        explode = [0.01 for i in range(len(ls))]
        labels = []
        for i in range(len(ls)):
            labels.append('Partition' + str(i) + ':' + str(ls[i][0]) + 'KB')
        t = []
        colors = []
        size = []
        for i in range(len(ls)):
            size.append(str(int(ls[i][0])))
            if ls[i][1] == 1:
                colors.append('lightgreen')
            else:
                colors.append('whitesmoke')
            t.append(ls[i][0])
        plt.pie(size, labels=labels, colors=colors, explode=explode, pctdistance=0.5, shadow=True,
                startangle=50, labeldistance=1.1)
        plt.show()
        while True:
            try:
                choice = int(input("输入1为分配，2为回收:"))
                if choice == 1 or choice == 2:
                    break
                else:
                    raise IOError
            except IOError:
                print("输入有误重新输入！！！")
        if choice == 1:
            need = int(input("请输入要分配内存的大小："))
            ls = distribution(ls, need)
        elif choice == 2:
            recover = int(input("请输入要回收的分区："))
            ls = recovery(ls, recover)
