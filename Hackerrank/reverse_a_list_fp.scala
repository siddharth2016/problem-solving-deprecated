/*

FP Question
Link in Problems.md

Reverse a List

*/

def f(arr:List[Int]): List[Int] = {
    def reverseList(head: Int, tail: List[Int], acc: List[Int]): List[Int] = {
        if (tail.isEmpty) head +: acc
        else reverseList(tail.head, tail.tail, head +: acc)
    }
    reverseList(arr.head, arr.tail, List())
}
