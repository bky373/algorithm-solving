package Lessons;

// Lesson3: Time Complexity
// Task: FrogJmp

class L3_FrogJmp {
    public int solution(int X, int Y, int D) {
        int jumpCount = (Y - X) / D;
        if ((Y - X) % D == 0) {
            return jumpCount;
        }
        return jumpCount + 1;
    }

    public static void main(String[] args) {
        L3_FrogJmp s = new L3_FrogJmp();
        int X = 10;
        int Y = 85;
        int D = 30;

        System.out.println(s.solution(X, Y, D));
    }
}
