object Solution {
    import scala.io.StdIn.readLine
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/      val p = readLine().trim()
        val q = readLine().trim()
        val zipped = p zip q
        for {
            a <- zipped
        } print(s"${a._1}${a._2}")
    }
}
