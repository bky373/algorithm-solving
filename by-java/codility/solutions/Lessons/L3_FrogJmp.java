package Lessons;

// 시간복잡도 : O(1)

class L3_FrogJmp {
    public int solution(int X, int Y, int D) {
        int jumpCount = (Y - X) / D;
        return jumpCount + ((Y - X) % D == 0 ? 0 : 1);
    }

    public static void main(String[] args) {
        L3_FrogJmp s = new L3_FrogJmp();
        int X = 10;
        int Y = 85;
        int D = 30;

        System.out.println(s.solution(X, Y, D));
    }
}
