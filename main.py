import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#Описание лабораторной работы(теория + картинки + формулы)

st.title("Интерактивная лабораторная работа по изучению затухающих колебаний и жидкого трения")

st.header("Идея эксперимента")
st.markdown("Изучение свойств собственных колебаний системы, представляющей собой подвешенный на пружине груз, "
            "который движется в вязкой среде. В нашем эксперименте определяется декремент затухания и коэффициент "
            "силы трения (сопротивления), действующий на груз со стороны вязкой среды.")

st.header("Теория")
st.markdown("Колебания широко распространены в природе. В общем случае **_под колебаниями понимают повторяющийся в той "
            "или иной степени во времени процесс изменения состояний системы около точки равновесия_**."
            "По физической природе колебательные процессы разделяют на механические, электромагнитные, "
            "электромеханические и т.д. Особую роль в физике играют механические и электромагнитные колебания. "
            "С помощью распространяющихся колебаний плотности и давления воздуха (воспринимаемых как звук) и с помощью "
            "распространяющихся электромагнитных колебаний (свет) мы получаем большую часть информации об окружающем мире.")

st.markdown("Несмотря на различную физическую природу колебаний, все они обладают некоторой общей сущностью, "
            "которая в первую очередь определяется возможностью их единообразного математического описания.")

st.markdown("Все колебания могут быть разбиты на три группы: периодические, квазипериодические, непериодические."
            "Периодическими колебаниями мы называем те процессы, которые повторяются во времени и описываются такой "
            "функцией времени, что **_f(t) = f(t + T)_**, где **_Т — период данного колебания_**. Квазипериодическими колебаниями "
            "называются такие непериодические колебания, которые в течение длительного времени сохраняют основные "
            "характеристики процесса при медленном изменении их параметров (например, амплитуды)")

st.markdown("Если уравнения, описывающие колебания, имеют вид линейных дифференциальных уравнений, колебания "
            "называются линейными. Физически это соответствуют тем случаям, когда в системе все возникающие силы "
            "можно считать линейными функциями координат и скоростей.")

st.markdown("Колебательный процесс в системе может возникнуть в двух случаях. В первом из них за счет внешней силы "
            "система выводится из состояния устойчивого равновесия, т.е. ей сообщается некоторое достаточное количество "
            "потенциальной или кинетической энергии, после чего внешние силы полностью отключаются. Тогда, за счет работы "
            "внутренних сил, образующихся в системе, происходит переход кинетической энергии в потенциальную и наоборот. "
            "В этом случае возникают колебания, которые называются свободными или собственными колебаниями системы. "
            "Если же на систему постоянно действует внешняя сила, то возникают так называемые вынужденные колебания")

st.markdown("Если физическая величина **_x(t)_** изменяется со временем по гармоническому закону, то колебания "
            "называются гармоническими. Формула гармонических колебаний:")

st.latex("х(t) = A cos(ω_0t + φ_0)")

st.markdown("Здесь **_A_** — амплитуда колебаний; **_ω0_** — круговая частота; **_t_** — время; **_φ0_** — начальная фаза колебаний.")

st.markdown("Круговая частота **_ω0_** связана с периодом:")

st.latex("ω_0 = 2π/T")

st.markdown("Функция **_х(t)_** представляет из себя решение дифференциального уравнения")

st.latex("d^2x/dt^2 + ω_0^2x = 0")

st.markdown("которое называется уравнением свободных колебаний.")

st.markdown("Физическую систему, выведенную из состояния равновесия и представленную самой себе, в которой изменение "
            "одного из параметров х описывается дифференциальным уравнением ")

st.latex("d^2x/dt^2 + ω_0^2x = 0")

st.markdown("называют классическим гармоническим осциллятором. ")

st.markdown("Действие классического гармонического осциллятора на примере пружинного маятника показано ниже. На нашем "
            "графике можно изменять следующие параметры: **_M_** – динамическая вязкость жидкости, **_m_** – масса маятника, "
            "**_r_** - радиус маятника и **_k_** – коэффициент жесткости пружины. Стоит так же отметить, что в нашей "
            "модели следующие начальные условия: **_t = 0_**, **_v0 = 0_**, **_х0 = A_**.")

