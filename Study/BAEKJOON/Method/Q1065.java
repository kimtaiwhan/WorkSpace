import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q1065 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println(isHanSu(Integer.parseInt(br.readLine())));
    }

    public static int isHanSu(int N) {
        if (N < 100) {
            return N;
        } else {
            int cnt = 99;

            if (N == 1000) {
                N = 999;
            }

            for (int i = 100; i <= N; i++) {
                int arr[] = new int[3];

                arr[0] = i / 100;
                arr[1] = (i / 10) % 10;
                arr[2] = i % 10;

                if ((arr[2] - arr[1]) == (arr[1] - arr[0])) {
                    cnt++;
                }
            }
            return cnt;
        }
    }
}