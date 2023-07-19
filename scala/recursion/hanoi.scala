import java.io.{BufferedWriter, OutputStreamWriter}
object Main {
    def main(args: Array[String]): Unit = {
        val n = scala.io.StdIn.readInt
        printHanoi(n)
    }

    def hanoi(n: Int): Int = {
        def loop(i: Int, acc: Int): Int = {
            if(i == 0) acc
            else loop(i - 1, acc * 2 + 1)
        }
        loop(n , 0)
    }

    def hanoiProcess(n: Int): Unit = {
        val writer = new BufferedWriter(new OutputStreamWriter(System.out))
        def loop(i: Int, start: Int, end: Int, aux: Int): Int = {
            if(i == 0) 0
            else {
                loop(i - 1, start, aux, end)
                writer.write(s"$start $end\n")
                loop(i - 1, aux, end, start)
            }
        }
        loop(n, 1, 3, 2)
        writer.flush()
        writer.close()
    }

    def printHanoi(n: Int): Unit = {
        print(s"${hanoi(n)}\n")
        hanoiProcess(n)
    }
}