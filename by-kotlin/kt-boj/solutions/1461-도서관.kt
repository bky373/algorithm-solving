import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val m = readLine().split(' ')[1].toInt()
    val positive = PriorityQueue<Int>()
    val negative = PriorityQueue<Int>()

    val st = StringTokenizer(readLine())
    while (st.hasMoreTokens()) {
        val position = st.nextToken().toInt()
        if (position > 0) {
            positive.offer(-position)
        } else {
            negative.offer(position)
        }
    }

    var longest = 0
    if (positive.isNotEmpty() && negative.isNotEmpty()) {
        longest = min(positive.peek(), negative.peek())
    } else if (negative.isEmpty()) {
        longest = positive.peek()
    } else if (positive.isEmpty()) {
        longest = negative.peek()
    }

    var result = 0

    while (positive.isNotEmpty()) {
        result += positive.poll()
        for (i in 1 until m) {
            if (positive.isNotEmpty()) {
                positive.poll()
            }
        }
    }

    while (negative.isNotEmpty()) {
        result += negative.poll()
        for (i in 1 until m) {
            if (negative.isNotEmpty()) {
                negative.poll()
            }
        }
    }

    print(-result * 2 + longest)
}
