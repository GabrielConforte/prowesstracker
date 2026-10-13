# prowesstracker
app de seguimiento del mazo izzet

Abrí `index.html` en el navegador (ideal en el celular). No necesita instalación ni servidor.

## Instalar en el celular
1. Activá GitHub Pages: en el repo, **Settings → Pages → Build and deployment → Source: Deploy from a branch**, elegí la rama donde está la app y la carpeta `/ (root)`, y guardá.
2. En un minuto queda en `https://gabrielconforte.github.io/prowesstracker/`.
3. Abrí esa dirección en el celular:
   - **Android (Chrome)**: menú ⋮ → **Agregar a la pantalla principal** / **Instalar app**.
   - **iPhone (Safari)**: botón Compartir → **Agregar a inicio**.
4. Queda un ícono 🔥 que abre la app a pantalla completa. Funciona sin cuenta y guarda la partida en el celular.

## Uso
- **Criaturas**: `+` / `−` para poner o sacar Monastery Swiftspear, Slickshot Show-Off, Dragon's Rage Channeler o Monk tokens del campo.
- **⚡ Hechizo no-criatura**: dispara el trigger de todas las criaturas a la vez (Swiftspear y Monk +1/+1, Slickshot +2/+0, DRC nada).
- **Prowess** en cada carta: dispara solo esa criatura.
- **+3 / +2 / +1** de fuerza y resistencia: pumps hasta fin de turno.
- **Delirium** (en DRC): pasa a 3/3 con vuelo.
- **Role token** (Monstrous Rage): Monster role, +1/+1 y arrolla. Permanente.
- **Equipar Cori-Steel**: +1/+1, arrolla y prisa. Permanente.
- **Fin de turno**: suma un turno al contador y limpia prowess, pumps y el contador de hechizos (role, equipo y delirium quedan).
- **Vidas**: contador de vida tuyo y del rival (−5, −1, +1, +5), arranca en 20.
- **💥 Pegar con todo**: resta al rival la fuerza total de tus criaturas.
- **🔄 Nueva partida**: reinicia vidas y campo (tocá dos veces para confirmar).
- **↶**: deshacer.

El estado se guarda en el navegador.
