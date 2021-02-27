import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Q1002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        StringTokenizer st;

        int x1, y1, r1, x2, y2, r2, rs, rm;
        double d;

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            r1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            r2 = Integer.parseInt(st.nextToken());

            d = Math.sqrt((Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2)));

            rs = r1 + r2;
            rm = Math.abs(r1 - r2);

            if (d == 0) {
                if (r1 == r2) {
                    sb.append(-1).append('\n');
                } else {
                    sb.append(0).append('\n');
                }
            } else {
                if (d == rs || d == rm) {
                    sb.append(1).append('\n');
                }
                
                else if (d < rs && d > rm) {
                    sb.append(2).append('\n');
                }

                else {
                    sb.append(0).append('\n');
                }
            }
        }

        System.out.print(sb);
    }
}