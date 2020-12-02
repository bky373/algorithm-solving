import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val N = nextInt()
    val m = nextInt()
    val M = nextInt()
    val T = nextInt()
    val R = nextInt()
    var x = m

    var exercise = 0
    var amount = 0

    if (m + T > M) {
        print(-1)
        return@with
    }

    while (true) {
        if (exercise == N) {
            print(amount)
            break
        }
        if (x + T <= M) {
            exercise += 1
            x += T
        } else {
            x -= R
            if (m > x) {
                x = m
            }
        }
        amount += 1
    }
}
