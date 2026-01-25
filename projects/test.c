int main(void) {
    DDRD = 0xFF;
    while(1) {
        PORTD ^= 0xFF;
        _delay_ms(1000);
    }
}