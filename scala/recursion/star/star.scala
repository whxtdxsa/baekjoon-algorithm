object Star {
    def star11(n: Int): List[String] = {
        if(n == 3) List("  *  ", " * * ", "*****")
        else {
            val prev = star11(n / 2)
            val tmpBlank = " " * (n / 2)
            val top = prev.map(line =>  tmpBlank + line + tmpBlank)
            val bottom = prev.map(line => line + " " + line)
            top ++ bottom
        }
    }

    def star18(n: Int): List[String] = {
        def loop(i: Int, acc: List[String]): List[String] = {
            if(i == n) acc
            else {
                val k = acc(0).size
                loop(i + 1, acc.map(j => j + " " * (k - j.size) + j) ++ acc.map(j => j))
            }
        }
        loop(0, List("*"))
    }

    def star19(n: Int): List[String] = {
        if(n == 1) List("*")
        else {
            val arr = star19(n - 1)
            val size = 4 * n - 3
            val topAndBottom = List("*" * size)
            val sides = List("*" + " " * (size -2) + "*")
            val middle = arr.map(line => s"* $line *")
            topAndBottom ++ sides ++ middle ++ sides ++ topAndBottom
        }
    }

    def star22(n: Int): List[String] = {
        if(n == 1) List("*")
        else star22Tail(n)
    }

    def star22Tail(n: Int): List[String] = {
        if(n == 1) List("*", "*", "*")
        else {
            val size = 4 * n - 3
            val topAndBottom = List("*" * size)
            val topSide = List( "*")
            val bottomSide = List( "*" + " " * (size - 2) + "*")
            val prev = star22Tail(n - 1)

            val middle = prev match {
                case x1::(x2::xs) => List("* " + x1 + "**") ++ 
                List("* " + x2 + " " * (4 * n - 8) + " *") ++ 
                xs.map{i => "* " + i + " *"}
                case _ => List()
            }
            topAndBottom ++ topSide ++ middle ++ bottomSide ++ topAndBottom
        }
    }
}