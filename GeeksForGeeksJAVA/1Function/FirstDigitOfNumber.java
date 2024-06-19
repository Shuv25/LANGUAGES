import java.util.*;

public class FirstDigitOfNumber {

    public static int firstDigit(int num)
    {
        int ans=0;
        while(num>0)
        {
            ans=num;
            num=num/10;
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the num:");
        int num=sc.nextInt();

        System.out.println("The first digit of "+num+" is "+firstDigit(num));
    }    
}
