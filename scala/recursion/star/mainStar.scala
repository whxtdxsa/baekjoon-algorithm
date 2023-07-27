import PrintStars.printStars
import Math.exp
object Main {
    def main(args: Array[String]): Unit = {
        val n = scala.io.StdIn.readInt()

        val res11 = Star.star11(3 * exp(2, n))
        val res18 = Star.star18(n)
        val res19 = Star.star19(n + 1)
        val res22 = Star.star22(n + 1)
        printStars(res22)
    }
}