class Solution {
    fun solution(numbers: IntArray): List<Int> {
        val answer = mutableListOf<Int>()
        val n = numbers.size
        for (i in 0 until n - 1) {
            for (j in i + 1 until n) {
                answer.add(numbers[i] + numbers[j])
            }
        }

        return answer.distinct().sorted()
    }
}

fun main() {
    val s = Solution()
    print(s.solution(intArrayOf(2,1,3,4,1)))
}
