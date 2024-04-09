import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class DayDayUp {
    // main() for test
    public static void main(String [] args) {
        System.out.println("_hola_");
        DayDayUp t = new DayDayUp();
        
        // TEST
        int a = 701;
        System.out.println(t.convertToTitle(a));
    }

    /* 4.9
     * Excel列表名称
     * A-1, B-2, ... , Z-26, AA-27, AB-28, ...
     * 相当有趣，没有0的26进制
     */
    public String convertToTitle(int columnNumber) {
        StringBuffer sBuffer = new StringBuffer();
        while (columnNumber != 0) {
            int i = columnNumber%26;
            if (i==0) {
                sBuffer.append('Z');
                --columnNumber;
            } else {
                sBuffer.append((char)((int)('A')+i-1));
            }
            columnNumber = columnNumber/26;
        }
        sBuffer.reverse();
        return sBuffer.toString();
    }


    /* 4.9
     * 二叉树后序遍历
     */
    public List<Integer> postorderTraversal_r(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root==null) {
            return res;
        } else {
            trav_post(root, res);
            return res;
        }
    }
    public void trav_post(TreeNode node, List<Integer> res) {
        if (node==null) {
            return;
        } else {
            trav_post(node.left, res);
            trav_post(node.right, res);
            res.add(node.val);
        }
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        if (root == null) {
            return res;
        }
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (root.right == null || root.right == prev) {
                res.add(root.val);
                prev = root;
                root = null;
            } else {
                stack.push(root);
                root = root.right;
            }
        }
        return res;
    }


    /* 4.8
     * 二叉树前序遍历
     * 递归EZ
     */
    //* 树结点
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public List<Integer> preorderTraversal_r(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root==null) {
            return res;
        } else {
            trav(root, res);
        }
        return res;
    }
    public void trav(TreeNode node, List<Integer> res) {
        if (node==null) {
            return;
        } else {
            res.add(node.val);
            trav(node.left, res);
            trav(node.right, res);
        }
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        if (root==null) {
            return res;
        }
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode tmp = stack.pop();
            res.add(tmp.val);
            if (tmp.right!=null) {
                stack.push(tmp.right);
            } 
            if (tmp.left!=null) {
                stack.push(tmp.left);
            }
        }
        return res;
    }


    /* 4.7
     * 判断环形链表（链表中是否存在环）
     * 想到了可以用快慢指针，但以前接触的快慢指针速度是一样的 :(
     */
    //* 链表结点数据结构：
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
     }
    public boolean hasCycle(ListNode head) {
        if (head==null || head.next==null) {
            return false; 
        } else {
            HashSet<ListNode> hSet = new HashSet();
            while (head.next!=null) {
                if (hSet.contains(head.next)) {
                    return true;
                } else {
                    hSet.add(head.next);
                    head = head.next;
                }
            }
            return false;
        }
    }
    public boolean hasCycle_sf(ListNode head) {
        if (head==null || head.next==null) {
            return false;
        } else {
            ListNode fast = head;
            ListNode slow = head;
            while (fast!=null && fast.next!=null) {
                fast = fast.next.next;
                slow = slow.next;
                if (fast==slow) {
                    return true;
                }
            }
            return false;
        }
    }


    /* 4.2
     * 只出现一次的元素（只有一个元素出现一次，其余出现两次）
     * 练习了哈哈希集，然后看到O(n)时间+O(1)空间的方法是异或运算
     * xor不同为1，相同为0
     */
    public int singleNumber(int[] nums) {
        if (nums.length==1) {
            return nums[0];
        } else {
            HashSet<Integer> hSet = new HashSet<Integer>();
            for (int i: nums) {
                if (hSet.contains(i)) {
                    hSet.remove(i);
                } else {
                    hSet.add(i);
                }
            }
            int res = 0;
            for (int i: hSet) {
                res = i;
            }
            return res;
        }
    }
    public int singleNumber_xor(int[] nums) {
        int res = 0;
        for (int i : nums) {
            res = res^i;
        }
        return res;
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