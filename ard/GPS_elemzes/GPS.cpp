#include <Arduino.h>

#define GPS_DATA_ELEMENTS 4

static String GPS_Rec[4];
static String GPS_Data[GPS_DATA_ELEMENTS];

void GPS_Init(void) {
  for (int i =0; i < 4; )
  
}

void GPS_Run(void) {
  while (gps.available() <= 0) {
    ;
  }
  if (gps.available() > 0) {
    static String GPS_Raw = Serial1.read()
  }

    GPS_Rec[0] = "$GPGGA,002153.000,3342.6618,N,11751.3858,W,1,10,1.2,27.0,M,-34.2,M,,0000*5E";
    GPS_Rec[1] = "$GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41";
    GPS_Rec[2] = "$GPGSA,A,3,07,02,26,27,09,04,15, , , , , ,1.8,1.0,1.5*33";
    GPS_Rec[3] = "$GPGSV,2,1,07,07,79,048,42,02,51,062,43,26,36,256,42,27,27,138,42*71";
}

String* GPS_Get_Data(void) {
  
}    



#undef GPS_DATA_MAX_LENGHT
