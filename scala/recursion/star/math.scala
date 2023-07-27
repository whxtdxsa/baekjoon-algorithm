object Math {
    def exp(x: Int, y: Int): Int = {
        def loop(i: Int, acc: Int): Int = {
            if(i == 0) acc
            else loop(i - 1, acc * x)
        }
        loop(y, 1)
    }
}