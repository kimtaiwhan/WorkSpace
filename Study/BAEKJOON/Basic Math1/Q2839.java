import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int Box = 0;

        while (true) {
            if (N % 5 == 0) {
                Box += N / 5;
                System.out.println(Box);
                break;
            }

            N -= 3;
            Box += 1;
            if (N < 0) {
                System.out.println(-1);
                break;
            }
        }
    }
}