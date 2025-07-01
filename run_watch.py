import streamlit as st
from datetime import datetime, timedelta
import random
import os

st.set_page_config(page_title="ohnabi 💖", page_icon="💖")

st.markdown("<h1 style='text-align: center; color: #ff69b4;'>ohnabi 💖</h1>", unsafe_allow_html=True)

fecha_inicio = datetime(2025, 3, 27)
dias = (datetime.now() - fecha_inicio).days
st.markdown(f"<h2 style='text-align: center;'>Llevamos <span style='color:#ff69b4'>{dias}</span> días juntos 🥰</h2>", unsafe_allow_html=True)

# Cuenta regresiva para cada mes juntos y para el aniversario del año
st.markdown("---")
st.subheader("Próximos meses juntos 💞")

hoy = datetime.now()
# Calcular el próximo mes de aniversario
if hoy.day < fecha_inicio.day:
    proximo_mes = hoy.replace(day=fecha_inicio.day)
else:
    if hoy.month == 12:
        proximo_mes = hoy.replace(year=hoy.year + 1, month=1, day=fecha_inicio.day)
    else:
        proximo_mes = hoy.replace(month=hoy.month + 1, day=fecha_inicio.day)
dias_para_mes = (proximo_mes - hoy).days
meses_juntos = (hoy.year - fecha_inicio.year) * 12 + (hoy.month - fecha_inicio.month)
if hoy.day >= fecha_inicio.day:
    meses_juntos += 1

st.info(f"¡Faltan {dias_para_mes} días para cumplir {meses_juntos} meses juntos! 🎉")

# Cuenta regresiva para el primer año
primer_anio = fecha_inicio.replace(year=fecha_inicio.year + 1)
dias_para_anio = (primer_anio - hoy).days
if dias_para_anio >= 0:
    st.success(f"¡Faltan {dias_para_anio} días para nuestro primer aniversario de 1 año! 🥳")
else:
    st.success("¡Ya cumplimos nuestro primer año juntos! 💖")

# Frases y mensajes
notas_romanticas = [
    "Eres mi persona favorita. Gracias por estar siempre conmigo. Te amo vida mía.",
    "Cada día contigo es el mejor regalo.",
    "No hay nada que me haga más feliz que verte sonreír."
]

mensajes_bonitos = [
    "¡Hoy será un gran día juntos!",
    "Recuerda que eres increíble. Siempre pienso en ti.",
    "Eres la razón de mi felicidad."
]

if st.button("Ver nota romántica"):
    st.info(random.choice(notas_romanticas))

if st.button("Ver mensaje bonito"):
    st.success(random.choice(mensajes_bonitos))

fechas_especiales = {
    "Aniversario": "27/03/2025",
    "Cumpleaños": "17/02/2006",
    "Primer encuentro": "4/12/2024",
    "Primer beso": "4/12/2024",
    "Mi Cumpleaños": "10/05/2005"
}
if st.button("Fechas especiales"):
    for k, v in fechas_especiales.items():
        st.write(f"**{k}:** {v}")

