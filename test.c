//c
//header
#include <stdio.h>
#include <stdbool.h>
#define TEST 9
#define CONDITION (!(time_now < 21 && time_now >= 7) || illumination < 6000) == lumen_on

int main(void){
    int data[TEST][2] = {{6000, 11}, {5000, 12}, {6000, 21}, {10000, 11}, {6000, 7}, {5999, 7}, {2000, 20}, {7000, 6}, {8000, 22}};
    for (short i = 0; i < TEST; i++) {
        int illumination = data[i][0], time_now = data[i][1];
bool lumen_on = (time_now < 21 && time_now >= 7) || illumination < 6000;
        printf("Тест %d: ", i + 1);
        printf((CONDITION) ? "Успешно ✅\n" : "Ошибка ❌\n");
    }
}