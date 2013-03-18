'''
Q:
有一只青蛙，它一次可以跳1个或者2个台阶；现在面对前方n级的台阶，它总共能有几种不同的跳法？

There is a stair with n levels. A frog can jump up 1 level or 2 levels at one time on the stair.
How many ways are there for the frog to jump the bottom of the stairs to the top?

Answer:
乍一看是一道排列组合的问题，却可以通过递归的方式构造出优雅的解，如下：
(1)当n = 1时:
    明显，只能有1种跳法，既f(1) = 1;
(2)当n = 2时:
    明显，可以有2种跳法，既f(2) = 2;

(3)当n = 3时:
    f(3)就不像之前可以轻易就看出来了。但是我们可以知道，如果青蛙要跳上最后一级台阶的时候，它只有2种选择
        (3.1)它先跳到了第二级阶梯（倒数第一级），最后轻松跃上顶端
        (3.2)它先跳到了第一级阶梯（倒数第二级），最后奋力一跃跳上2级台阶来到顶端

    那么现在求解f(3)就成了求解3.1 和3.2这两个子问题了。
    对于3.1，解明显就是f(3-1) = f(2) = 2  
    而对于3.2，解明显就是f(3-2) = f(1) = 1
    于是f(3) = f(3 - 1) + f(3 - 2) = f(2) + f(1) = 3
...
...
(k)当n = k时：有递推式f(k) = f(k - 1) + f(k - 2), (k > 2)

综上：
此题有递推式：
f(n) =  1,                    (n = 1)
        2,                    (n = 2)
        f(n - 1) + f(n - 2),  (n > 2)
'''

def jumpStair(n):    
    if n == 1:
        return 1

    if n == 2:
        return 2

    return jumpStair(n - 1) + jumpStair(n - 2)
