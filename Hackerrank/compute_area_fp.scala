/*

Compute the Area of a Polygon

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
            if (i==n) acc.abs/2.0
            else computePerimeter(X, Y, i+1, acc + {
                X(i)*Y((i+1)%n) - Y(i)*X((i+1)%n)
            })
        }
        println(computePerimeter(arX, arY, 0, 0.0))
    }
}
