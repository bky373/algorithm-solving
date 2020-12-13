fun solution2016(a: Int, b: Int): String {
    val days = listOf(0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    val nameOfDay = listOf("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
    var total = 0

    for (i in 0 until a) {
        total += days[i]
    }
    total += b
    return nameOfDay[total % 7]
}

fun main() {
    print(solution2016(5, 24))
}
