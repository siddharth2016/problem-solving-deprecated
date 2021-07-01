object Solution {
    import scala.io.StdIn.readInt
    import scala.collection.mutable.{Map => mMap}
    
    
    def factorial(x: Int, res: Int=1): Int = {
        if (x==0) res
        else factorial(x-1, res*x)
    }
    
    def printPascalTriangle(num: Int): Unit = {
        val map = mMap[Int, Int]()
        def helper(n: Int, r: Int, res: String): String = {
            if (!map.contains(n)) {
                map += (n -> factorial(n))
            }
            if (!map.contains(r)) {
                map += (r -> factorial(r))
            }
            if (!map.contains((n-r).abs)) {
                map += ((n-r).abs -> factorial((n-r).abs))
            }
            val ans = res + map(n)/(map(r) * map((n-r).abs)) + " "
            if (n==r) ans
            else helper(n, r+1, ans)
        }
        for {
            n <- 0 until num
        } println(helper(n, 0, ""))
        
    }
    
    
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/      val n = readInt()
        printPascalTriangle(n)
    }
}
