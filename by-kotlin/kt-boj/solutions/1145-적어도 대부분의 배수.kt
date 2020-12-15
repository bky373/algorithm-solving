import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val numbers = mutableListOf<Int>()
    repeat(5) { numbers.add(nextInt()) }

    numbers.sort()

    var result = 0
    val maximum = numbers[2] * numbers[3] * numbers[4]

    loop@ for (k in numbers[0]..maximum + 1) {
        var count = 0
        for (i in numbers.indices) {
            if (k % numbers[i] == 0 && k >= numbers[i]) {
                count += 1
            }
            if (count >= 3) {
                result = k
                break@loop
            }
        }
    }

    print(result)

}
