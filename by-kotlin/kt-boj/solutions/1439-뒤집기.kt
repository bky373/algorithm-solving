import java.util.*
import kotlin.math.min

fun main() = with(Scanner(System.`in`)) {
    val data = next()

    fun solve(data: String): Int {
        val cnts = arrayListOf<Int>(0, 0)
        val cdata = data.toCharArray()
        if (cdata[0] == '1') {
            cnts[0] += 1
        } else {
            cnts[1] += 1
        }

        for (i in 0 until cdata.size - 1) {
            if (cdata[i] != cdata[i + 1]) {
                if (cdata[i + 1] == '1') {
                    cnts[0] += 1
                } else {
                    cnts[1] += 1
                }
            }
        }

        return min(cnts[0], cnts[1])
    }

    print(solve(data))
}
