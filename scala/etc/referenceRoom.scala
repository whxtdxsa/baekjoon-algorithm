import java.io.{BufferedReader, InputStreamReader}
object Main {
  val reader = new BufferedReader(new InputStreamReader(System.in))
  def main(args: Array[String]) : Unit = {
    val n = reader.readLine.toInt
    val res0 = getRefTimes(n)
    val res1 = RefRoom.countCanRefTimes(res0)
    println(res1)

    reader.close()
  }

  def getRefTimes(n: Int) = {
    def loop(i: Int, l: List[Array[Int]]): List[Array[Int]] = {
      if(i == 0) l
      else {
        val input = reader.readLine.split(" ").map(_.toInt)
        loop(i - 1, input :: l)
      }
    }
    loop(n, List())
  }
}

object RefRoom {
  def sortRefTimes(l: List[Array[Int]]) =
    l.sortBy(_(1))

  def countCanRefTimes(list: List[Array[Int]]) = {
    val l = sortRefTimes(list)
    val size = l.length
    def loop(i: Int, prevEnd: Int, acc: Int): Int = {
      if(i == size) acc
      else if(prevEnd <= l(i)(0)) loop(i + 1, l(i)(1), acc + 1)
      else loop(i + 1, prevEnd, acc)
    }
    loop(0, 0, 0)
  }
}
