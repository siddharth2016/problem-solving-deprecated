/*

FP Question
Link in Problems.md

Functions or Not

*/

object Solution {
    import scala.io.StdIn.{readLine, readInt}
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution
*/      
        val T = readInt();
        for (i<-0 until T){
            val N = readInt();
            val X = collection.mutable.Set[Int]();
            val XY = collection.mutable.Set[Array[Int]]();
            var flag = 1
            for (j<-0 until N){
                val d = readLine().split(" ").map(_.toInt);
                if(X contains d(0)){
                    if(!(XY contains(d))){
                        flag = 0;
                    }
                }
                X+=d(0)
                XY+=d
            }
            if(flag==1){
                println("YES");
            }
            else{
                println("NO")
            }
         }
    }
}
