import java.io.{BufferedWriter, OutputStreamWriter}
object PrintStars {
    def printStars(stars: List[String]): Unit = {
        val writer = new BufferedWriter(new OutputStreamWriter(System.out))
        stars.foreach(i => print(s"${i}\n"))
        writer.flush()
        writer.close()
    }
}