st.header("Собственные колебания пружинного маятника")

st.markdown("Пружинный маятник состоит из тела массы **_m_** и легкой пружины с коэффициентом жесткости **_k_**. В общем случае "
            "движение пружинного маятника в поле силы тяжести довольно сложно и описывается большим числом степеней "
            "свободы. ")

st.markdown("Практический интерес, однако, представляют колебания с одной степенью свободы, когда движение маятника "
            "происходит вдоль вертикальной оси. Для того, чтобы маятник совершал только вертикальные колебания "
            "достаточно оттянуть тело строго вниз на небольшую величину. Для полного описания колебаний в этом "
            "случае необходимо знать поведение только одной переменной, например, вертикальной координаты центра "
            "масс тела маятника.")

st.markdown("На тело, подвешенное на пружине в поле силы тяжести действуют две силы (без учета сил трения) сила "
            "тяготения и упругая сила. Начало координат выберем таким образом, чтобы при х=0 масса m находилась "
            "в равновесии. При этом сила тяжести mg будет скомпенсирована некоторым начальным растяжением пружины "
            "и в дальнейшем рассмотрении участвовать не будет.")

st.markdown("При отклонении тела от точки равновесия будет возникать возвращающая сила **_F(х)_**. Рассмотрим малые "
            "колебания пружинного маятника. Колебания пружинного маятника называют малыми, если сила, возникающая "
            "при смещении грузика от положения равновесия, пропорциональна его смещению и направлена в сторону "
            "положения равновесия. Для пружинного маятника условия малости колебаний удовлетворяются при смещениях, "
            "создающих возвращающую силу у пружины в пределах применимости закона Гука. Уравнение движения пружинного "
            "маятника при этом имеет вид:")

st.latex("m*d^2x/dt^2 = -kx , ω_0 = \sqrt{k/m} , ω_0 = 2π/T = 2π\sqrt{m/k}.")

st.header("Затухающие колебания")

st.markdown("В реальных осцилляторах, за счет сил трения, происходит рассеяние (диссипация) запасенной энергии, "
            "в результате чего свободные колебания со временем затухают. При движении тела пружинного маятника в "
            "вязкой среде с небольшими скоростями, сила трения пропорциональна скорости.")

st.markdown("Пусть на пружинный маятник (систему) кроме силы трения")

st.latex("F = -rV ,")

st.markdown("где r – коэффициент сопротивления, V – скорость системы, действует ещё сила упругости. Тогда уравнение "
            "движения груза пружинного маятника на основании II закона Ньютона имеет вид ")

st.latex("ma = -kx -rV, (1)")

st.markdown("Разделив (1) на m и введя обозначения")

st.latex("β = r/2m")

st.markdown("коэффициент затухания,")

st.latex("ω_0 = \sqrt{k/m}")

st.markdown("циклическая частота собственных колебаний маятника, получим дифференциальное уравнение затухающих колебаний")

st.latex("a + 2βV + ω_0^2x = 0, (2).")

st.markdown("Решение уравнения (2) может быть найдено в виде:")

st.latex("x = A_0e^{-βt}cos(ωt + φ_0), (3)")

st.markdown("где")

st.latex("ω = \sqrt{ω_0^2 - β^2}")

st.markdown("частота затухающих колебаний,")

st.latex("A = A_0e^{-βt}, (4)")

st.markdown("амплитуда затухающих колебаний.")

st.markdown("График затухающих колебаний (рис.1) имеет вид:")

st.image("ris1.png")

st.markdown("График амплитуды затухающих колебаний(рис.2):")

st.image("ris2.png")

st.markdown("Частота и период затухающих колебаний пружинного маятника:")

st.latex("ω = \sqrt{k/m - r^2/4m^2}, (5)")

st.latex("T = 2π/\sqrt{k/m - r^2/4m^2}, (6)")

st.markdown("Время, за которое амплитуда затухающих колебаний уменьшается в e раз, называется временем релаксации τ. "
            "Время релаксации τ связано с коэффициентом затухания β соотношением")

