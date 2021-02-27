import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q9020 {
    public static boolean[] prime = new boolean[10001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        isPrime();

        int T = Integer.parseInt(br.readLine());
        int start;
        int end;
        int n;

        for (int i = 0; i < T; i++) {
            n = Integer.parseInt(br.readLine());
            start = n / 2;
            end = n / 2;

            while (true) {
                if (!prime[start] && !prime[end]) {
                    sb.append(start).append(' ').append(end).append('\n');
                    break;
                }

                start--;
                end++;
            }
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