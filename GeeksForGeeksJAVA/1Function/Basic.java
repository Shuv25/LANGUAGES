public class Basic {
    public static void funtwo() {
        System.out.println("Inside Fun Two ");
    }

    public static void funone() {
        System.out.println("Fun One Begins");
        funtwo();
        System.out.println("Fun One Ends");
    }

    public static void main(String[] args) {
        System.out.println("Main Begins");
        funone();
        System.out.println("Main Ends");
    }
}
