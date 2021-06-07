/*

FP Question
Link in Problems.md

Compute the Perimeter of a Polygon

*/

object Solution {
    import scala.io.StdIn.{readInt, readLine}
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/      val n = readInt()
        val arX = collection.mutable.ArrayBuffer[Int]();
        val arY = collection.mutable.ArrayBuffer[Int]();
        for(i <- 1 to n) {
            val xy = readLine().split(" ").map(_.toInt)
            arX += xy(0)
            arY += xy(1)
        }
        
        def computePerimeter(X: collection.mutable.ArrayBuffer[Int], Y: collection.mutable.ArrayBuffer[Int], i: Int, acc: Double): Double = {
            if (i==n) acc
            else computePerimeter(X, Y, i+1, acc + {
                scala.math.sqrt(scala.math.pow((X(i) - X((i+1)%n)), 2) + scala.math.pow((Y(i) - Y((i+1)%n)).abs, 2))
            })
        }
        println(computePerimeter(arX, arY, 0, 0.0))
    }
}
