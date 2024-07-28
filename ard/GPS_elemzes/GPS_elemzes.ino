/* === INCLUDES === */ 
#include "GPS.h"
//#include "PcData.h"

UART gps(4, 5, NC, NC);

#define MAX_DATA_SIZE 10
String Main_Data[MAX_DATA_SIZE];
String GPS_Data[4];

static long i;
  String* p;

void setup()
{

}

void loop()
{
  delay(1500);

  p = GPS_Run();

  Serial.println(*p);
  for (int i =0; i < 3; i++) {
    p+=1;
    Serial.println(*p);
  }

  for (int i =0; i < MAX_DATA_SIZE; i++) {
    Serial.println(Main_Data[i]);
  }
}

#undef MAX_DATA_SIZE

