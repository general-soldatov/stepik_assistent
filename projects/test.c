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