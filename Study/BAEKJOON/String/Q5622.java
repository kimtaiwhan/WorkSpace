import java.io.IOException;

public class Q5622 {
    public static void main(String[] args) throws IOException {
        int count = 0;
        int val;

        while (true) {
            val = System.in.read();

            if (val == '\n') {
                break;
            }

            if (val < 68) count += 3;
            else if (val < 71) count += 4;
            else if (val < 74) count += 5;
            else if (val < 77) count += 6;
            else if (val < 80) count += 7;
            else if (val < 84) count += 8;
            else if (val < 87) count += 9;
            else count += 10;
        }

        System.out.println(count);
    }
}