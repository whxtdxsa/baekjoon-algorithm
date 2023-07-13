object Eratos {
    def eratos(n: Int): Array[Boolean] = {
        // Initialize array 
        val info = new Array[Boolean](n+1)
        info(0) = true
        info(1) = true

        // Eratos's method
        def loop(i: Int): Array[Boolean] = {
            if(i * i > n) info
            else if(info(i) == true) loop(i + 1)
            else {
                def subLoop(j: Int): Int = {
                    if(j > n) 0
                    else {
                        info(j) = true
                        subLoop(j + i)
                    }
                }
                subLoop(i * i)
                loop(i + 1)
            }
        }
        loop(2)
    }
}