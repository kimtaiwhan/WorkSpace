import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Q3009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x;
        int y;

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int dot_1_x = Integer.parseInt(st.nextToken());
        int dot_1_y = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");

        int dot_2_x = Integer.parseInt(st.nextToken());
        int dot_2_y = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");

        int dot_3_x = Integer.parseInt(st.nextToken());
        int dot_3_y = Integer.parseInt(st.nextToken());

        if (dot_1_x == dot_2_x) {
            x = dot_3_x;
        } else {
            if (dot_1_x == dot_3_x) {
                x = dot_2_x;
            } else {
                x = dot_1_x;
            }
        }

        if (dot_1_y == dot_2_y) {
            y = dot_3_y;
        } else {
            if (dot_1_y == dot_3_y) {
                y = dot_2_y;
            } else {
                y = dot_1_y;
            }
        }

        System.out.println(x + " " + y);
    }
}