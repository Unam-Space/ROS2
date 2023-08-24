void setup()
{
    // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop()
{
    if (Serial.available())
    {
        String String_recived = Serial.readString();
        int b = String_recived.toInt();
        Serial.println(b);
    }
}
