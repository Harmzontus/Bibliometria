import os
import subprocess
from datetime import datetime

import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Automatización",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 36px;
        font-weight: bold;
        color: #4169E1;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        background-color: #f8f9fa;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .section-header {
        color: #2E8B57;
        font-weight: bold;
        border-bottom: 2px solid #2E8B57;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #666;
        font-size: 14px;
        margin-top: 50px;
    }
    .highlight {
        background-color: #FFE4B5;
        padding: 2px 5px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

def run_notebook(directorio, archivo):
    """Ejecuta un notebook de Jupyter utilizando jupyter nbconvert"""
    try:
        # Construir la ruta completa al archivo
        ruta_completa = os.path.join(os.path.abspath(directorio), archivo)
        
        # Verificar que el archivo existe
        if not os.path.exists(ruta_completa):
            st.error(f"No se encontró el archivo: {ruta_completa}")
            return False
        
        # Comando para ejecutar el notebook
        cmd = ["jupyter", "nbconvert", "--execute", "--to", "notebook", "--inplace", ruta_completa]
        
        # Ejecutar el proceso con manejo mejorado
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        
        # Capturar la salida y errores
        stdout, stderr = process.communicate()
        
        # Verificar si la ejecución fue exitosa
        if process.returncode == 0:
            st.success(f"✅{archivo} ejecutado exitosamente")
            # Mostrar detalles de la ejecución
            with st.expander("Ver detalles de ejecución"):
                st.write("Salida del comando:")
                st.code(stdout)
            return True
        else:
            st.error(f"❌ Error al ejecutar {archivo}")
            st.error(f"Código de error: {process.returncode}")
            st.error(f"Mensaje de error: {stderr}")
            return False
            
    except Exception as e:
        st.error(f"Error inesperado al ejecutar {archivo}: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return False

def mostrar_interfaz():
    """Muestra la interfaz principal con un diseño creativo"""
    # Header con animación
    st.markdown('<div class="main-header">🚀 Sistema de Automatización de Procesos</div>', unsafe_allow_html=True)
    
    # Mensaje de bienvenida con fecha actual
    fecha_actual = datetime.now().strftime("%d de %B, %Y")
    st.markdown(f"#### Bienvenido al panel de control - {fecha_actual}")
    
    # Sidebar con opciones
    with st.sidebar:
        st.image("https://www.python.org/static/community_logos/python-logo-generic.svg", width=200)
        st.markdown("### Navegación")
        vista = st.radio(
            "Selecciona una vista:",
            ["Dashboard", "Bases de Datos", "Procesamiento", "Visualización"]
        )
        
        st.markdown("---")
        st.markdown("### Información")
        st.info("Este sistema permite automatizar procesos relacionados con bases de datos y visualización de información.")
        
        # Métricas en el sidebar
        st.markdown("### Métricas")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Archivos", value="25")
        with col2:
            st.metric(label="Procesos", value="8")
    
    # Rutas absolutas para asegurar compatibilidad
    base_dir = os.path.abspath("C:/Users/FAFA/Desktop/algoritmos/algoritmos")
    
    # Configurar los directorios
    directorio_notebooks1 = os.path.join(base_dir, "descarga automatica para la base de datos")
    directorio_notebooks2 = os.path.join(base_dir, "metodos de ordenamiento")
    directorio_imagenes = os.path.join(base_dir, "img")
    directorio_datos_ordenados = os.path.join(base_dir, "datos ordenados")

    # Obtener listas de archivos (verificando que los directorios existan)
    archivos_notebooks1 = []
    if os.path.exists(directorio_notebooks1):
        archivos_notebooks1 = [f for f in os.listdir(directorio_notebooks1) if f.endswith(".ipynb")]
    else:
        st.warning(f"El directorio {directorio_notebooks1} no existe")
    
    archivos_notebooks2 = []
    if os.path.exists(directorio_notebooks2):
        archivos_notebooks2 = [f for f in os.listdir(directorio_notebooks2) if f.endswith((".py", ".ipynb"))]
    
    archivos_imagenes = []
    if os.path.exists(directorio_imagenes):
        archivos_imagenes = [f for f in os.listdir(directorio_imagenes) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    archivos_datos_ordenados = []
    if os.path.exists(directorio_datos_ordenados):
        archivos_datos_ordenados = [f for f in os.listdir(directorio_datos_ordenados) if f.endswith(('.csv', '.xlsx'))]

    # Dashboard principal
    if vista == "Dashboard":
        st.markdown('<h3 class="section-header">Panel de Control</h3>', unsafe_allow_html=True)
        
        # Tarjetas resumen
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📊 Bases de Datos")
            st.write(f"{len(archivos_notebooks1)} notebooks disponibles")
            st.progress(min(len(archivos_notebooks1)/10, 1.0))
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🔄 Procesos")
            st.write(f"{len(archivos_notebooks2)} métodos de ordenamiento")
            st.progress(min(len(archivos_notebooks2)/10, 1.0))
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📁 Datos")
            st.write(f"{len(archivos_datos_ordenados)} archivos disponibles")
            st.progress(min(len(archivos_datos_ordenados)/10, 1.0))
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col4:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🖼️ Imágenes")
            st.write(f"{len(archivos_imagenes)} visualizaciones")
            st.progress(min(len(archivos_imagenes)/10, 1.0))
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Acceso rápido
        st.markdown('<h3 class="section-header">Acceso Rápido</h3>', unsafe_allow_html=True)
        tabs = st.tabs(["Bases de Datos", "Ordenamiento", "Datos", "Imágenes"])
        
        with tabs[0]:
            if archivos_notebooks1:
                for i, archivo in enumerate(archivos_notebooks1[:3]):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{archivo}**")
                    with col2:
                        if st.button("Ejecutar", key=f"quick_db_{i}"):
                            with st.spinner(f"Ejecutando {archivo}..."):
                                if run_notebook(directorio_notebooks1, archivo):
                                    st.success(f"¡Notebook ejecutado correctamente!")
            else:
                st.info("No hay notebooks disponibles")
                
        with tabs[1]:
            if archivos_notebooks2:
                for i, archivo in enumerate(archivos_notebooks2[:3]):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{archivo}**")
                    with col2:
                        if st.button("Ejecutar", key=f"quick_sort_{i}"):
                            with st.spinner(f"Ejecutando {archivo}..."):
                                if run_notebook(directorio_notebooks2, archivo):
                                    st.success(f"¡Método de ordenamiento ejecutado!")
            else:
                st.info("No hay métodos de ordenamiento disponibles")
                
        with tabs[2]:
            if archivos_datos_ordenados:
                for i, archivo in enumerate(archivos_datos_ordenados[:3]):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{archivo}**")
                    with col2:
                        if st.button("Ver", key=f"quick_data_{i}"):
                            st.session_state.archivo_datos_seleccionado = archivo
                            st.success(f"Archivo seleccionado: {archivo}")
            else:
                st.info("No hay datos ordenados disponibles")
                
        with tabs[3]:
            if archivos_imagenes:
                image_cols = st.columns(3)
                for i, archivo in enumerate(archivos_imagenes[:3]):
                    with image_cols[i % 3]:
                        st.image(os.path.join(directorio_imagenes, archivo), 
                                caption=archivo, 
                                use_container_width=True)
            else:
                st.info("No hay imágenes disponibles")

    # Vista de Bases de Datos
    elif vista == "Bases de Datos":
        st.markdown('<h3 class="section-header">Descarga Automática de Datos</h3>', unsafe_allow_html=True)
        
        # Filtrar notebooks
        notebooks_filtrados = [nb for nb in archivos_notebooks1]
        
        if notebooks_filtrados:
            for i, archivo in enumerate(notebooks_filtrados):
                st.markdown('<div class="card">', unsafe_allow_html=True)
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.markdown(f"### {archivo}")
                    st.markdown(f"<span class>Notebook para obtención de datos</span>", unsafe_allow_html=True)
                
                with col2:
                    if st.button("Ejecutar", key=f"db_{i}"):
                        with st.spinner(f"Ejecutando {archivo}..."):
                            if run_notebook(directorio_notebooks1, archivo):
                                st.success(f"¡Notebook ejecutado correctamente!")
                                st.balloons()
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("No se encontraron notebooks que coincidan con la búsqueda")

    # Vista de Procesamiento
    elif vista == "Procesamiento":
        st.markdown('<h3 class="section-header">Métodos de Ordenamiento</h3>', unsafe_allow_html=True)
        
        # Organizar en cuadrícula
        if archivos_notebooks2:
            cols = st.columns(3)
            for i, archivo in enumerate(archivos_notebooks2):
                with cols[i % 3]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown(f"### {archivo}")
                    
                    # Simular una descripción
                    descripciones = {
                        "ordenar_por_fecha.ipynb": "Ordena datos cronológicamente",
                        "ordenar_por_categoria.ipynb": "Agrupa y ordena por categorías",
                        "ordenar_por_valor.ipynb": "Ordena por valor numérico"
                    }
                    
                    descripcion = descripciones.get(archivo, "Método de ordenamiento de datos")
                    st.write(descripcion)
                    
                    if st.button("Ejecutar Proceso", key=f"proc_{i}"):
                        with st.spinner(f"Ejecutando {archivo}..."):
                            if run_notebook(directorio_notebooks2, archivo):
                                st.success(f"¡Proceso completado!")
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("No hay métodos de ordenamiento disponibles")

    # Vista de Visualización
    elif vista == "Visualización":
        st.markdown('<h3 class="section-header">Datos e Imágenes</h3>', unsafe_allow_html=True)
        
        # Pestañas para datos e imágenes
        vis_tabs = st.tabs(["Datos Ordenados", "Imágenes"])
        
        with vis_tabs[0]:
            if archivos_datos_ordenados:
                # Selector con buscador
                archivo_seleccionado = st.selectbox(
                    "Selecciona un archivo de datos:",
                    archivos_datos_ordenados
                )
                
                if archivo_seleccionado:
                    st.markdown(f"**Visualizando:** {archivo_seleccionado}")
                    
                    # Determinar la ruta del archivo
                    ruta_datos = os.path.join(directorio_datos_ordenados, archivo_seleccionado)
                    
                    # Leer el archivo según su extensión
                    try:
                        if archivo_seleccionado.endswith('.csv'):
                            df = pd.read_csv(ruta_datos)
                        elif archivo_seleccionado.endswith('.xlsx'):
                            df = pd.read_excel(ruta_datos)
                        
                        # Opciones de visualización
                        opciones_col1, opciones_col2 = st.columns(2)
                        with opciones_col1:
                            mostrar_filas = st.slider("Número de filas a mostrar", 5, 100, 10)
                        with opciones_col2:
                            ordenar_por = st.selectbox("Ordenar por columna:", 
                                                      ["Sin ordenar"] + list(df.columns))
                        
                        # Aplicar ordenamiento si se seleccionó
                        if ordenar_por != "Sin ordenar":
                            df = df.sort_values(by=ordenar_por)
                        
                        # Mostrar el dataframe
                        st.dataframe(df.head(mostrar_filas))
                        
                        # Estadísticas del dataset
                        with st.expander("Estadísticas del conjunto de datos"):
                            st.write(f"**Número de filas:** {len(df)}")
                            st.write(f"**Número de columnas:** {len(df.columns)}")
                            st.write("**Columnas:**")
                            for col in df.columns:
                                st.write(f"- {col}")
                            
                            # Si hay columnas numéricas, mostrar estadísticas
                            numeric_cols = df.select_dtypes(include=['number']).columns
                            if not numeric_cols.empty:
                                st.write("**Estadísticas numéricas:**")
                                st.dataframe(df[numeric_cols].describe())
                    except Exception as e:
                        st.error(f"Error al leer el archivo: {e}")
            else:
                st.info("No hay archivos de datos disponibles")
                
        with vis_tabs[1]:
            if archivos_imagenes:
                # Galería de imágenes
                st.markdown("### Galería de Visualizaciones")
                
                # Crear filas de 3 imágenes
                for i in range(0, len(archivos_imagenes), 3):
                    cols = st.columns(3)
                    for j in range(3):
                        if i+j < len(archivos_imagenes):
                            archivo = archivos_imagenes[i+j]
                            with cols[j]:
                                st.image(os.path.join(directorio_imagenes, archivo), 
                                        caption=archivo,
                                        use_container_width=True)
                                if st.button("Ver Ampliado", key=f"img_{i+j}"):
                                    st.session_state.imagen_ampliada = archivo
            else:
                st.info("No hay imágenes disponibles")
    
    # Mostrar imagen ampliada si está seleccionada
    if 'imagen_ampliada' in st.session_state and st.session_state.imagen_ampliada:
        with st.dialog("Imagen Ampliada"):
            st.image(os.path.join(directorio_imagenes, st.session_state.imagen_ampliada), 
                    caption=st.session_state.imagen_ampliada,
                    use_container_width=True)
            if st.button("Cerrar"):
                del st.session_state.imagen_ampliada
    
    # Mostrar contenido del archivo seleccionado si está en la sesión
    if 'archivo_datos_seleccionado' in st.session_state and st.session_state.archivo_datos_seleccionado:
        with st.expander(f"Contenido de {st.session_state.archivo_datos_seleccionado}", expanded=True):
            # Determinar la ruta del archivo
            ruta_datos = os.path.join(directorio_datos_ordenados, st.session_state.archivo_datos_seleccionado)
            
            # Leer el archivo según su extensión
            try:
                if st.session_state.archivo_datos_seleccionado.endswith('.csv'):
                    df = pd.read_csv(ruta_datos)
                elif st.session_state.archivo_datos_seleccionado.endswith('.xlsx'):
                    df = pd.read_excel(ruta_datos)
                
                # Mostrar el dataframe
                st.dataframe(df)
                
                # Opciones para descargar
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Descargar como CSV",
                    data=csv,
                    file_name=f"datos_{st.session_state.archivo_datos_seleccionado.split('.')[0]}.csv",
                    mime='text/csv',
                )
            except Exception as e:
                st.error(f"Error al leer el archivo: {e}")
    
    # Footer
    st.markdown("""
    <div class="footer">
        Sistema de Automatización de Procesos © 2025<br>
        Desarrollado con Streamlit
    </div>
    """, unsafe_allow_html=True)

# Inicializar el estado de la sesión si es necesario
if 'archivo_datos_seleccionado' not in st.session_state:
    st.session_state.archivo_datos_seleccionado = None

# Configurar un mensaje para indicar el estado de Jupyter
try:
    # Verificar si jupyter está instalado y disponible
    result = subprocess.run(["jupyter", "--version"], capture_output=True, text=True)
except Exception as e:
    st.sidebar.error(f"❌ Jupyter no está disponible: {str(e)}")
    st.sidebar.info("Asegúrate de tener instalado Jupyter con: pip install jupyter")

# Mostrar la interfaz principal (sin login)
mostrar_interfaz()