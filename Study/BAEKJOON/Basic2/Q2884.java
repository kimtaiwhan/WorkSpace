import java.util.Scanner;

public class Q2884 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int H = input.nextInt();
        int M = input.nextInt();
        input.close();
        if (H == 0) {
            if (M < 45) {
                System.out.println(23 + " " + (M + 15));
            } else {
                System.out.println(0 + " " + (M - 45));
            }
        } else {
            if (M < 45) {
                System.out.println((H - 1) + " " + (M + 15));
            } else {
                System.out.println(H + " " + (M - 45));
            }
        }
    }
}
