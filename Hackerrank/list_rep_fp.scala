/*

FP Question
Link in Problems.md

List Replication

*/

def f(num:Int,arr:List[Int]):List[Int] = {
    arr.flatMap(x => List.fill(num)(x))
}
