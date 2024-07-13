'''



##[BUG]样例
①
[92, 91, 23, 31, 47, 98, 67, 92, 27, 38, 74, 12, 85, 10, 43, 31, 18, 95, 64, 26, 77, 27, 40, 96, 5, 23, 11, 80, 83, 87, 51, 43, 40, 21, 13, 59, 72, 63, 56, 0, 30, 47, 24, 48, 26, 19, 94, 45, 18, 87, 41, 20, 9, 11, 32, 9, 89, 23, 69, 15, 44, 59, 36, 95, 83, 80, 8, 24, 44, 27, 23, 38, 37, 46, 20, 43, 85, 30, 5, 74, 49, 92, 40, 62, 83, 93, 17, 70, 23, 37, 87, 39, 56, 91, 83, 13, 17, 83, 81, 87]
9
②txt文件中第四个样例、第九个样例、第十个样例
报错信息：超过了最大递归层数，算法的问题！



一家物流公司有[一辆]载重为 w 的货车和[一系列]重量为 w1, w2 ,..., wn 的包裹，这些包裹需要在 [d 天]内运输完成。
由于包裹是被有序生产出来的，每一天要按照包裹的[顺序]往车辆上装载包裹，但装载的总重量不能超过载重 w。
请计算如果在 [d 天内]（但最小的载重应该是d天完成的）将包裹全部运输完，货车所需要的最低载重 w 。

输入格式：
一共两行，第一行是一个列表，表示所有包裹对应的重量；第二行表示天数 d。
输出格式：
在规定时间内将包裹全部运输完所需要的最低载重。
###tip:这些包裹可不一定是从小到大的呢！
###tip：最小的载重应该是d天完成的，天数越少，最小载重越大！
示例输入：
[1,2,3,4,5,6,7,8,9,10]
5
示例输出：
15
解释：
最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此选择载重为 14 并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的

[3,3,3,3]
2
[1,2,2,4]
2

'''


load=eval(input())#处理输入的列表好帮手
day=int(input())
l=load[:]
chang=len(load)
l.sort()
maxw=load[-1]
#让w通过递归，从小往大搜索，如果可以的话，直接输出
def log(day_remain,burden,load_remain):#从小到大搜索，不会出现剩余天数>0，货物全被运输完成的事情呢
    global day,load
    if day_remain==0 and load_remain!=[]:#剩余可用天数为0 而且 货物还没有运输完>>burden给小了
        return log(day,burden+1,load[:])
    elif day_remain==0 and load_remain==[]:#所有天数都用完了 而且 货物也运输完毕了
        return burden#找到了 最小运输重量
    else:
        sum=0
        loadding=load_remain[:]
        for i in range(0,len(load_remain)):
            if sum+load_remain[i]<=burden:
                sum+=load_remain[i]
                loadding.remove(load_remain[i])
            else:
                break
        return log(day_remain-1,burden,loadding)#【BUG】有返回值的递归必须要每一次调用都有return的！
loadd=load[:]
target=log(day,maxw,loadd)
print(target)

#[BUG]!!!传参数的时候是不是引用的原来的列表！
























