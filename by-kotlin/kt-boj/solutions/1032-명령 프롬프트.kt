import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val inputs = arrayListOf<String>()
    repeat(n) {
        inputs.add(next())
    }

    val first = inputs[0]
    val result = arrayListOf<String>()
    (first.indices).forEach { i ->
        var ck = false
        (1 until n).forEach { j ->
            if (first[i] != inputs[j][i]) {
                ck = true
            }
        }
        if (ck) {
            result.add("?")
        } else {
            result.add(first[i].toString())
        }
    }
    (result.indices).forEach { i ->
        print(result[i])
    }
}
