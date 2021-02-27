import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q4948 {
    public static boolean prime[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n;
        int cnt;

        while (true) {
            n = Integer.parseInt(br.readLine());
            cnt = 0;

            if (n == 0) break;

            prime = new boolean[2 * n + 1];
            isPrime();

            for (int i = n + 1; i <= 2 * n; i++) {
                if (prime[i] == false) cnt++;
            }

            sb.append(cnt).append("\n");
        }

        System.out.print(sb);
    }

    public static void isPrime() {
        prime[0] = true;
        prime[1] = true;

        for (int i = 2; i <= Math.sqrt(prime.length); i++) {
            if (prime[i]) continue;

            for (int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }
    }
}
