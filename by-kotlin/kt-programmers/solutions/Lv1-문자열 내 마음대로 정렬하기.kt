fun solutionString1(strings: Array<String>, n: Int): Array<String> {
    return strings.also {
        it.sort()
        it.sortBy { it[n] }
    }
}

fun solutionString2(strings: Array<String>, n: Int): Array<String> {
    return strings.sortedWith(Comparator<String> { o1, o2 ->
        when (o1[n] == o2[n]) {
            true -> o1.compareTo(o2)
            false -> o1[n].compareTo(o2[n])
        }
    }).toTypedArray()

}

fun main() {
    solutionString1(arrayOf("abzcd", "cdzab", "abzfg", "abzaa", "abzbb", "bbzaa"), 2).forEach(System.out::println)
    solutionString2(arrayOf("abzcd", "cdzab", "abzfg", "abzaa", "abzbb", "bbzaa"), 2).forEach(System.out::println)
}
