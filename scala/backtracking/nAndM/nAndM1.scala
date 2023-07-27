import java.io.{BufferedWriter, OutputStreamWriter}
object nAndM1 {
    def dfs(n: Int, m: Int) = {
        val visited = new Array[Boolean](n)
        val writer = new BufferedWriter(new OutputStreamWriter(System.out))

        def loop(depth: Int, l: List[Int]): Unit = {
            if(depth == m) {
                l.reverse.foreach(i => writer.write(s"${i + 1} ")) 
                writer.write("\n")
            }
            else (0 until n).foreach { i =>
                    if(!visited(i)) {
                        visited(i) = true
                        loop(depth + 1, i :: l)
                        visited(i) = false
                    }
                }
        }
        loop(0, List())
        writer.flush()
        writer.close()
    }
}