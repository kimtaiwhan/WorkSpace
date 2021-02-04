import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q2742 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        br.close();

        StringBuilder sb = new StringBuilder();

        for (int i = N; i > 0; i--) sb.append(i + "\n");

        System.out.println(sb);
    }
}