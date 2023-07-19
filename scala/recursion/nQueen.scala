object nQueen {
    def main(args: Array[String]): Unit = {
        val n = scala.io.StdIn.readInt()
        val res = nQueen(n);
        println(res)
    }

    def nQueen(n: Int): Int = {
        var cnt = 0;
        val arr = new Array[Int](n)

        def loop(depth: Int): Unit = {
            if(depth == n) cnt += 1
            else {
                for (j <- 0 until n) {
                    def canAttack(j: Int): Boolean = {
                        (0 until depth).exists({y =>
                            val x = arr(y)
                            val diffX = x - j
                            val diffY = y - depth
                            diffY == diffX || diffY == -diffX || diffX == 0
                        })
                    }
                    if(!canAttack(j)) {
                        arr(depth) = j
                        loop(depth + 1)
                    }
                }
            }
        }
        loop(0)
        cnt
    }
}