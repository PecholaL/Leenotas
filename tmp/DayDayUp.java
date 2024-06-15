import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

import javax.swing.tree.TreeNode;

public class DayDayUp {
    // main() for test
    public static void main(String [] args) {
        System.out.println("_hola_");
        DayDayUp t = new DayDayUp();
        
        // TEST
        int a = 701;
        String s = "ABB";
        System.out.println(t.titleToNumber(s));
    }


    /* 6.15
     * 无重复字符的最长子串的长度
     */
    public int lenghthOfLongestSubstring(String s) {
        if (s.length()==0) {
            return 0;
        }
        Set<Character> hset = new HashSet<>();
        // 右指针ptr，左指针i
        int len = s.length();
        int ptr = -1, res = 0;
        for (int i=0; i<len; ++i) {
            if (i!=0) {
                hset.remove(s.charAt(i-1));
            }
            while (ptr+1<len && !hset.contains(s.charAt(ptr+1))) {
                hset.add(s.charAt(ptr+1));
                ++ptr;
            }
            res = Math.max(res, ptr-i+1);
        }
        return res;
    }
    // 头一天刷了这道题，第二天在联洲的机试中碰到，记得方法但写不出来:(

    
    /* 6.6
     * 颠倒二进制位
     */
    public reverseBits(int n) {
        int res = 0;
        for (int i=0; i<32; ++i) {
            int p = n & 1; // 获得当前最低位
            n = n>>1;
            res = res | (p<<(31-i)); // 将p移位到目标位，即左移31-i位
        }
        return res;
    }


    /* 4.18
     * Excel列表序号
     */
    public int titleToNumber(String columnTitle) {
        String revColumnTitle = new StringBuffer(columnTitle).reverse().toString();
        int base = 1;
        int res = 0;
        for (int i=0; i<revColumnTitle.length(); ++i) {
            char ch = revColumnTitle.charAt(i);
            int val = (int)(ch-'A'+1) * base;
            res = res + val;
            base = base * 26;
        }
        return res;
    }


    /* 4.11
     * 多数元素
     * 返回数组中出现次数大于n/2的元素
     * 练习哈HashMap先
     * 更好的方法有排序（排序后下表为n/2的元素），分治，随机
     */
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        for (int num : nums) {
            if (!counts.containsKey(num)) {
                counts.put(num, 1);
            } else {
                counts.put(num, counts.get(num)+1);
            }
        }
        Map.Entry<Integer, Integer> resEntry = null;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (resEntry==null || entry.getValue()>resEntry.getValue()) {
                resEntry = entry;
            }
        }
        return resEntry.getKey();
    }


    /* 4.11
     * 相交链表
     * 返回相交结点
     * 自己的方法写了一大段，看到题解解决不同长度问题可以只遍历一遍
     * 两个指针分别从两个head开始往后，当较短链表的指针指向null时
     * 将其指向还没走完的链表（较长者）的头部，两个指针继续走直到较长链表走完
     * 将走完较长链表的指针指向较短链表head，此时两个指针距离尾部的距离相同
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA==null || headB==null) {
            return null;
        } else {
            int lenA = 0;
            int lenB = 0;
            ListNode ptrA = new ListNode(0);
            ListNode ptrB = new ListNode(0);
            for (ptrA=headA; ptrA!=null; ptrA=ptrA.next) {
                ++lenA;
            }
            for (ptrB=headB; ptrB!=null; ptrB=ptrB.next) {
                ++lenB;
            }
            ptrA = headA;
            ptrB = headB;
            if (lenA>lenB) {
                int diff = lenA - lenB;
                int i = 0;
                while (i<diff) {
                    ptrA = ptrA.next;
                    ++i;
                }
            } else {
                int diff = lenB - lenA;
                int i = 0;
                while (i<diff) {
                    ptrB = ptrB.next;
                    ++i;
                }
            }
            boolean flag = false;
            ListNode res = new ListNode(0);
            while (ptrA!=null) {
                if (ptrA==ptrB) {
                    if (!flag) {
                        res = ptrA;
                    }
                    flag = true;
                } else {
                    flag = false;
                }
                ptrA = ptrA.next;
                ptrB = ptrB.next;
            }
            if (flag) {
                return res;
            } else {
                return null;
            }
        }
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