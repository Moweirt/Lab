import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

@st.cache
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

lab_data = load_dataset('Parametrs.csv')

##titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
##titanic_data = load_dataset(titanic_link)

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

par_columns = st.columns(5)
par_rig = par_columns[0].number_input("Жесткость пружины", value=lab_data['Rig'].max())
par_mass = par_columns[1].number_input("Масса груза", value=lab_data['Mass'].max())
par_rad = par_columns[2].number_input("Радиус шарика", value=lab_data['Rad'].max())
par_vis = par_columns[3].number_input("Динамическая вязкость жидкости", value=lab_data['Vis'].max())
par_ff = par_columns[4].number_input("Частота кадров", value=lab_data['FF'].max())

'''
par1_columns = st.columns(2)
par_rig = par1_columns[0].number_input("Жесткость пружины", value=titanic_data['age'].min())
par_mass = par1_columns[1].number_input("Масса груза", value=titanic_data['age'].max())

par2_columns = st.columns(2)
par_rad = par2_columns[0].number_input("Радиус", value=titanic_data['age'].min())
par_vis = par2_columns[1].number_input("Динамическая вязкость жидкости", value=titanic_data['age'].max())

optionals = st.expander("Скорость анимации", True)
ff = optionals.slider(
    "Скорость",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
'''
#T = 2*np.pi*np.sqrt(par_mass/par_rig)

#m = float(input("введите массу (килограмм)"))
m = par_mass
#r = float(input("введите радиус (метр)"))
r = par_rad
#k = float(input("введите коэф жесткости пружины (ньютон/метр)"))
k = par_rig
#y = float(input("введите динамическую вязкость (паскаль/сек)"))
y = par_vis
#s = float(input("введите скорость (от 0.1 до 10)"))
s = par_ff

plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-3 , 3))
line, = ax.plot([], [], lw=1)


w0 = np.sqrt(k/m)
h = 6 * np.pi * r * y
v = h/(m*2)
w = w0/10

#if (v >=0.018): print("Декремент большой - быстрое затухание");
#if (v < 0.018): print("Декремент маленький - медленное затухание");

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

#st.write(f"Период колебаний: {T}")