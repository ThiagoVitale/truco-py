#include"../lib/carta.h"
#include"../lib/base.h"

extern const Carta barajaEspanola[40];

int main(int argc, char const *argv[])
{
    Carta **baraja = crearBarajaEspanola();
    Carta *mazo[40];
    shuffle_copy((void**)baraja, 40, (void**)mazo);
    for (int i = 0; i < 40; i++)
    {
        imprimirCarta(mazo[i]);
    }
    destruirBarajaEspanola(baraja);
    return 0;
}