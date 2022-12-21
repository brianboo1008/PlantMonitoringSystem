#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Wire.h>

// Insert your network credentials
#define WIFI_SSID "realme GT 2 Pro"
#define WIFI_PASSWORD "ahboo123"

WiFiClient client;

// Initialize WiFi
void initWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
}

void setup() {

  Serial.begin(9600);
  
  initWiFi();
}

void loop() {
  // put your main code here, to run repeatedly:
  HTTPClient http;
  http.begin(client,"http://boospammer999.pythonanywhere.com/data/");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  int httpResponseCode = http.POST("temperature=40, humidity=40, light_intensity=40");
  String payload = http.getString();
  Serial.println(httpResponseCode);
  Serial.println(payload);
  http.end();
}
