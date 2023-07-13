import Eratos.eratos
object Chebyshev {
    def chebyshev(n: Int): Int = {
        // Chebyshev's Thm
        val seq = eratos(2 * n)
        (n + 1 to 2 * n).count(i => seq(i) == false)
    }
}