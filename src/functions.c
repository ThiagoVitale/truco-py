#include <stdio.h>
#include <string.h>

// Definimos la estructura para el diccionario
typedef struct {
    char carta[20];
    char valor[20];
} Carta;

// Función para inicializar el diccionario
void inicializarDiccionario(Carta diccionario[], int tam) {
    // Todas las cartas del truco argentino
    char *cartas[] = {
        "1 de Espadas", "1 de Bastos", "7 de Espadas", "7 de Oro", "3 de Espadas",
        "3 de Bastos", "3 de Oro", "3 de Copas", "2 de Espadas", "2 de Bastos",
        "2 de Oro", "2 de Copas", "1 de Oro", "1 de Copas", "12 de Espadas",
        "12 de Bastos", "12 de Oro", "12 de Copas", "11 de Espadas", "11 de Bastos",
        "11 de Oro", "11 de Copas", "10 de Espadas", "10 de Bastos", "10 de Oro",
        "10 de Copas", "7 de Bastos", "7 de Copas", "6 de Espadas", "6 de Bastos",
        "6 de Oro", "6 de Copas", "5 de Espadas", "5 de Bastos", "5 de Oro",
        "5 de Copas", "4 de Espadas", "4 de Bastos", "4 de Oro", "4 de Copas"
    };

    for(int i = 0; i < tam; i++) {
        strcpy(diccionario[i].carta, cartas[i]);
        strcpy(diccionario[i].valor, ""); // Inicializamos el valor como vacío
    }
}

int main() {
    const int tam = 40;
    Carta diccionario[tam];

    inicializarDiccionario(diccionario, tam);

    // Imprimimos el diccionario
    for(int i = 0; i < tam; i++) {
        printf("Carta: %s, Valor: %s\n", diccionario[i].carta, diccionario[i].valor);
    }

    return 0;
}

