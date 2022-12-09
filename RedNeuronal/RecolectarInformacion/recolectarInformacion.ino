const int s0 = 4;
const int s1 = 5;
const int s2 = 6;
const int s3 = 7;
const int out = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(out, INPUT);

  digitalWrite(s0, HIGH);
  digitalWrite(s1, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  int R = getRojo();
  delay(200);
  int V = getVerde();
  delay(200);
  int A = getAzul();
  delay(200);

  Serial.print("Int R " + String(R));
  Serial.print(" -- Int V " + String(V));
  Serial.println(" -- Int A " + String(A));
}

int getRojo(){
  //Leer coclor rojo
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  int ROJO = pulseIn(out, LOW);
  return ROJO;
}

int getAzul(){
  //Leer coclor azul
  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);
  int AZUL = pulseIn(out, LOW);
  return AZUL;
}

int getVerde(){
  //Leer coclor verde
  digitalWrite(s2, HIGH);
  digitalWrite(s3, HIGH);
  int VERDE = pulseIn(out, LOW);
  return VERDE;
}
