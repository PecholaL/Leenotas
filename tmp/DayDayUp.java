import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DayDayUp {
    // main() for test
    public static void main(String [] args) {
        System.out.println("_hola_");
        DayDayUp t = new DayDayUp();
        
        // TEST
        String a = " as./!d./.dsa";
        System.out.println(t.isPalindrome(a));
    }


    /* 4.2
     * 验证回文串（忽视特殊字符及大小写）
     * 又是对语法和包装类和Collection类方法的考量
     * StringBuffer, Character, String
     */
    public boolean isPalindrome(String s) {
        StringBuffer sb = new StringBuffer(s.length());
        for (int i=0; i<s.length(); ++i) {
            Character ch = s.charAt(i);
            if (Character.isLetterOrDigit(ch)) {
                sb.append(Character.toLowerCase(ch));
            }
        }
        String s_ = sb.toString();
        if (s_.length()==0) {
            return true;
        } else {
            int ptrB = 0;
            int ptrE = s_.length()-1;
            while (ptrB<=ptrE) {
                if (s_.charAt(ptrB)!=s_.charAt(ptrE)) {
                    return false;
                } else {
                    ++ptrB;
                    --ptrE;
                }
            }
            return true;
        }
    }


    /* 4.1
     * 最佳卖股票时机
     * 首先我知道不要用两个for，那样不够优雅
     * 直接分治，但没想到有O(n)的方法
     */
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxRes = 0;
        for (int i=0; i<prices.length; ++i) {
            if (prices[i]<minPrice) {
                minPrice = prices[i];
            } else if (prices[i]-minPrice > maxRes) {
                maxRes = prices[i]-minPrice;
            }
        }
        return maxRes;
    }
    // Divide & Conquer
    public int maxProfit_DC(int[] prices) {
        if (prices.length <= 1) {
            return 0;
        } else {
            int start = 0;
            int end = prices.length;
            int mid = (start+end)/2;
            int left = maxProfit(Arrays.copyOfRange(prices, start, mid));
            int right = maxProfit(Arrays.copyOfRange(prices, mid, end));
            int cross = maxProfitCross(prices, mid);
            return Math.max(Math.max(left, right), cross);
        }
    }
    public int maxProfitCross(int[] prices, int mid) {
        if (prices.length <= 1) {
            return 0;
        } else {
            int leftMin = prices[0];
            int rightMax = prices[mid];
            for (int i=0; i<mid; ++i) {
                if (prices[i] < leftMin) {
                    leftMin = prices[i];
                }
                if (prices[mid+i] > rightMax) {
                    rightMax = prices[mid+i];
                }
            }
            if (prices[prices.length-1] > rightMax) {
                rightMax = prices[prices.length-1];
            }
            return rightMax - leftMin;
        }
    }


    /* 3.28
     * 杨辉三角 
     * 被难住的是Java语法，垃圾Python破坏手感
     */
    public List<List<Integer>> generateYangHui(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i=0; i<numRows; ++i) {
            List<Integer> tmp = new ArrayList<>();
            for (int j=0; j<i+1; ++j) {
                if (j==0 || j==i) {
                    tmp.add(1);
                } else {
                    tmp.add(res.get(i-1).get(j-1)+res.get(i-1).get(j));
                }
            }
            res.add(tmp);
        }
        return res;
    }
    // 获取三角第i行(从1开始)，采用滚动数组，每行从右往左，而不用将前面结果全部保存
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex==0) {
            return null;
        }
        List<Integer> res = new ArrayList<>();
        res.add(1);
        for (int i=1; i<=rowIndex; ++i) {
            res.add(0);
            for (int j=i; j>0; --j) {
                res.set(j, res.get(j)+res.get(j-1));
            }
        }
        return res;
    }
}