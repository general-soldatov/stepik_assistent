::c
::header
#define TEST 1

#include <stdio.h>
unsigned char portd, ddrd, ddrb, portb, pinb;
#define PORTD portd
#define DDRD ddrd
#define PORTB portb
#define DDRB ddrb
#define PINB pinb
#define TST_MASS 9
#define while(a) if (a == 1) for(int iter = 0; iter < TEST; iter++)

void _delay_ms(int msec) {
    if (!(~(DDRB&(0 << 0))&(PORTB&(1 << 0))) || (DDRD != 0xFF)) {
        printf("Ошибка! Не правильно настроены регистры!\n");
        return;
    }
    printf("Кнопка | %s |\n", (PINB&(1 << 0) ? "off" : "on"));
    printf("Панель: ");
    for (int i = 0; i < 8; i++)
        printf(DDRD&PORTD&(1 << i) ? "🟩" : "⬛");
    printf(" | Задержка %d ms\n", msec);
}


int main(void)
{
::code
/* #include <avr/io.h>
   #define F_CPU 8000000UL
   #include <avr/delay.h> */
#define BUTTON 0

int main(void)
{
    while(1)
    {

    }
}
::footer
    unsigned char button[2] = {0, 1};
    for (int i = 0; i < 2; i++) {
        PINB = button[i];
        main();
    }
}