# Galería de fotos
if st.button("Ver galería de fotos 📸"):
    st.subheader("Nuestros momentos juntos")
    fotos_dir = "fotos"
    if os.path.exists(fotos_dir):
        fotos = [os.path.join(fotos_dir, f) for f in os.listdir(fotos_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
        if fotos:
            cols = st.columns(3)
            for idx, foto in enumerate(fotos):
                with cols[idx % 3]:
                    st.image(foto, use_container_width=True)
        else:
            st.info("Aún no hay fotos en la galería.")
    else:
        st.warning("Crea una carpeta llamada 'fotos' y pon ahí tus imágenes.")

# Espacio para que ella escriba una nota
st.markdown("---")
st.subheader("Escribe una nota para nosotros 💌")
nota = st.text_area("Tu mensaje aquí:")
if st.button("Guardar nota"):
    if nota.strip():
        with open("notas.txt", "a", encoding="utf-8") as f:
            f.write(nota.strip() + "\n")
        st.success("¡Nota guardada!")
    else:
        st.warning("Por favor, escribe algo antes de guardar.")

# Mostrar las notas guardadas
st.markdown("### Notas que has escrito 📝")
if os.path.exists("notas.txt"):
    with open("notas.txt", "r", encoding="utf-8") as f:
        notas_guardadas = f.readlines()
    if notas_guardadas:
        for n in notas_guardadas:
            st.info(n.strip())
    else:
        st.write("Aún no has escrito ninguna nota.")
else:
    st.write("Aún no has escrito ninguna nota.")

# Lista de deseos juntos
st.markdown("---")
st.subheader("Lista de deseos juntos ✨")
deseo = st.text_input("Escribe un deseo o meta:")
if st.button("Agregar deseo"):
    if deseo.strip():
        with open("deseos.txt", "a", encoding="utf-8") as f:
            f.write(deseo.strip() + "\n")
        st.success("¡Deseo agregado!")
if os.path.exists("deseos.txt"):
    with open("deseos.txt", "r", encoding="utf-8") as f:
        deseos = f.readlines()
    if deseos:
        st.markdown("#### Nuestros deseos:")
        for d in deseos:
            st.write(f"- {d.strip()}")

# Nuestra canción favorita
st.markdown("---")
st.subheader("Nuestra canción favorita 🎶")
st.video("https://youtu.be/MldGX_mbS-o?si=2DUzAZm9Q1LnKIPE")  # Cambia el enlace por el de tu canción

# Lista de tareas compartidas
st.markdown("---")
st.subheader("Lista de tareas juntos 📝")
tarea = st.text_input("Nueva tarea:")
if st.button("Agregar tarea"):
    if tarea.strip():
        with open("tareas.txt", "a", encoding="utf-8") as f:
            f.write("[ ] " + tarea.strip() + "\n")
        st.success("¡Tarea agregada!")

# Mostrar y marcar tareas
if os.path.exists("tareas.txt"):
    with open("tareas.txt", "r", encoding="utf-8") as f:
        tareas = f.readlines()
    nuevas_tareas = []
    for i, t in enumerate(tareas):
        hecho = st.checkbox(t[4:], value=t.startswith("[x]"), key=f"tarea_{i}")
        if hecho and t.startswith("[ ]"):
            nuevas_tareas.append("[x] " + t[4:])
        elif not hecho and t.startswith("[x]"):
            nuevas_tareas.append("[ ] " + t[4:])
        else:
            nuevas_tareas.append(t)
    # Guardar cambios
    with open("tareas.txt", "w", encoding="utf-8") as f:
        f.writelines(nuevas_tareas)
else:
    st.write("No hay tareas aún.")

# Juegos para parejas
st.markdown("---")
st.subheader("Juego para parejas 🎲")
preguntas = [
    "¿Cuál fue tu primera impresión de mí?",
    "¿Qué lugar te gustaría visitar conmigo?",
    "¿Cuál es nuestro mejor recuerdo juntos?",
    "¿Qué canción te recuerda a nosotros?",
    "¿Qué es lo que más te gusta de nuestra relación?",
    "¿Cuál ha sido nuestro momento más divertido?"
]
if st.button("Pregunta aleatoria"):
    st.info(random.choice(preguntas))

# Recordatorios de aniversarios o fechas especiales
st.markdown("---")
st.subheader("Recordatorios de fechas especiales 📅")
fechas_recordatorio = {
    "Aniversario": datetime(2025, 3, 27),
    "Cumpleaños de ella": datetime(2026, 2, 17),
    "Cumpleaños tuyo": datetime(2026, 5, 10)
}
for nombre, fecha in fechas_recordatorio.items():
    dias = (fecha - datetime.now()).days
    if dias >= 0:
        st.write(f"**{nombre}:** Faltan {dias} días ({fecha.strftime('%d/%m/%Y')})")
    else:
        st.write(f"**{nombre}:** Ya pasó este año ({fecha.strftime('%d/%m/%Y')})")