from decouple import config
import requests
# Cargar la clave API desde el archivo .env
ELEVENLABS_API_KEY = config('ELEVENLABS_API_KEY')


def convert_text_to_speech(message, output_file="output.mp3"):
    body = {
        "text": message,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }
    voice_laura = "FGY2WhTYpPnrIDTdsKH5"
    voice_liam = "TX3LPaxmHKxFdv7VOQHJ"
    headers = {"xi-api-key": ELEVENLABS_API_KEY,
               "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_liam}"

    try:
        print("------- Enviando petición a elevenlabs -------")
        response = requests.post(endpoint, headers=headers, json=body)
        # Guardar la respuesta en un buffer
        with open(output_file, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error convirtiendo texto a voz ")
    if response.status_code == 200:
        return response.content
    else:
        return None


if __name__ == '__main__':
    convert_text_to_speech("Hola! me llamo Brayan, como estas?")
