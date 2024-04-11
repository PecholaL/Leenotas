/*
 * O(n)时间 O(1)空间
 * 找到数组中出现次数最多的元素（出现次数大于n/2）
 */

/*
 * 看到的很有趣的解释
 * 不同的元素尝试占领flag
 * 从第一个元素开始，第一个占领
 * 如果第二个与之不同，则与flag下的一个占领者同归于尽
 * 如果相同，则该势力实力++
 * 最终出现最多的元素总能赢得旗帜
 */

public class MajorityElement {
    public static void main (String[] args) {

    }    
}
