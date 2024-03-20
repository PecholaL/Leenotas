/*
 * 快速幂 O(logn)计算a^n
 * 将取幂的任务按指数的二进制来分割为更小的任务
 *  3^{13} = 3^{1101b} = 3^8*3^4*3^1
 *  n有logn个二进制位，当分别算出a^1, a^2, a^4, ..., a^{logn}后，使用O(logn)次乘法即可得到a^n
 *  注意该序列中每个元素都是前一个元素的平方
 */

/*
 * 使用递归来解决
 *  递归终止条件：
 */

class BinExp {
    public static void main (String[] args) {
        System.out.println("Hola");
    }

    public int binExp (int a, int n) {
        if (n==0) {
            return 1;
        }
        int res = binExp (a, n/2);
        if (n%2==1) {
            return res * res * a;
        } else {
            return res * res;
        }
    }
 }