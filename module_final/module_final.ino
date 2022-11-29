/**
 * Created by @Author: Mai Manh Huy
 * Project : Safety Smart Home IoT Systems
 * Create Time : 03:22 - 23/11/2022
 * For all issue contact me : huymm98@gmail.com
 * Module sensor for Smart Home IoT 
 */
//Sơ đồ chân cắm
/* DHT11
 * VCC -> 3.3V, 5V
 * GND -> GND
 * DATA -> D4
 */
/* Light Sensor
 * VCC -> 3.3V, 5V
 * GND -> GND
 * D0 -> D10
 */
/* MQ135  
 * VCC -> 3.3V ,5V
 * GND -> GND
 * A0 -> A2
 */
 /* MQ2
 * VCC -> 3.3V ,5V
 * GND -> GND
 * Aout -> A0 
  */
 /* Sound Sensor
  * VCC -> 5V
  * GND -> GND
  * Aout -> A1
  */
 /* Vibration Sensor
  * VCC -> 5V
  * GND -> GND
  * Aout -> A2
  */
 
#include "DHT.h" 
#include "stdlib.h"
#include "arduino.h"     
#include "MQ135.h" 

#define PIN_MQ135 A2
const int DHTPIN = 4;      
const int DHTTYPE = DHT11; 
DHT dht(DHTPIN, DHTTYPE);
int Light_digital = 10;
MQ135 mq135_sensor = MQ135(PIN_MQ135);
int Gas_analog = A0;
int Sound_analog = A1;
int Vibration_analog = A2;
int gas_value; 
float temperature = 25.0;
float humidity = 60.0;
int gas;
int sound;
int vibration;
int i = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode (Gas_analog, INPUT);
  dht.begin();
  pinMode (Light_digital,INPUT);
  pinMode (Vibration_analog, INPUT);
  pinMode (Sound_analog, INPUT); 
}
 
void loop() {
  int h = dht.readHumidity();    
  int t = dht.readTemperature(); 
  int light = digitalRead(Light_digital);
  int sound_value;
  int vibration_value;
//  Serial.println(light_value);
//  Serial.print("Nhiet do: ");
//  Serial.println(t);               
//  Serial.print("Do am: ");
//  Serial.println(h);  
          
  float rzero = mq135_sensor.getRZero();
  float correctedRZero = mq135_sensor.getCorrectedRZero(temperature, humidity);
  float resistance = mq135_sensor.getResistance();
  float ppm = mq135_sensor.getPPM();
  float correctedPPM = mq135_sensor.getCorrectedPPM(temperature, humidity);
  
//  Serial.print("MQ135 RZero: ");
//  Serial.println(rzero);
//  Serial.print("Corrected RZero: ");
//  Serial.println(correctedRZero);
//  Serial.print("Resistance: ");
//  Serial.println(resistance);
//  Serial.print(" PPM: ");
//  Serial.println(ppm);
//  Serial.print("Corrected PPM: ");
//  Serial.print(correctedPPM);  
//  Serial.println("ppm"); 
  gas_value = analogRead(A0);   
  
                                
  int gas_percent = map(gas_value, 0, 1023, 0, 99);      
  
//  Serial.println(gas_percent);
  
//  Serial.println(gas_value); 
//  Serial.println("%");

   sound_value = analogRead(A1) ;
   
//  Serial.println(sound) ;

   vibration_value = analogRead(A2);
   
//  Dig = digitalRead(Dig_vib);
//  Serial.println(vibration);
//  Serial.println(Dig_vib);  

  if(gas_percent > 0 && gas_percent < 50) 
  {
    gas = 0;
//    Serial.println(gas);
//    Serial.println("Gas Safety");
  }
  if(gas_percent > 55 && gas_percent <= 75) 
  {
    gas = 1;
//    Serial.println(gas);
//    Serial.println("Gas Detect");
  }
  if(gas_percent > 65 && gas_percent <= 99) 
  {
    gas = 2;
//    Serial.println(gas);
//    Serial.println("Gas Warning");
  }
//  num = (int)correctedPPM;
 if (1023 >= vibration_value && vibration_value >= 500)
//  {
//   
    vibration = 0;
//    Serial.println(vibration);
//  }
  if (500 > vibration_value && vibration_value >= 0)
//  {
//    vibration = 1;
//      Serial.println(vibration);
//  }
 
  if (0 <= sound_value && sound_value <= 100)
  {
//    Serial.print("No Sound");
    sound = 0;
//    Serial.println(sound);
  }
  if (100 < sound_value )
  {
//    Serial.print("Sound Warning");
    sound = 1;
//    Serial.println(sound);
  }

//  Serial.print("h :");
//  Serial.println(h);
//  Serial.print("t :");
//  Serial.println(t);
//  Serial.print("light :");
//  Serial.println(light);
//  Serial.print("gas :");
//  Serial.println(gas);
//  Serial.print("chat luong :");
//  Serial.println(gas_percent);
//  Serial.print("sound :");
//  Serial.println(sound);
//  Serial.print("vibration :");
//  Serial.println(vibration);
//  Serial.println();
  int send_data[i] ;
  send_data[0] = h;
  send_data[1] = t;
  send_data[2] = light;
  send_data[3] = gas;
  send_data[4] = gas_percent; 
  send_data[5] = sound;
  send_data[6] = vibration;
  for( i=0;i<=6;i++)
  {
    Serial.print(send_data[i]);
  }
  Serial.println();
  delay(500);
}
