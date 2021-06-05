/*

FP Question
Link in Problems.md

Sum Of Odd Elements

*/

def f(arr:List[Int]):Int = {
    arr.filter(x => x % 2 != 0).sum
}
