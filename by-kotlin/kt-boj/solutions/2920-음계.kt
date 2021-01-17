import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var ascending = true
    var descending = true

    val nums = readLine().split(" ").map { it.toInt() }

    for (i in 0 until 7) {
        if (nums[i] < nums[i + 1]) descending = false
        else if (nums[i] > nums[i + 1]) ascending = false
    }

    if (ascending) println("ascending")
    else if (descending) println("descending")
    else println("mixed")
}
