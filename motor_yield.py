

import streamlit as st

# Funciones de cálculo
def calculate_motor_yield(dog_leg, feet_slid):
    """
    Calcula el motor yield de un motor de fondo para perforación direccional.
    """
    if feet_slid <= 0:
        raise ValueError("La cantidad de pies deslizados debe ser mayor que cero.")
    motor_yield = dog_leg / feet_slid
    return motor_yield

def calculate_feet_to_slide(desired_dog_leg, motor_yield):
    """
    Calcula los pies que necesitas deslizar para alcanzar un dogleg deseado.
    """
    if motor_yield <= 0:
        raise ValueError("El motor yield debe ser mayor que cero.")
    feet_slid = desired_dog_leg / motor_yield
    return feet_slid

# Interfaz de Streamlit
st.title("Cálculo de Motor Yield y Pies Deslizados")

# Paso 1: Calcular el Motor Yield
st.header("Paso 1: Calcular el Motor Yield")
dog_leg = st.number_input("Ingresa el Dogleg Severity actual (en grados por 100 pies):", min_value=0.0, step=0.1)
feet_slid = st.number_input("Ingresa la cantidad de pies deslizados:", min_value=0.0, step=1.0)

if st.button("Calcular Motor Yield"):
    try:
        motor_yield = calculate_motor_yield(dog_leg, feet_slid)
        st.session_state.motor_yield = motor_yield  # Guardar el valor de motor_yield en session_state
        st.success(f"El Motor Yield es: {motor_yield:.4f} grados por pie deslizado.")
    except ValueError as e:
        st.error(str(e))

# Paso 2: Calcular los Pies Necesarios para un Dogleg Deseado
st.header("Paso 2: Calcular los Pies Necesarios para un Dogleg Deseado")
desired_dog_leg = st.number_input("Ingresa el Dogleg Severity deseado (en grados por 100 pies):", min_value=0.0, step=0.1)

if st.button("Calcular Pies Necesarios"):
    try:
        if 'motor_yield' in st.session_state:  # Verifica si el motor_yield está calculado
            motor_yield = st.session_state.motor_yield
            required_feet_slid = calculate_feet_to_slide(desired_dog_leg, motor_yield)
            st.success(f"Para alcanzar un Dogleg Severity de {desired_dog_leg}° por 100 pies, necesitas deslizar: {required_feet_slid:.2f} pies.")
        else:
            st.warning("Por favor, calcula primero el Motor Yield.")
    except ValueError as e:
        st.error(str(e))

# Pie de página
st.markdown("---")  # Línea separadora
st.markdown(
    """
    **Realizado por:** Diomer Algendonis (https://www.linkedin.com/in/diomer-algendonis-reyes-44395067/)  
    **Contacto:** mailto:diomer.algendonis@gmail.com
    **Repositorio GitHub:** [Ver código fuente](https://github.com/Diomer2021/Motor_Yield)
    """
)