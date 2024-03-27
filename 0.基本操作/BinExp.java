/*
 * 快速幂 O(logn)计算a^n
 * 将取幂的任务按指数的二进制来分割为更小的任务
 *  3^{13} = 3^{1101b} = 3^8*3^4*3^1
 *  n有logn个二进制位，当分别算出a^1, a^2, a^4, ..., a^{logn}后，使用O(logn)次乘法即可得到a^n
 *  注意该序列中每个元素都是前一个元素的平方
 */

class BinExp {
    public static void main (String[] args) {
        int a = 2;
        int n = 12;
        int res = binExp_rec(a, n);
        System.out.println(a+"^{"+n+"}="+res);
    }

    /*
    * 非递归
    */
    public static int binExp (int a, int n) {
        int res = 1;
        while (n>0) {
            if ((n&1)==1) {
                res = res*a;
            }
            a = a*a;
            n>>=1;
        }
        return res;
    }



    /*
    * 使用递归来解决
    *  递归终止条件：指数n的二进制所有“1”位右移完成，即n=0时
    *  每次递归调用右移一位后的指数
    *  https://oi-wiki.org/math/binary-exponentiation/
    */
    public static int binExp_rec (int a, int n) {
        if (n==0) {
            return 1;
        }
        int res = binExp (a, n>>1);
        if ((n&1)==1) {
            return res * res * a;
        } else {
            return res * res;
        }
    }
 }


//  Pechola注：善用移位运算，这样看上去很有气势。
