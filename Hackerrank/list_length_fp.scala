/*

FP Question

Link in Problems.md

List Length

*/

def f(arr:List[Int]):Int = {
    def findLength(list: List[Int], acc: Int): Int = {
        if (list.isEmpty) acc
        else findLength(list.tail, acc + 1)
    }
    findLength(arr, 0)
}
