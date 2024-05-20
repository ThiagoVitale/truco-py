#include "carta.h"

extern const Carta barajaEspanola[40];

Carta *crearCarta(Palo palo, int numero)
{
    Carta *carta = (Carta *)malloc(sizeof(Carta));
    carta->palo = palo;
    carta->numero = numero;
    return carta;
}

void destruirCarta(Carta *carta)
{
    free(carta);
}

void imprimirCarta(Carta *carta)
{
    printf("%s\n", cartaStr(carta));
}

const char *cartaStr(Carta *carta)
{
    static char str[16];
    switch(carta->palo) {
        case OROS:
            sprintf(str, "%d de Oro", carta->numero);
            break;
        case COPAS:
            sprintf(str, "%d de Copa", carta->numero);
            break;
        case ESPADAS:
            sprintf(str, "%d de Espada", carta->numero);
            break;
        case BASTOS:
            sprintf(str, "%d de Basto", carta->numero);
            break;
    }
    return str;
}

int valorCarta(Carta *carta)
{
    return carta->numero;
}

int cmpCartas(Carta *carta1, Carta *carta2)
{
    // TODO: Implementar comparación de cartas con reglas el truco
    return 0;
}

Carta **crearBarajaEspanola()
{
    Carta **baraja = (Carta **)malloc(40 * sizeof(Carta*));
    for (int i = 0; i < 10; i++)
    {
        baraja[i] = crearCarta(OROS, i + 1);
        baraja[i + 10] = crearCarta(COPAS, i + 1);
        baraja[i + 20] = crearCarta(ESPADAS, i + 1);
        baraja[i + 30] = crearCarta(BASTOS, i + 1);
    }
    return baraja;
}

void destruirBarajaEspanola(Carta **baraja)
{
    for (int i = 0; i < 40; i++)
    {
        destruirCarta(baraja[i]);
    }
    free(baraja);
}

Carta **mazoRandom(Carta **baraja)
{
    Carta** mazoRandom = (Carta **)malloc(40 * sizeof(Carta*));
    shuffle_copy((void**)baraja, 40, (void**) mazoRandom);
    return mazoRandom;
}

// Path: c/lib/mazo.c