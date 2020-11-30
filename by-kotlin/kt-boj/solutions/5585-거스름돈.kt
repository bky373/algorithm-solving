import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()

    fun solve(myMoney: Int, paid: Int): Int {
        val coins = arrayListOf(500, 100, 50, 10, 5, 1)
        var v = myMoney - paid
        var i = 0
        var cnt = 0
        while (v > 0) {
            if (v >= coins[i]) {
                v -= coins[i]
                cnt += 1
            } else {
                i += 1
            }
        }
        return cnt
    }

    print(solve(1000, n))
}
