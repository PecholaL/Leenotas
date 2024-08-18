public class convertToTitle {
    /* 
     * 由数字返回列表名称
     * A-1, B-2, ... , Z-26, 
     * AA-27, AB-28, ... , ZZ-52,
     * 没有0的26进制
     * 如果取余得到0则代表在一行的末尾，即Z
     *  需要减去1再除以底数26^n
     */
    public static void main (String[] args) {
        int columnNumber = 52;
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
        System.out.println(sBuffer.toString());
    }
}
