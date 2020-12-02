import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val k = nextInt()

    if (k >= n) {
        print(0)
        return@with
    }

    val data = arrayListOf<Int>()
    repeat(n) { data.add(nextInt()) }

    data.sort()

    val distances = arrayListOf<Int>()
    for (i in 1 until n) {
        distances.add(data[i] - data[i - 1])
    }
    distances.sortDescending()

    for (i in 0 until k - 1) {
        distances[i] = 0
    }

    print(distances.sum())
}
