#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include "base.h"

typedef enum Palo {
    OROS = 'O',
    COPAS = 'C',
    ESPADAS = 'E',
    BASTOS = 'B'
} Palo;


typedef struct Carta {
    Palo palo;
    int numero;
} Carta ;

Carta* crearCarta(Palo palo, int numero);
void destruirCarta(Carta* carta);
void imprimirCarta(Carta* carta);
const char* cartaStr(Carta* carta);
int valorCarta(Carta* carta);
int cmpCartas(Carta* carta1, Carta* carta2);
Carta **crearBarajaEspanola();
void destruirBarajaEspanola(Carta **baraja);
Carta **mazoRandom(Carta **baraja);

