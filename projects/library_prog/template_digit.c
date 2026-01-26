::c
::header
#define DIGIT
#define LETTER
#undef DIGIT

unsigned char a = 0, b = 0, c = 0;
#define PORTD a
#define DDRD b
#include <stdio.h>
#define TEST 1
#define while(a) if (a == 1) for(int iter = 0; iter < TEST; iter++)

#define A	0
#define B	1
#define C	2
#define D	3
#define E	4
#define F	5
#define G	6
#define DP  7

#define ZEROSA  (1<<A)|(1<<B)|(1<<C)|(1<<D)|(1<<E)|(1<<F)|(0<<G)
#define ONESA   (0<<A)|(1<<B)|(1<<C)|(0<<D)|(0<<E)|(0<<F)|(0<<G)
#define TWOS    (1<<A)|(1<<B)|(0<<C)|(1<<D)|(1<<E)|(0<<F)|(1<<G)
#define THRE    (1<<A)|(1<<B)|(1<<C)|(1<<D)|(0<<E)|(0<<F)|(1<<G)
#define FOU     (0<<A)|(1<<B)|(1<<C)|(0<<D)|(0<<E)|(1<<F)|(1<<G)
#define FIVE    (1<<A)|(0<<B)|(1<<C)|(1<<D)|(0<<E)|(1<<F)|(1<<G)
#define SIX     (1<<A)|(0<<B)|(1<<C)|(1<<D)|(1<<E)|(1<<F)|(1<<G)
#define SEVEN   (1<<A)|(1<<B)|(1<<C)|(0<<D)|(0<<E)|(0<<F)|(0<<G)
#define EIGTH   (1<<A)|(1<<B)|(1<<C)|(1<<D)|(1<<E)|(1<<F)|(1<<G)
#define NINE    (1<<A)|(1<<B)|(1<<C)|(1<<D)|(0<<E)|(1<<F)|(1<<G)


unsigned char letter(char let) {
	switch (let) {
		case 'a': return (1<<E)|(1<<F)|(1<<A)|(1<<B)|(1<<C)|(1<<G);
		case 'b': return (1<<F)|(1<<E)|(1<<D)|(1<<C)|(1<<G);
		case 'c': return (1<< A)|(1<< F)|(1<<E)|(1<<D);
		case 'd': return (1<<E)|(1<<B)|(1<<C)|(1<<D)|(1<<G);
		case 'e': return (1<<A)|(1<<F)|(1<<G)|(1<<E)|(1<<D);
		case 'f': return (1<<A)|(1<<F)|(1<<G)|(1<<E);
		case 'g': return (1<<A)|(1<<B)|(1<<C)|(1<<D)|(1<<F)|(1<<G);
		case 'h': return (1<<F)|(1<<E)|(1<<G)|(1<<C);
		case 'i': return (1<<B)|(1<<C);
		case 'k': return (1<<A)|(1<<F)|(1<<G)|(1<<E)|(1<<C);
		case 'l': return (1<<F)|(1<<E)|(1<<D);
		case 'n': return (1<<E)|(1<<G)|(1<<C);
		case 'o': return (1<<E)|(1<<D)|(1<<C)|(1<<G);
		case 'p': return (1<<A)|(1<<B)|(1<<E)|(1<<F)|(1<<G);
		case 'r': return (1<<E)|(1<<G);
		case 's': return (1<<A)|(1<<F)|(1<<G)|(1<<C)|(1<<D);
		case 't': return (1<<F)|(1<<G)|(1<<E)|(1<<D);
		case 'u': return (1<<E)|(1<<D)|(1<<C);
		case 'x': return (1<<F)|(1<<G)|(1<<B)|(1<<E)|(1<<C);
		case 'y': return (1<<F)|(1<<G)|(1<<B)|(1<<C)|(1<<D);
		case '\0': return 0x00;
		default: return (1<<D);
	}
}

unsigned char item = 0, mask = ~(1 << DP);
unsigned char digit_data[10] = {ZEROSA, ONESA, TWOS, THRE,
                  FOU, FIVE, SIX, SEVEN, EIGTH, NINE};

unsigned char digit_to_bit(unsigned char num) {
    if (num >= 0 && num < 10)
        return digit_data[num];
    return 0;
}

unsigned char bit_to_digit(unsigned char port) {
    for (int i = 0; i < 10; ++i) {
        if ((port&mask) == digit_to_bit(i))
            return i;
    }
    return 8;
}

unsigned char bit_to_letter(char port) {
    for (int i = 'a'; i < 'z'; i++) {
        if ((port&mask) == letter(i))
            return i;
    }
}

void _delay_ms(int msec) {
#ifdef DIGIT
    if (item++ < 10) {
        printf("Индикатор: %d", bit_to_digit(PORTD&DDRD));
        printf((PORTD&(1 << DP)) ? "." : " ");
        printf(" | Задержка в %d c\n", msec / 1000);
    }
#endif
#ifdef LETTER
    if (item++ < 'z') {
        printf("Индикатор: %c", bit_to_letter(PORTD&DDRD));
        printf((PORTD&(1 << DP)) ? "." : " ");
        printf(" | Задержка в %d c\n", msec / 1000);
    }
#endif
}

int main(void)
{
    // scanf("%d", &c);
    // PORTD = digit_to_bit(c);
::code
    /* #include <avr/io.h>
       #define F_CPU 8000000
       #include <avr/delay.h> */

    int main(void)
    {
        while (1)
        {
            // Напишите Ваш код здесь
        }
    }

::footer
    main();
}
