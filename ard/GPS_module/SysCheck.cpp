/*
#include <Arduino.h>
#include "SysCheck.h"

#define SYSCHECK_BAUD 9600     // < Termianl Baud
static long Mode = 0;

typedef enum {
  OFF = 0,
  ON = 1,
  DEFAULT = 2
} syscheck_state;

typdef enum {
  ALWAYS_OFF = 0,
  ALWAYS_ON = 1,
  ALWAYS_DEFAULT = 2
} syscheck_mode;

void SysCheck_Init(systemcheck_mode MODE, syscheck_state STATE) {
  swich(MODE){
    case ALWAYS_OFF: {
      Mode = ALWAYS_OFF;
    }
    case ALWAYS_ON: {
      Serial.beguin(SYSCHECK_BAUD);
      Serial.println("==> System Check active <==");
      Serial.println(> Mode: ALWAYS_ON);
      Mode = ALWAYS_ON;
    }
    case ALWAYS_DEFAULT: {
      Serial.beguin(SYSCHECK_BAUD);

      swich(STATE) {
        case OFF: {

        }
        case ON: {

        }
        case DEFAULT: {

        }
        default: {
          
        }
      }
    }
    default: {
      Serial.beguin(SYSCHECK_BAUD);
    }
  }
}

void SysCheck_prt(syscheck_state STATE ,const char* DATA) {
  swich(mode){

  }
}

#undef state
#undef mode
*/