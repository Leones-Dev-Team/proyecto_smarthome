
---

## 🛠 Paso a paso con Git

### 1️⃣ Clonar el repositorio remoto

Esto crea una copia local del repositorio online.

```bash
git clone https://github.com/Leones-Dev-Team/proyecto_smarthome.git
```

📌 Esto crea una carpeta `proyecto_smarthome` con todo el historial y la rama `main` por defecto.

---

### 2️⃣ Entrar a la carpeta del proyecto

```bash
cd proyecto_smarthome
```

---

### 3️⃣ Crear una rama secundaria **local**

Supongamos que la rama se llama `feature-modularizacion`:

```bash
git branch feature-modularizacion
```

---

### 4️⃣ Cambiarte a esa rama secundaria local

```bash
git checkout feature-modularizacion
```

💡 También podés hacerlo en un solo paso:

```bash
git checkout -b feature-modularizacion
```

---

### 5️⃣ Crear la rama secundaria **remota** y vincularla

Cuando subas por primera vez, usás `-u` para establecer el seguimiento:

```bash
git push -u origin feature-modularizacion
```

Ahora tu rama local `feature-modularizacion` está vinculada a la rama remota del mismo nombre.

---

### 6️⃣ Hacer cambios en el código

Editá, agregá o eliminá archivos según lo que necesites.

---

### 7️⃣ Preparar los cambios para commit (**staging**)

```bash
git add .
```

💡 El `.` agrega todos los cambios. Si querés agregar solo archivos específicos:

```bash
git add ruta/al/archivo.py
```

---

### 8️⃣ Hacer el commit

```bash
git commit -m "Descripción clara de los cambios realizados"
```

---

### 9️⃣ Subir los cambios a la rama secundaria remota

```bash
git push
```

💡 Como ya configuraste el seguimiento en el paso 5, no hace falta poner `origin feature-modularizacion` cada vez.

---

### 🔄 10️⃣ Solicitar el merge (Pull Request)

- Ir a **GitHub** → repositorio `proyecto_smarthome`.
- Vas a ver un aviso para crear un **Pull Request** desde `feature-modularizacion` hacia `main`.
- Revisá los cambios, poné un título y descripción, y creá el PR.
- Esperá la revisión y aprobación (o hacelo vos si tenés permisos).

---

### 1️⃣1️⃣ Una vez fusionado en `main` (merge completado en GitHub)

Volvemos a la rama `main` local:

```bash
git checkout main
```

---

### 1️⃣2️⃣ Actualizar `main` local con los cambios del remoto

```bash
git pull origin main
```

---

### 1️⃣3️⃣ Volver a la rama secundaria local

```bash
git checkout feature-modularizacion
```

---

### 1️⃣4️⃣ Fusionar los cambios de `main` en tu rama secundaria local

Esto mantiene tu rama secundaria actualizada con lo último de `main`:

```bash
git merge main
```

💡 Si no hay conflictos, listo. Si hay conflictos, Git te pedirá resolverlos antes de confirmar el merge.

---

## 📌 Resumen visual del flujo

1. **Clonar** → `git clone ...`
2. **Crear rama local** → `git checkout -b feature`
3. **Subir rama remota** → `git push -u origin feature`
4. **Cambiar código**
5. **Staging** → `git add .`
6. **Commit** → `git commit -m "..."`
7. **Push** → `git push`
8. **Pull Request** en GitHub
9. **Merge** en GitHub
10. **Actualizar main local** → `git checkout main` + `git pull`
11. **Volver a rama secundaria** → `git checkout feature`
12. **Merge desde main** → `git merge main`

---
