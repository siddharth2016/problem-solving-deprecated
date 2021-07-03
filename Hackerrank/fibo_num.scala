object Solution {
    
     def fibonacci(x:Int):Int = {
          
		// Fill Up this function body
        // You can add another function as well, if required
        
        def helper(n: Int, a: Int=0, b: Int=1): Int = {
            if (n == x) a
            else helper(n+1, b, a+b)
        }
        
        helper(1)
     }

    def main(args: Array[String]) {
         /** This will handle the input and output**/
         import scala.io.StdIn.readInt
         println(fibonacci(readInt()))

    }
}
