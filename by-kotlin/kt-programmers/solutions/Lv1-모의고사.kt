fun solution(answers: IntArray): IntArray {
    val student1 = intArrayOf(1, 2, 3, 4, 5)
    val student2 = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
    val student3 = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    val results = mutableListOf(0, 0, 0)
    var a = 0
    var b = 0
    var c = 0

    answers.indices.forEach { x ->
        if (a == student1.size) a = 0
        if (b == student2.size) b = 0
        if (c == student3.size) c = 0

        val anwser = answers[x]
        if (anwser == student1[a++]) results[0]++
        if (anwser == student2[b++]) results[1]++
        if (anwser == student3[c++]) results[2]++
    }

    val max = results.maxOrNull()
    val winners = mutableListOf<Int>()
    results.indices.forEach { x ->
        if (results[x] == max)
            winners.add(x + 1)
    }

    return winners.toIntArray()
}
