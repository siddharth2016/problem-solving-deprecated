/*

FP Question
Link in Problems.md

Evaluating e^x

*/

import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {


    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val n = stdin.readLine.trim.toInt

        for (nItr <- 1 to n) {
            val x = stdin.readLine.trim.toDouble
            println(geteX(x))
        }
        
        def geteX(x: Double): Double = {
            val limit = 10
            def wrapper(n: Int, term: Double, res: Double): Double = {
                if (n==limit) res
                else wrapper(n+1, term*x/(n+1), res + term)
            }
            
            wrapper(1, x, 1.0)
        }
        
    }
}