st.latex("β = 1/τ, (7)")

st.markdown("β - характеризует быстроту затухания колебаний.")

st.markdown("Логарифм отношения амплитуды A1(t) затухающих колебаний в момент времени t к амплитуде A2(t+T) "
            "колебаний через время, равное периоду T называется логарифмическим декрементом затухания.")

st.latex("δ = ln A_1(t)/A_2(t+T) = ln A_0e^{-βt}/A_0e^{-β(t+T)} = βT = r/2m * 2π/\sqrt{k/m - r^2/4m^2}, (8) ")

st.markdown("При очень больших коэффициентах сопротивления r (когда k/m << r2/4m2), несмотря на наличие сил, "
            "возвращающих систему в положение равновесия, колебания не возникает. Система возвращается в положение "
            "равновесия асимптотически (не переходя положения равновесия). Такое движение называется апериодическим. "
            "На рис. 1 показан характер колебаний при различных декрементах затухания.")

st.markdown("Определив на опыте две последующие амплитуды An и An+1 и зная массу колеблющейся системы m и период "
            "затухающих колебаний Т, можно вычислить коэффициент сопротивления среды по формуле:")

st.latex("r = 2mδ/T = 2m/T * ln A_n/A_{n+1}, (9).")

st.markdown("За время релаксации система совершает количество колебаний N = t/T. С учетом этого и (7) "
            "логарифмический декремент затухания")

st.latex("δ = βT = βτ/N = 1/N,")

st.markdown("т.е. логарифмический декремент затухания есть величина, обратная числу колебаний, совершаемых системой за "
            "время, в течение которого амплитуда колебаний убывает в e раз.")

st.markdown("Затухание колебаний по экспоненциальному закону происходит в том случае, когда сила трения пропорциональна "
            "скорости. При этом отношение двух последовательных амплитуд (декремент затухания) остается постоянным. "
            "При других типах сил трения закон затухания будет иным. Во многих колебательных системах наряду с трением, "
            "пропорциональным скорости, присутствует и сухое трение. Поэтому на опыте часто получается, что отношение "
            "двух последовательных амплитуд не является постоянной величиной.")

st.header("Затухающие колебания на практике")

st.markdown("В жизни можно часто увидеть примеры затухающих колебаний. На практике возникает потребность как в "
            "уменьшении, так и в увеличении затухания колебаний.")

st.markdown("Например, при конструировании часовых механизмов стремятся уменьшить затухание колебаний балансира часов. "
            "Для этого ось балансира снабжают острыми наконечниками, которые упираются в хорошо отполированные "
            "конические подпятники, выполненные из твердого камня (агата или рубина). ")

st.image("balance.jpg")

st.markdown("Наоборот, во многих измерительных приборах очень желательно, чтобы подвижная часть устройства "
            "устанавливалась в процессе измерений быстро, не совершая большого числа колебаний. Для увеличения "
            "затухания в этом случае применяют различные демпферы – устройства, увеличивающие трение и, в общем случае, "
            "потерю энергии.")

st.markdown("Примеры затухающих колебаний в жизни:")

st.markdown("Колебания, производимые детьми, сидящими на весенних лошадях в парке, — это то, что мы наблюдаем регулярно. "
            "Как только лошадь будет возвращена и освобождена, можно наблюдать, как ребенок, сидящий на лошади, "
            "движется вперед и назад, что эквивалентно совершению колебаний. В конце концов, он замедляется и, "
            "наконец, полностью останавливается, что есть не что иное, как гашение колебаний пружинной лошади.")

st.image("horse.jpg")

st.markdown("Когда человек спрыгивает с моста или платформы, длинная эластичная веревка привязана к лодыжкам человека, "
            "что вызывает серию вертикальных колебаний на мосту или платформе. Эти вертикальные колебания будут "
            "продолжаться до тех пор, пока у упругой веревки есть энергия. И, как только он использует всю свою "
            "энергию, он вызывает гашение колебаний.")

st.image("jump.jpg")

