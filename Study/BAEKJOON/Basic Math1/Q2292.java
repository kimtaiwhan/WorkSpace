import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q2292 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int start = 1;
        int num = 1;

        if (N == 1) {
            System.out.println(1);
        } else {
            while (N > start) {
                start += 6 * num;
                num += 1;
            }
            System.out.println(num);
        }
    }
}