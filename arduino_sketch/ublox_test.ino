#include <AltSoftSerial.h>
AltSoftSerial altserial;
#define led 6
void setup() {
  pinMode( led, OUTPUT );
  Serial.begin(9600);
  altserial.begin( 9600 );

  //blink 1 time - indicates that setup is complete
  digitalWrite(led, HIGH);
  delay( 500 );
  digitalWrite(led, LOW);
  delay( 250 );
  while( !Serial ) { delay(100); } //wait until usb serial is connected
  //while( !altserial ) { delay(100); }
  digitalWrite(led, HIGH); // once the PC serial is established ON the LED
  Serial.println( "AltSoftTest begins" );

}

void loop() {
    // When you receive the data from PC send it to HC12
    //while( Serial.available() )
    //{
    //  altserial.write( Serial.read() );
    //}

    // When you receive the data from serial device send it to the PC
    while( altserial.available() )
    {
      Serial.write( altserial.read() );
    }
}
