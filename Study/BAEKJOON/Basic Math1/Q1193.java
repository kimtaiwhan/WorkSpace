import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Q1193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(br.readLine());
        
        int start = 1;
        int floor = 1;

        while (start + floor <= X) {
            start += floor;
            floor++;
        }

        int num = X - start;

        int x = num + 1;
        int y = floor - num;

        if (floor % 2 == 0) {
            System.out.printf("%d/%d", x, y);
        } else {
            System.out.printf("%d/%d", y, x);
        }
    }
}