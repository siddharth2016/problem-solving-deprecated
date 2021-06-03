/*

FP Question
Link in Problems.md

Hello World N Times

*/


def f(n: Int) = {
    for {
    x <- 0 until n
    } println("Hello World")
}
