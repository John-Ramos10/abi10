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
    "¡Hoy será un gran día vida mía!",
    "Recuerda que eres increíble. Siempre pienso en ti.",
    "Eres la razón de mi felicidad."
]

if st.button("Notita 🩵"):
    st.info(random.choice(notas_romanticas))

if st.button("Mensaje bonito 🩷"):
    st.success(random.choice(mensajes_bonitos))

fechas_especiales = {
    "Aniversario": "27/03/2025   💗" ,
    "Cumpleaños": "17/02/2006  🎂",
    "Primer encuentro": "4/12/2024  💞",
    "Primer beso": "4/12/2024 💋",
    "Mi Cumpleaños": "10/05/2005 🎉",
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
quien_nota = st.selectbox("¿Quién la escribe?", ["John", "Abi"], key="nota_quien")
if st.button("Guardar nota"):
    if nota.strip():
        with open("notas.txt", "a", encoding="utf-8") as f:
            f.write(f"{nota.strip()} ({quien_nota})\n")
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
quien_deseo = st.selectbox("¿Quién lo propone?", ["John", "Abi"], key="deseo_quien")
if st.button("Agregar deseo"):
    if deseo.strip():
        with open("deseos.txt", "a", encoding="utf-8") as f:
            f.write(f"{deseo.strip()} ({quien_deseo})\n")
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
quien_tarea = st.selectbox("¿Quién la propone?", ["John", "Abi"], key="tarea_quien")
if st.button("Agregar tarea"):
    if tarea.strip():
        with open("tareas.txt", "a", encoding="utf-8") as f:
            f.write(f"[ ] {tarea.strip()} ({quien_tarea})\n")
        st.success("¡Tarea agregada!")

# Mostrar y marcar tareas
if os.path.exists("tareas.txt"):
    with open("tareas.txt", "r", encoding="utf-8") as f:
        tareas = f.readlines()
    nuevas_tareas = []
    for i, t in enumerate(tareas):
        texto = t[4:].strip()
        hecho = st.checkbox(texto, value=t.startswith("[x]"), key=f"tarea_{i}")
        if hecho and t.startswith("[ ]"):
            nuevas_tareas.append("[x] " + texto + "\n")
        elif not hecho and t.startswith("[x]"):
            nuevas_tareas.append("[ ] " + texto + "\n")
        else:
            nuevas_tareas.append(t)
    with open("tareas.txt", "w", encoding="utf-8") as f:
        f.writelines(nuevas_tareas)
else:
    st.write("No hay tareas aún.")

# -------------------- JUEGOS PARA NOSOTROS DOS --------------------
st.markdown("---")
st.subheader("¡Juguemos juntos, Abi! 💑")

# Preguntas para conocernos más
preguntas = [
    "¿Cuál fue tu primera impresión de mí?",
    "¿Qué lugar te gustaría visitar conmigo?",
    "¿Cuál es nuestro mejor recuerdo juntos?",
    "¿Qué canción te recuerda a nosotros?",
    "¿Qué es lo que más te gusta de nuestra relación?",
    "¿Cuál ha sido nuestro momento más divertido?",
    "¿Qué sueño te gustaría cumplir conmigo?",
    "¿Qué hábito mío te parece más tierno?",
    "¿Qué comida te gustaría que cocinemos juntos?",
    "¿Qué película describe mejor nuestra relación?",
    "¿Qué apodo gracioso me pondrías?",
    "¿Qué harías si tuviéramos un día sin límites?",
    "¿Qué te gustaría aprender conmigo?",
    "¿Qué meta te gustaría lograr juntos?",
    "¿Qué es lo más loco que harías por mí?",
    "¿Qué viaje soñado tenemos pendiente?",
    "¿Qué tradición te gustaría crear juntos?",
    "¿Qué emoji crees que nos representa?",
    "¿Qué frase sientes que es nuestra?",
    "¿Qué harías si pudieras sorprenderme sin límites?"
]

# ¿Quién es más probable que...?
mas_probable = [
    "¿Quién de los dos es más probable que se duerma primero?",
    "¿Quién olvida más seguido las llaves?",
    "¿Quién hace más bromas?",
    "¿Quién canta más en la ducha?",
    "¿Quién se ríe más fuerte?",
    "¿Quién propone más planes locos?",
    "¿Quién se pone más romántico/a?",
    "¿Quién es más detallista?",
    "¿Quién se enoja más rápido?",
    "¿Quién es más probable que llore viendo una peli?"
]

# Verdad o reto
verdades = [
    "¿Qué es lo que más te gusta de mí?",
    "¿Cuál es tu recuerdo favorito conmigo?",
    "¿Qué te gustaría que hagamos más seguido?",
    "¿Qué es lo más tierno que he hecho por ti?",
    "¿Qué te gustaría decirme y aún no lo has hecho?",
    "¿Qué es lo que más te hace reír de mí?",
    "¿Qué sueño tienes conmigo?",
    "¿Qué es lo que más te enamora de nuestra relación?",
    "¿Qué cambiarías de nuestro día a día?",
    "¿Qué es lo que más te gustaría que nunca cambie entre nosotros?"
]
retos = [
    "Dime un piropo que nunca me hayas dicho.",
    "Hazme una declaración de amor como en una novela.",
    "Haz una cara graciosa y mándamela por WhatsApp.",
    "Cántame una canción romántica (aunque sea por audio).",
    "Hazme un dibujo rápido y mándamelo.",
    "Escríbeme un mensaje bonito y mándamelo.",
    "Haz un baile tonto y mándame el video.",
    "Prométeme algo para esta semana.",
    "Hazme una pregunta difícil.",
    "Imítame diciendo algo gracioso."
]

# Ruleta de actividades (sin repeticiones)
actividades = [
    "Dame un abrazo de 30 segundos.",
    "Veamos juntos un video gracioso.",
    "Hagamos una lista de 5 sueños juntos.",
    "Escribamos una carta para abrir en un año.",
    "Hagamos una selfie divertida.",
    "Bailemos una canción juntos.",
    "Dime 3 cosas que amas de mí.",
    "Hagamos un dibujo juntos.",
    "Planeemos una cita imaginaria.",
    "Invéntame un apodo nuevo."
]

# Preguntas rápidas
preguntas_rapidas = [
    "¿Color favorito?",
    "¿Comida favorita?",
    "¿Lugar soñado?",
    "¿Canción favorita?",
    "¿Película favorita?",
    "¿Animal favorito?",
    "¿Día favorito del año?",
    "¿Postre favorito?",
    "¿Serie favorita?",
    "¿Superhéroe favorito?"
]

# Reto semanal de pareja (sin repeticiones)
retos_semanales = [
    "Cocinen algo juntos esta semana.",
    "Vean una película nueva juntos.",
    "Den un paseo sin celulares.",
    "Escríbanse una carta a mano.",
    "Tómense una foto recreando una vieja foto.",
    "Hagan una lista de sueños juntos.",
    "Hagan una playlist juntos y escúchenla.",
    "Dediquen una noche a ver fotos viejas.",
    "Hagan un picnic (en casa o fuera).",
    "Aprendan algo nuevo juntos (baile, receta, idioma).",
    "Hagan una cita sorpresa para el otro.",
    "Hagan un dibujo el uno del otro.",
    "Escriban 5 cosas que aman del otro y léanlas.",
    "Hagan una tarde de juegos de mesa o cartas.",
    "Planeen un viaje soñado (aunque sea imaginario).",
    "Hagan una lista de metas para el próximo mes.",
    "Hagan un video divertido juntos.",
    "Vístanse igual o combinen ropa un día.",
    "Hagan una noche de karaoke en casa.",
    "Hagan una cápsula del tiempo para abrir en un año."
]

# Guardar y mostrar el reto semanal sin repetir
st.markdown("---")
st.subheader("Reto semanal de pareja 🏆")
if "retos_mostrados" not in st.session_state:
    st.session_state.retos_mostrados = []
if "reto_semanal" not in st.session_state or st.button("Nuevo reto semanal"):
    disponibles = [r for r in retos_semanales if r not in st.session_state.retos_mostrados]
    if not disponibles:
        st.session_state.retos_mostrados = []
        disponibles = retos_semanales.copy()
    st.session_state.reto_semanal = random.choice(disponibles)
    st.session_state.retos_mostrados.append(st.session_state.reto_semanal)
st.info(f"Reto de la semana: {st.session_state.reto_semanal}")

# Selector de juego
juego = st.selectbox(
    "¿Qué quieres jugar hoy, Abi?",
    [
        "Preguntas para conocernos",
        "¿Quién es más probable que...?",
        "Verdad o reto",
        "Ruleta de actividades",
        "Preguntas rápidas",
        "Lista de sueños juntos",
        "Cosas que quiero hacer contigo",
        "Nuestro top 5",
        "Historias inventadas",
        "Preguntas de confianza",
        "Preguntas de futuro"
    ]
)

if juego == "Preguntas para conocernos":
    if "pregunta_actual" not in st.session_state:
        st.session_state.pregunta_actual = ""
    if st.button("Hazme una pregunta aleatoria"):
        st.session_state.pregunta_actual = random.choice(preguntas)
    if st.session_state.pregunta_actual:
        st.info(st.session_state.pregunta_actual)
        respuesta = st.text_input("Tu respuesta, Abi:", key="respuesta_pareja_conocernos")
        if st.button("Guardar respuesta"):
            if respuesta.strip():
                # Se guarda en respuestas_pareja.txt
                with open("respuestas_pareja.txt", "a", encoding="utf-8") as f:
                    f.write(f"{st.session_state.pregunta_actual} - {respuesta.strip()} (Abi)\n")
                st.success("¡Respuesta guardada!")
            else:
                st.warning("Escribe una respuesta antes de guardar.")
        st.markdown("#### Tus respuestas:")
        if os.path.exists("respuestas_pareja.txt"):
            with open("respuestas_pareja.txt", "r", encoding="utf-8") as f:
                respuestas_guardadas = f.readlines()
            for r in respuestas_guardadas:
                st.write(r.strip())
        else:
            st.write("Aún no hay respuestas guardadas.")

elif juego == "¿Quién es más probable que...?":
    if "mas_probables_mostradas" not in st.session_state:
        st.session_state.mas_probables_mostradas = []
    if st.button("Siguiente pregunta"):
        disponibles = [p for p in mas_probable if p not in st.session_state.mas_probables_mostradas]
        if not disponibles:
            st.session_state.mas_probables_mostradas = []
            disponibles = mas_probable.copy()
        st.session_state.mas_probable = random.choice(disponibles)
        st.session_state.mas_probables_mostradas.append(st.session_state.mas_probable)
    if "mas_probable" in st.session_state:
        st.info(st.session_state.mas_probable)

elif juego == "Verdad o reto":
    tipo = st.radio("Elige:", ["Verdad", "Reto"], key="verdad_reto_tipo")
    if "verdades_mostradas" not in st.session_state:
        st.session_state.verdades_mostradas = []
    if "retos_mostrados_juego" not in st.session_state:
        st.session_state.retos_mostrados_juego = []
    if st.button("Siguiente (Verdad o Reto)"):
        if tipo == "Verdad":
            disponibles = [v for v in verdades if v not in st.session_state.verdades_mostradas]
            if not disponibles:
                st.session_state.verdades_mostradas = []
                disponibles = verdades.copy()
            st.session_state.verdad = random.choice(disponibles)
            st.session_state.verdades_mostradas.append(st.session_state.verdad)
            st.session_state.reto = ""
        else:
            disponibles = [r for r in retos if r not in st.session_state.retos_mostrados_juego]
            if not disponibles:
                st.session_state.retos_mostrados_juego = []
                disponibles = retos.copy()
            st.session_state.reto = random.choice(disponibles)
            st.session_state.retos_mostrados_juego.append(st.session_state.reto)
            st.session_state.verdad = ""
    if st.session_state.get("verdad"):
        st.info("Verdad: " + st.session_state.verdad)
    if st.session_state.get("reto"):
        st.warning("Reto: " + st.session_state.reto)

elif juego == "Ruleta de actividades":
    if "actividades_mostradas" not in st.session_state:
        st.session_state.actividades_mostradas = []
    if st.button("Girar ruleta"):
        disponibles = [a for a in actividades if a not in st.session_state.actividades_mostradas]
        if not disponibles:
            st.session_state.actividades_mostradas = []
            disponibles = actividades.copy()
        st.session_state.actividad = random.choice(disponibles)
        st.session_state.actividades_mostradas.append(st.session_state.actividad)
    if st.session_state.get("actividad"):
        st.success("Actividad: " + st.session_state.actividad)

elif juego == "Preguntas rápidas":
    if st.button("Pregunta rápida"):
        st.session_state.pregunta_rapida = random.choice(preguntas_rapidas)
    if st.session_state.get("pregunta_rapida"):
        st.info(st.session_state.pregunta_rapida)

elif juego == "Lista de sueños juntos":
    st.markdown("Escribe sueños o metas que quieras lograr conmigo:")
    sueno = st.text_input("Nuevo sueño:", key="sueno_nuevo")
    if st.button("Agregar sueño"):
        if sueno.strip():
            # Se guarda en suenos_juntos.txt
            with open("suenos_juntos.txt", "a", encoding="utf-8") as f:
                f.write(f"{sueno.strip()} (Abi)\n")
            st.success("¡Sueño agregado!")
    if os.path.exists("suenos_juntos.txt"):
        with open("suenos_juntos.txt", "r", encoding="utf-8") as f:
            suenos = f.readlines()
        st.markdown("#### Nuestros sueños juntos:")
        for s in suenos:
            st.write(f"🌟 {s.strip()}")

elif juego == "Cosas que quiero hacer contigo":
    st.markdown("Escribe cosas que quieras hacer conmigo:")
    cosa = st.text_input("Nueva cosa:", key="cosa_nueva")
    if st.button("Agregar cosa"):
        if cosa.strip():
            # Se guarda en cosas_contigo.txt
            with open("cosas_contigo.txt", "a", encoding="utf-8") as f:
                f.write(f"{cosa.strip()} (Abi)\n")
            st.success("¡Agregado!")
    if os.path.exists("cosas_contigo.txt"):
        with open("cosas_contigo.txt", "r", encoding="utf-8") as f:
            cosas = f.readlines()
        st.markdown("#### Cosas que quieres hacer conmigo:")
        for c in cosas:
            st.write(f"💡 {c.strip()}")

elif juego == "Nuestro top 5":
    st.markdown("Haz nuestro ranking de cosas favoritas (comidas, pelis, lugares, etc.):")
    top = st.text_input("Agrega algo a nuestro top:", key="top_nuevo")
    if st.button("Agregar al top"):
        if top.strip():
            # Se guarda en top5.txt
            with open("top5.txt", "a", encoding="utf-8") as f:
                f.write(f"{top.strip()} (Abi)\n")
            st.success("¡Agregado!")
    if os.path.exists("top5.txt"):
        with open("top5.txt", "r", encoding="utf-8") as f:
            top5 = f.readlines()
        st.markdown("#### Nuestro top 5:")
        for t in top5:
            st.write(f"⭐ {t.strip()}")

elif juego == "Historias inventadas":
    st.markdown("Inventemos una historia juntos. Escribe una frase y yo la continúo:")
    frase_historia = st.text_input("Nueva frase para la historia:", key="historia_nueva")
    if st.button("Agregar frase a la historia"):
        if frase_historia.strip():
            # Se guarda en historia.txt
            with open("historia.txt", "a", encoding="utf-8") as f:
                f.write(f"{frase_historia.strip()} (Abi)\n")
            st.success("¡Frase agregada!")
    if os.path.exists("historia.txt"):
        with open("historia.txt", "r", encoding="utf-8") as f:
            historia = f.readlines()
        st.markdown("#### Nuestra historia inventada:")
        for h in historia:
            st.write(f"📖 {h.strip()}")

elif juego == "Preguntas de confianza":
    preguntas_confianza = [
        "¿Hay algo que nunca me hayas contado?",
        "¿Qué es lo que más te cuesta decirme?",
        "¿Qué te gustaría que mejoremos juntos?",
        "¿Qué te hace sentir segura conmigo?",
        "¿Qué te gustaría que nunca cambie entre nosotros?",
        "¿Qué te gustaría que hablemos más?",
        "¿Qué harías si tuvieras miedo y yo no estuviera?",
        "¿Qué te gustaría que haga por ti cuando estés triste?",
        "¿Qué te gustaría que recuerde siempre de ti?",
        "¿Qué te gustaría que nunca olvide?"
    ]
    if st.button("Pregunta de confianza"):
        st.session_state.pregunta_confianza = random.choice(preguntas_confianza)
    if st.session_state.get("pregunta_confianza"):
        st.info(st.session_state.pregunta_confianza)

elif juego == "Preguntas de futuro":
    preguntas_futuro = [
        "¿Dónde te imaginas conmigo en 5 años?",
        "¿Qué meta te gustaría lograr juntos en el futuro?",
        "¿Qué tipo de familia te gustaría formar conmigo?",
        "¿Qué viaje soñado te gustaría hacer conmigo?",
        "¿Qué tradición te gustaría crear juntos?",
        "¿Qué te gustaría que logremos como pareja?",
        "¿Qué te gustaría que nunca falte en nuestro futuro?",
        "¿Qué te gustaría que aprendamos juntos?",
        "¿Qué te gustaría que recordemos siempre?",
        "¿Qué te gustaría que sea nuestro próximo gran paso?"
    ]
    if st.button("Pregunta de futuro"):
        st.session_state.pregunta_futuro = random.choice(preguntas_futuro)
    if st.session_state.get("pregunta_futuro"):
        st.info(st.session_state.pregunta_futuro)

# -------------------- FIN JUEGOS --------------------

# Recordatorios de aniversarios o fechas especiales
st.markdown("---")
st.subheader("Recordatorios de fechas especiales 📅")
fechas_recordatorio = {
    "Aniversario (1 año)": datetime(fecha_inicio.year + 1, fecha_inicio.month, fecha_inicio.day),
    "Cumpleaños de ella": datetime(2026, 2, 17),
    "Cumpleaños tuyo": datetime(2026, 5, 10)
}
for nombre, fecha in fechas_recordatorio.items():
    dias = (fecha - datetime.now()).days
    if nombre.startswith("Aniversario"):
        if dias >= 0:
            st.write(f"**{nombre}:** Faltan {dias} días ({fecha.strftime('%d/%m/%Y')})")
        else:
            st.write(f"**{nombre}:** ¡Ya cumplimos nuestro primer año juntos! ({fecha.strftime('%d/%m/%Y')})")
    else:
        if dias >= 0:
            st.write(f"**{nombre}:** Faltan {dias} días ({fecha.strftime('%d/%m/%Y')})")
        else:
            st.write(f"**{nombre}:** Ya pasó este año ({fecha.strftime('%d/%m/%Y')})")