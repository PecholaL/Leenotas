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
        boolean flag = false;  // 当前是否有flag占领者
        int currentHolder = 0;  // 当前flag占领者
        int currentHolderNum = 0;  // 当前占领者数量
        int [] nums = {1,2,3,4,5,3,3,2,2,1,5,1,4,1,1,2};

        for (int num : nums) {
            if (!flag) {
                flag = true;
                currentHolder = num;
                ++currentHolderNum;
            } else {
                if (num!=currentHolder) {
                    --currentHolderNum;
                    if (currentHolderNum==0) {
                        flag = false;
                    }
                } else {
                    ++currentHolderNum;
                }
            }
        }
        if (flag) {
            System.out.println(currentHolder);
        } else {
            System.out.println("no majority element");
        }
    }    
}
