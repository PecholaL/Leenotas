import java.util.ArrayList;
import java.util.List;

public class DayDayUp {
    public static void main(String [] args) {
        System.out.println("hola");
        List<List<Integer>> r = new ArrayList<>();
        DayDayUp t = new DayDayUp();
        r = t.generate(5);
        System.out.println(r);
    }

    
    /*
     * 杨辉三角 3.28
     * 被难住的是Java语法，垃圾python破坏手感
     */
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<numRows;i++) {
            List<Integer> tmp = new ArrayList<>();
            for(int j=0;j<i+1;j++) {
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
    
}
