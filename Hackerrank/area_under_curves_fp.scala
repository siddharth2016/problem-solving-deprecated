/*

FP Question
Link in Problems.md

Area Under Curves and Volume

*/

import scala.io.StdIn.{readLine, readInt}
import math.pow
import math.Pi

def f(coefficients:List[Int],powers:List[Int],x:Double):Double = 
    (coefficients zip powers).map(t => t._1 * pow(x, t._2)).sum

def area(coefficients:List[Int],powers:List[Int],x:Double):Double = 
    Pi*pow(f(coefficients, powers, x), 2)

def summation(func:(List[Int],List[Int],Double)=>Double,upperLimit:Int,lowerLimit:Int,coefficients:List[Int],powers:List[Int]):Double ={
    (0 to ((upperLimit-lowerLimit)/0.001).toInt).map(x => func(coefficients, powers, lowerLimit+0.001*x)*0.001).sum
}
