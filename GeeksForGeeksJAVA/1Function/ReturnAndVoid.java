import java.util.*;

public class ReturnAndVoid {

    public static void Details(String name,int age,String address)
    {
        System.out.println("Your Name:"+name);
        System.out.println("Your Age:"+age);
        System.out.println("Your Address:"+address);
    }
    public static int addAge(int age)
    {
        return age+40;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Name? ");
        String name=sc.nextLine();
        System.out.print("Age? ");
        int age=sc.nextInt();
        sc.nextLine();
        System.out.print("Address? ");
        String address=sc.nextLine();

        Details(name, age, address);

        System.out.println("After 40 years your age will be:"+addAge(age));

    }
}
