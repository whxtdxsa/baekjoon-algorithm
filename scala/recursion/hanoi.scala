import java.io.{BufferedWriter, OutputStreamWriter}

object Hanoi {

    def hanoi(n: Int): Int = {
        def loop(i: Int, acc: Int): Int = {
            if(i == 0) acc
            else loop(i - 1, 2 * acc + 1)
        }
        loop(n, 0)
    }
    
    def hanoiLog(n: Int): List[String] = {
        def loop(i: Int, from: Int, to: Int, aux: Int): List[String] ={
            if(i == 1) List(s"$from $to")
            else loop(i - 1, from, aux, to) ++ List(s"$from $to") ++ loop(i - 1, aux, to, from)
        }
        loop(n, 1, 3, 2)
    }

    def printResult(n: Int, l: List[String]): Unit = {
        val writer = new BufferedWriter(new OutputStreamWriter(System.out))
        writer.write(s"$n\n")
        l.foreach(i => writer.write(s"$i\n"))
        writer.flush()
        writer.close()
    }
}