/*
 * 没有重复字符的最长子串的长度
 */

import java.util.HashSet;
import java.util.Set;

public class LongestSubstringLength {
    public static void main(String[] args) {
        String s = new String("abcabcdeebcdfs");
        LongestSubstringLength obj = new LongestSubstringLength();
        int res = obj.lenghthOfLongestSubstring(s);
        System.out.println(res);
    }

    public int lenghthOfLongestSubstring(String s) {
        if (s.length()==0) {
            return 0;
        }
        Set<Character> hset = new HashSet<>();
        // 右指针ptr，左指针i
        int len = s.length();
        int ptr = -1, res = 0;

        // 逐步对每个左指针所在的位置，
        //    移动右指针，直到右指针移动到尾或出现重复
        // 移动左指针并去除之前左指针所在位置的元素
        for (int i=0; i<len; ++i) {
            if (i!=0) {
                hset.remove(s.charAt(i-1));
            }
            // 先确定右指针将指向的下一个元素是否在集合中
            while (ptr+1<len && !hset.contains(s.charAt(ptr+1))) {
                hset.add(s.charAt(ptr+1));
                ++ptr;
            }
            res = Math.max(res, ptr-i+1);
        }
        return res;
    }
    
}
