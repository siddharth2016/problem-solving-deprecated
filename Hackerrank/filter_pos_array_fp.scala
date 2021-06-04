/*

FP Question
Link in Problems.md

Filter Position in Array

*/


def f(arr:List[Int]):List[Int] = {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/
    def aux(arr: List[Int], n: Int, result: List[Int]): List[Int] = {
        if (n > arr.size) result
        else if (n % 2 == 0) aux(arr, n+1, result :+ arr(n-1))
        else aux(arr, n+1, result)
    }
    
    aux(arr, 1, List())

}
