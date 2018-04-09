import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class BigSorting {
    BigInt[] unsorted;

    private class BigInt implements Comparable<BigInt> {
        String number;

        public BigInt(String s) {
            number = s;
        }

        public int compareTo(BigInt another) {
            if (number.length() != another.number.length()) { return number.length() - another.number.length(); }
            int i = 0;
            while (i < number.length()-1 && number.charAt(i) == another.number.charAt(i)) { i++; }
            return number.charAt(i) - another.number.charAt(i);
        }
    }

    public BigSorting(Scanner in) {
        int n = in.nextInt();
        unsorted = new BigInt[n];
        for(int unsorted_i=0; unsorted_i < n; unsorted_i++){
            unsorted[unsorted_i] = new BigInt(in.next());
        }
    }
    
    public void sort() {
        Arrays.sort(unsorted);
        for (BigInt bi : unsorted)
            System.out.println(bi.number);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigSorting bs = new BigSorting(in);
        bs.sort();
    }
}
