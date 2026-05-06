// c
// header
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
/* #include <avr/io.h>
   #define F_CPU 8000000UL
   #include <avr/delay.h> */
#define BUTTON 0

int main(void)
{
    DDRD = 0xFF;
    DDRB = (0 << BUTTON);
    PORTB = (1 << BUTTON);
    while(1)
    {
        if (!(PINB&(1 << BUTTON)))
          PORTD = 0xFF;
        else
          PORTD = 0x00;
        _delay_ms(500);
    }
}
    unsigned char button[2] = {0, 1};
    for (int i = 0; i < 2; i++) {
        PINB = button[i];
        main();
    }
}
