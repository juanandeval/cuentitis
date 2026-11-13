# Cuentitis
Web estática de lectura comprensiva (5-12 años). Sin servidor ni API: las lecturas están en `lecturas.json`.

## Probar en local
`python3 -m http.server 8000` y abre http://localhost:8000 (hace falta servidor; no vale abrir el archivo directamente).

## Publicar gratis
1. Sube esta carpeta a un repositorio de GitHub.
2. GitHub Pages: Settings → Pages → Deploy from branch → `main` / root. (También vale Netlify, Vercel o Cloudflare Pages conectando el repo.)
3. Cada `git push` actualiza la web.

## Añadir lecturas
Pide a Claude lecturas nuevas con este prompt y pega el resultado dentro del array de `lecturas.json`:

> Genera N lecturas en español de España para niños, en JSON con esta forma: {"id","band" (5-6|7-8|9-10|11-12),"topics" (1-2 de: Animales, Dinosaurios, Espacio, Fútbol, Princesas y reyes, Superhéroes, Piratas, Coches, Cocina, Ciencia, Dragones, Robots),"hero" (niño|niña|neutro),"title","paragraphs" (5-8, 450-550 palabras),"questions" (5: {"q","options","answer" (índice desde 0),"why"})}. Opciones: 3 por pregunta en 5-6 y 7-8 años, 4 en 9-10 y 11-12. 2 preguntas de detalle, 2 de inferencia, 1 de vocabulario o idea principal. Posición de la correcta variada. Lenguaje adaptado a la edad. Contenido positivo y apto para niños.

Después ejecuta `python3 validate.py` para comprobar el formato.

## Cómo elige la lectura
Filtra por tramo de edad y puntúa: tema principal (el primer gusto) > otros gustos > lecturas no vistas > protagonista según niño/niña (o neutro). Se guardan las ya vistas en el navegador para no repetir.

## Aviso de «lecturas nuevas»
Al abrir la web, esta compara los `id` de `lecturas.json` con los que ese navegador ya conocía. Si hay `id` nuevos, aparece una etiqueta 🆕 en la cabecera; al pulsarla se listan los títulos nuevos. La primera vez que alguien entra no se avisa de nada (todo es nuevo para él).
- Cada lectura nueva debe tener un `id` **único y nunca reutilizado**.
- Si cambias el texto de una lectura ya existente sin cambiar su `id`, no se avisa.
