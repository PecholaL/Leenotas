import java.util.List;

public class May {
    // main() for test
    public static void main(String[] args) {
        System.out.println("hola");
    }

    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // LeetCode nr.2 链表中两数相加
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(-1);
        int carry = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode pr = res;
        while(!(p1==null && p2==null && carry==0)) {
            int tmpval = 0;
            if (p1==null && p2!=null) {
                tmpval = p2.val+carry;
                p2 = p2.next;
            } else if (p2==null && p1!=null) {
                tmpval = p1.val+carry;
                p1 = p1.next;
            } else if (p1==null && p2==null) {
                tmpval = carry;
            } else {
                tmpval = p1.val+p2.val+carry;
                p1 = p1.next;
                p2 = p2.next;
            }

            ListNode tmpNode = new ListNode();
            tmpNode.val = tmpval%10;
            carry = (int) tmpval/10;
            if (res.val==-1) {
                res = tmpNode;
                pr = res;
            } else {
                pr.next = tmpNode;
                pr = pr.next;
            }
        }
        return res;
    }



} // END May