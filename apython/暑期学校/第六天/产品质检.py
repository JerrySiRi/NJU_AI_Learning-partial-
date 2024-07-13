'''
题目：产品质检
题目描述：
质检部门需要对一项产品进行跌落测试，可以测试的最大高度为n米，测试员只会选择高度为整数的位置进行测试。
测试目的在于测试出产品的跌落极限高度 h （0 <= h <= n），任何从高于 h 处落下的产品都会损坏，而从 h 高度或更低高度落下的产品都完好无损。
现一共有 k 个相同的产品可用于测试。

每次操作，你可以取一个完好无损的产品并把它从任一高度 x 扔下（满足 1 <= x <= n）。
如果产品损坏，你就不能再次使用它。如果该产品跌落后没有损坏，则可以在之后的操作中重复使用这个产品。

请你计算并返回要确定 h 确切的值的最小操作次数是多少？

输入格式：
一共两行，第一行表示产品数量 k；第二行表示测试高度 n。
输出格式：
确定 h 确切的值的最小操作次数。

输入样例：
1
2
输出样例：
2
解释：
产品从 1 米掉落。如果它损坏了，肯定能得出 h = 0 。
否则，产品从 2 米掉落。如果它损坏，肯定能得出 h = 1 ；
如果它没损坏，那么肯定能得出 h = 2 。
因此，在最坏的情况下我们需要 2 次操作来确定 h 是多少。

输入样例：
2
3
输出样例：
2
解释：
选一个产品从 2 米掉落。如果它损坏了，用另一个产品从 1 米掉落，肯定能得出 h = 0或1 。
否则，产品从 3 米掉落，肯定能得出 h = 2或3；
因此，在最坏的情况下我们需要 2 次操作来确定 h 是多少。
'''