st.markdown("Когда человек стоит на трамплине, готовый прыгнуть в бассейн, трамплин наклоняется вниз. "
            "Изгиб платы указывает на то, что энергия накапливается в самой плате. Когда человек прыгает "
            "с трамплина, он взлетает ввысь, прежде чем нырнут в воду. После этого мы видим, что трамплин все "
            "еще немного колеблется после взлета. Демпфирующие колебания — это явление, при котором запасенная "
            "в трамплине энергия постепенно уменьшается и в конечном итоге прекращается, что демонстрирует трамплин.")

st.image("water.jpg")

st.markdown("Есть так много струнных инструментов, по которым мы хорошо знакомы с гитарой и скрипкой. Когда мы дергаем "
            "струну гитары или натираем смычком струну скрипки, мы слышим мелодичные звуки. Этот звук возникает из-за "
            "колебаний струны соответствующего инструмента вверх и вниз. По прошествии некоторого времени обнаруживается,"
            " что струны перестают вибрировать, демонстрируя явление затухания колебаний.")

st.image("skr.jpg")

#Предлагаем пользователю проверить, как усвоился материал

#Упражнение1

st.subheader("Упражнение №1")
st.markdown(" **_ЗАДАНИЕ_**: Меняя один из параметров системы и изучая изменения графика, определите, как они влияют на её харатеристики")

# Создаем кнопки для изменения параметров и считываем их показатели

par1_columns = st.columns(2)
par_rig = par1_columns[0].number_input("Жесткость пружины(H/m)", value=40)
par_mass = par1_columns[1].number_input("Масса груза(kg)", value=0.1)

par2_columns = st.columns(2)
par_rad = par2_columns[0].number_input("Радиус шарика(m)", value=0.01)
par_vis = par2_columns[1].number_input("Динамическая вязкость жидкости(P/s)", value=0.9)

st.info("Для удобства вы также можете изменить частоту кадров анимации")

par3_columns = st.columns(1)
par_ff = par3_columns[0].number_input("Частота кадров(FPS)", value=4)

m = par_mass
r = par_rad
k = par_rig
y = par_vis
s = par_ff

#Строим измененный график по считанным показателям

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

#Проверяем как пользователь определил закономерности

st.markdown("##### Укажите, как изменяются характеристики системы при увеличении параметра:")
ch_mass = st.multiselect("Влияние массы на систему", ["Увеличивает период", "Уменьшает период", "Не влияет на период", "Увеличивает амплитуду", "Уменьшает амплитуду", "Не влияет на амплитуду"])
ch_rad = st.multiselect("Влияние радиуса шарика на систему", ["Увеличивает период", "Уменьшает период", "Не влияет на период", "Увеличивает амплитуду", "Уменьшает амплитуду", "Не влияет на амплитуду"])
ch_rig = st.multiselect("Влияние жесткости пружины на систему", ["Увеличивает период", "Уменьшает период", "Не влияет на период", "Увеличивает амплитуду", "Уменьшает амплитуду", "Не влияет на амплитуду"])
ch_vis = st.multiselect("Влияние динамической вязкости жидкости на систему", ["Увеличивает период", "Уменьшает период", "Не влияет на период", "Увеличивает амплитуду", "Уменьшает амплитуду", "Не влияет на амплитуду"])

resp = 0

for i in ch_mass:
    if (i == "Увеличивает период" or i == "Не влияет на амплитуду"): resp += 1
for i in ch_rad:
    if (i == "Не влияет на период" or i == "Уменьшает амплитуду"): resp += 1
for i in ch_rig:
    if (i == "Уменьшает период" or i == "Не влияет на амплитуду"): resp += 1
for i in ch_vis:
    if (i == "Не влияет на период" or i == "Уменьшает амплитуду"): resp += 1
if (resp > 0 and resp <= 3):
    st.error(f"Есть ошибки (+ {resp/2} балл(а))")
elif(resp >= 4 and resp < 7):
    st.warning(f"Вы неплохо справились (+ {resp/2} балла)")
elif (resp == 7):
    st.success(f"Почти всё верно! Отлично!(+ {resp/2} балла)")
elif (resp == 8):
    st.success(f"Абсолютно верно! Вы молодец!(+ {resp/2} балла)")