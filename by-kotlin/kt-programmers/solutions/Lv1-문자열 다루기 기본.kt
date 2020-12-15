fun solutionStringBase(s: String): Boolean {
    return s.all { it.isDigit() } && (s.length == 4 || s.length == 6)
}
