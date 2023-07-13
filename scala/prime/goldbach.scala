import Eratos.eratos
object Goldbach {
    def goldbach(n: Int): Int = {
        val seq = eratos(n)
        (2 to n / 2).count(i => seq(i) == false && seq(n - i) == false)
    }
}