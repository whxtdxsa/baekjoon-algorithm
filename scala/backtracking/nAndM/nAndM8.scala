import java.io.{BufferedWriter, OutputStreamWriter}
object nAndM8 {
    def dfs(n: Int, m: Int, list: List[Int]) = {
        val visited = new Array[Boolean](n)
        val writer = new BufferedWriter(new OutputStreamWriter(System.out))
        val sortedList = list.sorted
        def loop(depth: Int, l: List[Int]): Unit = {
            if(depth == m) {
                l.reverse.foreach(i => writer.write(s"$i "))
                writer.write("\n")
            }
            else (0 until n).foreach {i =>
                    if(!visited(i)) {
                        val tag = visited.indexOf(false)
                        (tag until i).foreach(j => visited(j) = true)
                        loop(depth + 1, sortedList(i) :: l)
                        (tag until i).foreach(j => visited(j) = false)
                    }
                }
        }
        loop(0, List())
        writer.flush()
        writer.close()
    }
}