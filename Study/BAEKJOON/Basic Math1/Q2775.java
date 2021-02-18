import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int Test_Case = Integer.parseInt(br.readLine());

        int k;
        int n;
        int[] arr;

        for (int a = 0; a < Test_Case; a++) {
            k = Integer.parseInt(br.readLine());
            n = Integer.parseInt(br.readLine());
            arr = new int[n];

            for (int b = 0; b < n; b++) {
                arr[b] = b + 1;
            }

            for (int b = 0; b < k; b++) {
                for (int c = 1; c < n; c++) {
                    arr[c] += arr[c - 1];
                }
            }

            sb.append(arr[arr.length - 1]).append('\n');
        }

        System.out.print(sb);
    }    
}