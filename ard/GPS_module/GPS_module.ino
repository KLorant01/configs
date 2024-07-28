//#include "GPS.h"

static char* Data_Stream = "";      // < The char that contain the processed data, trugh the code  

void setup(){
  Serial.begin(9600),
  Serial.println("setup");
}

void loop() {
  Serial.println("Main");
  delay(800);
}

int Main_Data_Store(const char*) {

  return 0;
}
