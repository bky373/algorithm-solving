fun solution(seoul: Array<String>): String {
    var answer = seoul.indexOfFirst { a -> a == "Kim" }
    return "김서방은 ${answer}에 있다"
}
