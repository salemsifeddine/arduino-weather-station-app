int light;
int ledd=2;
String InBytes;
int x;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledd,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 int L = analogRead(A0);
 int W = analogRead(A1);
 int H = analogRead(A2);
 
  
  if(Serial.available() > 0){
    
    InBytes=Serial.readString();
   

    
    
    if(InBytes.indexOf("on") == 0 ){
      digitalWrite(ledd, HIGH);
      
      
    }
    if(InBytes.indexOf("off") == 0 ){
      digitalWrite(ledd, LOW);
     
    }
    
  }

  Serial.print("humidity:");
  Serial.print(H);
  Serial.print(",");
  Serial.print("water:");
  Serial.print(W);
  Serial.print(",");
  Serial.print("light:");
  Serial.println(L );
  
  
  delay(1000);

}
