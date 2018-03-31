int trigPin = 9; // trigger pin in the US sensor
int echoPin = 10; // data pin in the US sensor

#define NR 10 // number of repetition of readings under each test condition
long duration; // microseconds
float soundSpeed = 0.034; // cm/us
int T[11]={1,20,40,60,80,100,120,140,160,180,200}; // time interval between consecutive readings, milliseconds
float distance[NR]; // array with the readings of the repeated measurements, cm
float sum = 0;

void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}

void loop() {
    for (int i=0; i<11; i++) // for each T interval
    {
      for (int j=0; j<NR; j++) // for each of the NR repetitions
      {
      duration = durCalc(trigPin, echoPin); // measures the sound travelling distance (microseconds)
      distance[j] = duration*soundSpeed/2.; // converts the time into a distance (cm)
      delay(T[i]); // wait as required between consecutive readings
      }
      
      for (int j=0; j<NR; j++)
      {  
        sum = sum + distance[j];
      } 
      sum = sum/10;
      Serial.print(sum);
      Serial.print("\n");
      sum = 0;
    }
}

float durCalc(int pinI, int pinO)
{
  // The PING is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(pinI, LOW);
  delayMicroseconds(2);
  digitalWrite(pinI, HIGH);
  delayMicroseconds(12);
  digitalWrite(pinI, LOW);
  //delay(10);
  return(pulseIn(pinO, HIGH)); 
}



 

 

 



