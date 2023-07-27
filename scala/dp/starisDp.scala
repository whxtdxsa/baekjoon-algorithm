import java.io.{BufferedReader, InputStreamReader}
object Main {
    def main(args: Array[String]): Unit = {
        /* Get Input */
        val reader = new BufferedReader(new InputStreamReader(System.in))
        val n = reader.readLine.toInt
        val list = (0 until n).map(i => reader.readLine.toInt).toList

        /* Func */
        val res = stairs(n, list)
        println(res)
    }

    def stairs(n: Int, l: List[Int]) = {
        if(n == 1) l(0)
        else if(n == 2) l(0) + l(1)
        else dp(n, l)
    }

    def dp(n: Int, l: List[Int]) = {
        val dpArr = new Array[Int](n)
        dpArr(0) = l(0)
        dpArr(1) = l(0) + l(1)
        dpArr(2) = Math.max(l(0), l(1)) + l(2)
        (3 until n).foreach(i => 
            dpArr(i) = Math.max(dpArr(i - 3) + l(i - 1), dpArr(i - 2)) + l(i)
        )
        dpArr(n - 1)
    }
}