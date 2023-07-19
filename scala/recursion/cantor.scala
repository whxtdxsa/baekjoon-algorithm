object Cantor {
    def findLine(n: Int): String = {
        def loop(i: Int, s: String): String = {
            if(i == 0) s
            else loop(i - 1, s + " " * s.length() + s)
        }
        loop(n, "-")
    }
}