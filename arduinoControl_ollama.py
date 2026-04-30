import serial
import time
import ollama

ser = serial.Serial('COM1', 9600, timeout=1)
time.sleep(2)

def ask_llm(sensor_value):
    prompt = f"Sensor reading is {sensor_value}. If it's above 500, return 'LED_ON'. If below, return 'LED_OFF'. Answer with only one word."
    try:
        response = ollama.chat(model='llama3', messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content'].strip()
    except Exception:
        return "LED_OFF"

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if "SENSOR_DATA:" in line:
                value = line.split(":")[1]
                command = ask_llm(value)
                ser.write((command + "\n").encode())
        time.sleep(0.5)
except KeyboardInterrupt:
    ser.close()
