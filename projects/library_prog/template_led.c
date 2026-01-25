::c
::header
#define TEST 10

#include <stdio.h>

char reg[2] = {0}, port[2] = {0};
int tst = 0;

#define DDRD reg[0]
#define DDRB reg[1]
#define PORTD port[0]
#define PORTB port[1]

void delay_ms(int ms) {
    printf("Панель: | ");
    for (int i = 0; i < 8; i++) {
        printf(DDRD&PORTD&(1 << i) ? "🟩" : "⬛");
    }
    printf(" | Задержка в %d мc\n", ms);
    tst++;
}

#define _delay_ms(a) do { if (tst >= TEST) return 0; delay_ms(a);} while (0)

::code
int main(void) {

    while(1) {

    }
}

::footer