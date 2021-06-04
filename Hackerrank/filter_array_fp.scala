/*

FP Question
Link in Problems.md

Filter Array

*/

def f(delim:Int,arr:List[Int]):List[Int] = {
    arr.filter(x => x < delim)
}
