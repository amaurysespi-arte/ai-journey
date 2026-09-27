from google import genai


client = genai.Client()


def procesar_texto():
	print("--- Asistente de IA (Gemini): Resúmenes y Preguntas ---")

	texto_usuario = input(
		"\nPor favor, escribe o pega el texto que deseas analizar:\n> "
	)
	if not texto_usuario.strip():
		print("El texto no puede estar vacío.")
		return

	print("\n¿Qué deseas hacer con este texto?")
	print("1. Resumirlo")
	print("2. Hacer una pregunta sobre el texto")
	opcion = input("Selecciona una opción (1 o 2): ")

	if opcion == "1":
		prompt_final = (
			"Instrucción: Eres un asistente experto. Tu tarea es resumir "
			"de forma clara y concisa el texto provisto.\n\n"
			f"Texto a resumir:\n{texto_usuario}"
		)
	elif opcion == "2":
		pregunta = input("\nEscribe tu pregunta sobre el texto:\n> ")
		prompt_final = (
			"Instrucción: Eres un asistente experto. Responde la pregunta "
			"basándote estrictamente en el texto provisto.\n\n"
			f"Texto:\n{texto_usuario}\n\nPregunta: {pregunta}"
		)
	else:
		print("Opción no válida. Saliendo del programa.")
		return

	print("\n[Procesando con Gemini...]")

	try:
		respuesta = client.models.generate_content(
			model="gemini-3.8-flash",
			contents=prompt_final,
		)

		print("\n=== RESPUESTA DE LA IA ===")
		print(respuesta.text)
		print("==========================")
	except Exception as e:
		print(f"\nOcurrió un error al conectar con la API: {e}")
		print("Asegúrate de haber configurado tu GEMINI_API_KEY correctamente.")


if __name__ == "__main__":
	procesar_texto()