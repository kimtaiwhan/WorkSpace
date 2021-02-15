public class Q4673 {
	public static void main(String[] args) {
		boolean[] cnpz = new boolean[10001];	// 1부터 10000이므로

		for (int i = 1; i < 100001; i++) {
			int n = d(i);
		
			if (n < 10001) {
				cnpz[n] = true;
			}
		}

		StringBuilder sb = new StringBuilder();
        
		for (int i = 1; i < 10001; i++) {
			if (!cnpz[i]) {
				sb.append(i).append("\n");
			}
        }
        
		System.out.println(sb);
    }
    
	public static int d(int num) {
		int sum = num;
    
		while (num != 0) {
			sum += num % 10;
			num = num / 10;
		}
    
		return sum;
	}
}