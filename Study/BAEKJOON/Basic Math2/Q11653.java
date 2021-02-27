import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q11653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        int i = 2;

        while (N != 1) {
            if (N % i == 0) {
                N /= i;
                sb.append(i).append('\n');
            } else {
                i++;
            }
        }
        
        System.out.print(sb);
    }
}
