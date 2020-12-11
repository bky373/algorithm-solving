fun solution(arr: IntArray, divisor: Int): List<Int> {
    val answer = arr.filter { it % divisor == 0 }.sorted()
    return if (answer.isEmpty()) listOf(-1) else answer
}

fun main() {
    solution(intArrayOf(5, 9, 7, 10), 5).forEach { print("$it ") }
}
