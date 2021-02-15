import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q8958 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int Case = Integer.parseInt(br.readLine());

        String arr[] = new String[Case];

        for (int i = 0; i < Case; i++) {
            arr[i] = br.readLine();
        }

        for (int i = 0; i < Case; i++) {
            int sum = 0;
            int cnt = 0;

            for (int j = 0; j < arr[i].length(); j++) {
                if (arr[i].charAt(j) == 'O') {
                    cnt++;
                } else {
                    cnt = 0;
                }

                sum += cnt;
            }

            sb.append(sum).append("\n");
        }

        System.out.print(sb);
    }
}