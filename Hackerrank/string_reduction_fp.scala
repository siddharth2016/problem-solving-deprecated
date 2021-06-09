/*

String Reduction

*/

object Solution {
    import scala.io.StdIn.{readLine}
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/      val s = readLine().trim()
        val m = scala.collection.mutable.Map[Char, Int]()
        var r = ""
        
        s.foreach { c =>
            if(!m.contains(c)) {
                m += (c -> 1)
                r += c
            }
        }
        
        println(r)
        
    }
}
