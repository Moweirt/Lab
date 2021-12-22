import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#new code

#Alex`s new code

#sofia

@st.cache
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

lab_data = load_dataset('https://raw.githubusercontent.com/Moweirt/Lab/main/Parametrs.csv')


st.title("Интерактивная лабораторная работа по изучению затухающих колебаний и жидкого трения")
st.markdown("## Идея эксперимента\n")
st.markdown("Используется пружинный маятник, тело которого движется в вязкой среде.\n")
st.markdown("## Теория")
st.markdown("**_Уравнение колебаний._** Колебания широко распространены в природе. В общем случае под колебаниями понимают движения, в том "
            "или иной степени повторяющиеся во времени. По физической природе изменяющейся величины колебательные процессы "
            "разделяют на механические, электромагнитные, электромеханические и т.д. Особую роль в физике играют механические "
            "и электромагнитные колебания. С помощью распространяющихся колебаний плотности и давления воздуха (воспринимаемых "
            "как звук) и с помощью распространяющихся электромагнитных колебаний (свет) мы получаем большую часть информации "
            "об окружающем мире.")
st.markdown("Несмотря на различную физическую природу колебаний, все они обладают некоторой общей сущностью,"
            " которая в первую очередь определяется возможностью их единообразного математического описания.\nВсе колебания могут"
            " быть разбиты на три группы: периодические, квазипериодические и непериодические. Периодическими колебаниями "
            "мы называем те процессы, которые повторяются во времени и описываются такой функцией времени, что f(t)=f(t+T), "
            "где Т — период данного колебания. Квазипериодическими колебаниями называются такие непериодические колебания, "
            "которые в течение длительного времени сохраняют основные характеристики процесса при медленном изменении "
            "их параметров (например, амплитуды).")
st.markdown("Если уравнения, описывающие колебания, имеют вид линейных дифференциальных "
            "уравнений, колебания называются линейными. Физически это соответствуют тем случаям, когда в системе все "
            "возникающие силы можно считать линейными функциями координат и скоростей.")
st.markdown("Колебательный процесс в системе может возникнуть в двух случаях. В первом из них за счет внешней силы система выводится из состояния устойчивого"
            " равновесия, т.е. ей сообщается некоторое достаточное количество потенциальной или кинетическоэй энергии, "
            "после чего внешние силы полностью отключаются. Тогда, за счет работы внутренних сил, образующихся в ситеме, "
            "происходит переход кинетической энергии в потенциальную и наоборот. В этом случае возникают колебания, "
            "которые называются свободными или собственными колебаниями системы. Если же на систему постоянно действует "
            "внешняя сила, то возникают так называемые вынужденные колебания.")

st.markdown("## Упражнение")
st.markdown("### Изучение зависимости периода колебаний от жесткости пружины и массы груза")

par_columns = st.columns(3)
par_rig = par_columns[0].number_input("Жесткость пружины(H/m)", value=40)
par_mass = par_columns[1].number_input("Масса груза(kg)", value=0.1)
par_rad = par_columns[2].number_input("Радиус шарика(m)", value=0.01)
par2_columns = st.columns(2)
par_vis = par_columns[0].number_input("Динамическая вязкость жидкости(P/s)", value=0.9)
par_ff = par_columns[1].number_input("Частота кадров(FPS)", value=4)

m = par_mass
r = par_rad
k = par_rig
y = par_vis
s = par_ff

plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-3 , 3))
line, = ax.plot([], [], lw=1)

w0 = np.sqrt(k/m)
h = 6 * np.pi * r * y
v = h/(m*2)
w = w0/10

def init():
    line.set_data([], [])
    return line,

def animate(i):

    x = np.linspace(0, 4, 1000)

    y = np.exp(-v * x) * np.sin( 2 * np.pi * w * (x - 0.01 * i * s ) )


    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=20, blit=True)

anim.save('animation.gif', writer='pillow')

st.image("animation.gif")

# добавлено упражение(не меняю переменные)

# тут начинать писать фронтэнд по упражнению

plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-3 , 3))
line_err, = ax.plot([], [], lw=1)

k = 45  # Жесткость пружины(H/m)
m = 0.080  # Масса груза(kg)
r = 0.05  # Радиус шарика(m)
y = 0.7  # Динамическая вязкость жидкости(P/s) - берем глицерин


w0 = np.sqrt(k/m)
h = 6 * np.pi * r * y
v_err = h/(m*2)
w_err = w0/10


def init_err():
    line_err.set_data([], [])
    return line_err,

def animate_err(i):

    x = np.linspace(0, 4, 100)

    y_err = np.random.random(100)
    y = np.exp(-v_err * x) * np.sin( 2 * np.pi * w_err * (x - 0.01 ) ) + y_err


    line_err.set_data(x, y)
    return line_err,


anim = FuncAnimation(fig, animate_err, init_func=init_err,
                     frames=200, interval=20, blit=True)

anim.save('error.gif', writer='pillow')

st.image("error.gif")