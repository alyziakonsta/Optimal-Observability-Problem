from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')
pi6 = Real('pi6')
pi7 = Real('pi7')
pi8 = Real('pi8')
pi9 = Real('pi9')
pi10 = Real('pi10')
pi11 = Real('pi11')
pi12 = Real('pi12')
pi13 = Real('pi13')
pi14 = Real('pi14')
pi15 = Real('pi15')
pi16 = Real('pi16')
pi17 = Real('pi17')
pi18 = Real('pi18')
pi19 = Real('pi19')
pi20 = Real('pi20')
pi21 = Real('pi21')
pi22 = Real('pi22')
pi23 = Real('pi23')
pi24 = Real('pi24')
pi25 = Real('pi25')
pi26 = Real('pi26')
pi27 = Real('pi27')
pi28 = Real('pi28')
pi29 = Real('pi29')
pi30 = Real('pi30')
pi31 = Real('pi31')
pi32 = Real('pi32')
pi33 = Real('pi33')
pi34 = Real('pi34')
pi35 = Real('pi35')
pi36 = Real('pi36')
pi37 = Real('pi37')
pi38 = Real('pi38')
pi39 = Real('pi39')
pi40 = Real('pi40')
pi41 = Real('pi41')
pi42 = Real('pi42')
pi43 = Real('pi43')
pi44 = Real('pi44')
pi45 = Real('pi45')
pi46 = Real('pi46')
pi47 = Real('pi47')
pi48 = Real('pi48')

# Choice of observations
y0 = Real('y0')
y1 = Real('y1')
y2 = Real('y2')
y3 = Real('y3')
y4 = Real('y4')
y5 = Real('y5')
y6 = Real('y6')
y7 = Real('y7')
y8 = Real('y8')
y9 = Real('y9')
y10 = Real('y10')
y11 = Real('y11')
y12 = Real('y12')
y13 = Real('y13')
y14 = Real('y14')
y15 = Real('y15')
y16 = Real('y16')
y17 = Real('y17')
y18 = Real('y18')
y19 = Real('y19')
y20 = Real('y20')
y21 = Real('y21')
y22 = Real('y22')
y23 = Real('y23')
y24 = Real('y24')
y25 = Real('y25')
y26 = Real('y26')
y27 = Real('y27')
y28 = Real('y28')
y29 = Real('y29')
y30 = Real('y30')
y31 = Real('y31')
y32 = Real('y32')
y33 = Real('y33')
y34 = Real('y34')
y35 = Real('y35')
y36 = Real('y36')
y37 = Real('y37')
y38 = Real('y38')
y39 = Real('y39')
y40 = Real('y40')
y41 = Real('y41')
y42 = Real('y42')
y43 = Real('y43')
y44 = Real('y44')
y45 = Real('y45')
y46 = Real('y46')
y47 = Real('y47')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo0u = Real('xo0u')
xo0d = Real('xo0d')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo2u = Real('xo2u')
xo2d = Real('xo2d')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo3u = Real('xo3u')
xo3d = Real('xo3d')
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xo4u = Real('xo4u')
xo4d = Real('xo4d')
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo5u = Real('xo5u')
xo5d = Real('xo5d')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xo6u = Real('xo6u')
xo6d = Real('xo6d')
xo7l = Real('xo7l')
xo7r = Real('xo7r')
xo7u = Real('xo7u')
xo7d = Real('xo7d')
xo8l = Real('xo8l')
xo8r = Real('xo8r')
xo8u = Real('xo8u')
xo8d = Real('xo8d')
xo9l = Real('xo9l')
xo9r = Real('xo9r')
xo9u = Real('xo9u')
xo9d = Real('xo9d')
xo10l = Real('xo10l')
xo10r = Real('xo10r')
xo10u = Real('xo10u')
xo10d = Real('xo10d')
xo11l = Real('xo11l')
xo11r = Real('xo11r')
xo11u = Real('xo11u')
xo11d = Real('xo11d')
xo12l = Real('xo12l')
xo12r = Real('xo12r')
xo12u = Real('xo12u')
xo12d = Real('xo12d')
xo13l = Real('xo13l')
xo13r = Real('xo13r')
xo13u = Real('xo13u')
xo13d = Real('xo13d')
xo14l = Real('xo14l')
xo14r = Real('xo14r')
xo14u = Real('xo14u')
xo14d = Real('xo14d')
xo15l = Real('xo15l')
xo15r = Real('xo15r')
xo15u = Real('xo15u')
xo15d = Real('xo15d')
xo16l = Real('xo16l')
xo16r = Real('xo16r')
xo16u = Real('xo16u')
xo16d = Real('xo16d')
xo17l = Real('xo17l')
xo17r = Real('xo17r')
xo17u = Real('xo17u')
xo17d = Real('xo17d')
xo18l = Real('xo18l')
xo18r = Real('xo18r')
xo18u = Real('xo18u')
xo18d = Real('xo18d')
xo19l = Real('xo19l')
xo19r = Real('xo19r')
xo19u = Real('xo19u')
xo19d = Real('xo19d')
xo20l = Real('xo20l')
xo20r = Real('xo20r')
xo20u = Real('xo20u')
xo20d = Real('xo20d')
xo21l = Real('xo21l')
xo21r = Real('xo21r')
xo21u = Real('xo21u')
xo21d = Real('xo21d')
xo22l = Real('xo22l')
xo22r = Real('xo22r')
xo22u = Real('xo22u')
xo22d = Real('xo22d')
xo23l = Real('xo23l')
xo23r = Real('xo23r')
xo23u = Real('xo23u')
xo23d = Real('xo23d')
xo24l = Real('xo24l')
xo24r = Real('xo24r')
xo24u = Real('xo24u')
xo24d = Real('xo24d')
xo25l = Real('xo25l')
xo25r = Real('xo25r')
xo25u = Real('xo25u')
xo25d = Real('xo25d')
xo26l = Real('xo26l')
xo26r = Real('xo26r')
xo26u = Real('xo26u')
xo26d = Real('xo26d')
xo27l = Real('xo27l')
xo27r = Real('xo27r')
xo27u = Real('xo27u')
xo27d = Real('xo27d')
xo28l = Real('xo28l')
xo28r = Real('xo28r')
xo28u = Real('xo28u')
xo28d = Real('xo28d')
xo29l = Real('xo29l')
xo29r = Real('xo29r')
xo29u = Real('xo29u')
xo29d = Real('xo29d')
xo30l = Real('xo30l')
xo30r = Real('xo30r')
xo30u = Real('xo30u')
xo30d = Real('xo30d')
xo31l = Real('xo31l')
xo31r = Real('xo31r')
xo31u = Real('xo31u')
xo31d = Real('xo31d')
xo32l = Real('xo32l')
xo32r = Real('xo32r')
xo32u = Real('xo32u')
xo32d = Real('xo32d')
xo33l = Real('xo33l')
xo33r = Real('xo33r')
xo33u = Real('xo33u')
xo33d = Real('xo33d')
xo34l = Real('xo34l')
xo34r = Real('xo34r')
xo34u = Real('xo34u')
xo34d = Real('xo34d')
xo35l = Real('xo35l')
xo35r = Real('xo35r')
xo35u = Real('xo35u')
xo35d = Real('xo35d')
xo36l = Real('xo36l')
xo36r = Real('xo36r')
xo36u = Real('xo36u')
xo36d = Real('xo36d')
xo37l = Real('xo37l')
xo37r = Real('xo37r')
xo37u = Real('xo37u')
xo37d = Real('xo37d')
xo38l = Real('xo38l')
xo38r = Real('xo38r')
xo38u = Real('xo38u')
xo38d = Real('xo38d')
xo39l = Real('xo39l')
xo39r = Real('xo39r')
xo39u = Real('xo39u')
xo39d = Real('xo39d')
xo40l = Real('xo40l')
xo40r = Real('xo40r')
xo40u = Real('xo40u')
xo40d = Real('xo40d')
xo41l = Real('xo41l')
xo41r = Real('xo41r')
xo41u = Real('xo41u')
xo41d = Real('xo41d')
xo42l = Real('xo42l')
xo42r = Real('xo42r')
xo42u = Real('xo42u')
xo42d = Real('xo42d')
xo43l = Real('xo43l')
xo43r = Real('xo43r')
xo43u = Real('xo43u')
xo43d = Real('xo43d')
xo44l = Real('xo44l')
xo44r = Real('xo44r')
xo44u = Real('xo44u')
xo44d = Real('xo44d')
xo45l = Real('xo45l')
xo45r = Real('xo45r')
xo45u = Real('xo45u')
xo45d = Real('xo45d')
xo46l = Real('xo46l')
xo46r = Real('xo46r')
xo46u = Real('xo46u')
xo46d = Real('xo46d')
xo47l = Real('xo47l')
xo47r = Real('xo47r')
xo47u = Real('xo47u')
xo47d = Real('xo47d')
xol = Real('xol')
xor = Real('xor')
xod = Real('xod')
xou = Real('xou')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=12, pi1>=11, pi2>=10, pi3>=9, pi4>=8, pi5>=7, pi6>=6, pi7>=11, pi8>=10, pi9>=9, pi10>=8, pi11>=7, pi12>=6, pi13>=5, pi14>=10, pi15>=9, pi16>=8, pi17>=7, pi18>=6, pi19>=5, pi20>=4, pi21>=9, pi22>=8, pi23>=7, pi24>=6, pi25>=5, pi26>=4, pi27>=3, pi28>=8, pi29>=7, pi30>=6, pi31>=5, pi32>=4, pi33>=3, pi34>=2, pi35>=7, pi36>=6, pi37>=5, pi38>=4, pi39>=3, pi40>=2, pi41>=1, pi42>=6, pi43>=5, pi44>=4, pi45>=3, pi46>=2, pi47>=1, pi48>=0, # Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1) + ((1 - y0)*xou + y0*xo0u) * (1 + pi0) + ((1 - y0)*xod + y0*xo0d) * (1 + pi7),
 pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2) + ((1 - y1)*xou + y1*xo1u) * (1 + pi1) + ((1 - y1)*xod + y1*xo1d) * (1 + pi8),
 pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3) + ((1 - y2)*xou + y2*xo2u) * (1 + pi2) + ((1 - y2)*xod + y2*xo2d) * (1 + pi9),
 pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4) + ((1 - y3)*xou + y3*xo3u) * (1 + pi3) + ((1 - y3)*xod + y3*xo3d) * (1 + pi10),
 pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi5) + ((1 - y4)*xou + y4*xo4u) * (1 + pi4) + ((1 - y4)*xod + y4*xo4d) * (1 + pi11),
 pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6) + ((1 - y5)*xou + y5*xo5u) * (1 + pi5) + ((1 - y5)*xod + y5*xo5d) * (1 + pi12),
 pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7) + ((1 - y6)*xou + y6*xo6u) * (1 + pi6) + ((1 - y6)*xod + y6*xo6d) * (1 + pi13),
 pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8) + ((1 - y7)*xou + y7*xo7u) * (1 + pi0) + ((1 - y7)*xod + y7*xo7d) * (1 + pi14),
 pi8== ((1 - y8)*xol + y8*xo8l) * (1 + pi7) + ((1 - y8)*xor + y8*xo8r) * (1 + pi9) + ((1 - y8)*xou + y8*xo8u) * (1 + pi1) + ((1 - y8)*xod + y8*xo8d) * (1 + pi15),
 pi9== ((1 - y9)*xol + y9*xo9l) * (1 + pi8) + ((1 - y9)*xor + y9*xo9r) * (1 + pi10) + ((1 - y9)*xou + y9*xo9u) * (1 + pi2) + ((1 - y9)*xod + y9*xo9d) * (1 + pi16),
 pi10== ((1 - y10)*xol + y10*xo10l) * (1 + pi9) + ((1 - y10)*xor + y10*xo10r) * (1 + pi11) + ((1 - y10)*xou + y10*xo10u) * (1 + pi3) + ((1 - y10)*xod + y10*xo10d) * (1 + pi17),
 pi11== ((1 - y11)*xol + y11*xo11l) * (1 + pi10) + ((1 - y11)*xor + y11*xo11r) * (1 + pi12) + ((1 - y11)*xou + y11*xo11u) * (1 + pi4) + ((1 - y11)*xod + y11*xo11d) * (1 + pi18),
 pi12== ((1 - y12)*xol + y12*xo12l) * (1 + pi11) + ((1 - y12)*xor + y12*xo12r) * (1 + pi13) + ((1 - y12)*xou + y12*xo12u) * (1 + pi5) + ((1 - y12)*xod + y12*xo12d) * (1 + pi19),
 pi13== ((1 - y13)*xol + y13*xo13l) * (1 + pi12) + ((1 - y13)*xor + y13*xo13r) * (1 + pi14) + ((1 - y13)*xou + y13*xo13u) * (1 + pi6) + ((1 - y13)*xod + y13*xo13d) * (1 + pi20),
 pi14== ((1 - y14)*xol + y14*xo14l) * (1 + pi13) + ((1 - y14)*xor + y14*xo14r) * (1 + pi15) + ((1 - y14)*xou + y14*xo14u) * (1 + pi7) + ((1 - y14)*xod + y14*xo14d) * (1 + pi21),
 pi15== ((1 - y15)*xol + y15*xo15l) * (1 + pi14) + ((1 - y15)*xor + y15*xo15r) * (1 + pi16) + ((1 - y15)*xou + y15*xo15u) * (1 + pi8) + ((1 - y15)*xod + y15*xo15d) * (1 + pi22),
 pi16== ((1 - y16)*xol + y16*xo16l) * (1 + pi15) + ((1 - y16)*xor + y16*xo16r) * (1 + pi17) + ((1 - y16)*xou + y16*xo16u) * (1 + pi9) + ((1 - y16)*xod + y16*xo16d) * (1 + pi23),
 pi17== ((1 - y17)*xol + y17*xo17l) * (1 + pi16) + ((1 - y17)*xor + y17*xo17r) * (1 + pi18) + ((1 - y17)*xou + y17*xo17u) * (1 + pi10) + ((1 - y17)*xod + y17*xo17d) * (1 + pi24),
 pi18== ((1 - y18)*xol + y18*xo18l) * (1 + pi17) + ((1 - y18)*xor + y18*xo18r) * (1 + pi19) + ((1 - y18)*xou + y18*xo18u) * (1 + pi11) + ((1 - y18)*xod + y18*xo18d) * (1 + pi25),
 pi19== ((1 - y19)*xol + y19*xo19l) * (1 + pi18) + ((1 - y19)*xor + y19*xo19r) * (1 + pi20) + ((1 - y19)*xou + y19*xo19u) * (1 + pi12) + ((1 - y19)*xod + y19*xo19d) * (1 + pi26),
 pi20== ((1 - y20)*xol + y20*xo20l) * (1 + pi19) + ((1 - y20)*xor + y20*xo20r) * (1 + pi21) + ((1 - y20)*xou + y20*xo20u) * (1 + pi13) + ((1 - y20)*xod + y20*xo20d) * (1 + pi27),
 pi21== ((1 - y21)*xol + y21*xo21l) * (1 + pi20) + ((1 - y21)*xor + y21*xo21r) * (1 + pi22) + ((1 - y21)*xou + y21*xo21u) * (1 + pi14) + ((1 - y21)*xod + y21*xo21d) * (1 + pi28),
 pi22== ((1 - y22)*xol + y22*xo22l) * (1 + pi21) + ((1 - y22)*xor + y22*xo22r) * (1 + pi23) + ((1 - y22)*xou + y22*xo22u) * (1 + pi15) + ((1 - y22)*xod + y22*xo22d) * (1 + pi29),
 pi23== ((1 - y23)*xol + y23*xo23l) * (1 + pi22) + ((1 - y23)*xor + y23*xo23r) * (1 + pi24) + ((1 - y23)*xou + y23*xo23u) * (1 + pi16) + ((1 - y23)*xod + y23*xo23d) * (1 + pi30),
 pi24== ((1 - y24)*xol + y24*xo24l) * (1 + pi23) + ((1 - y24)*xor + y24*xo24r) * (1 + pi25) + ((1 - y24)*xou + y24*xo24u) * (1 + pi17) + ((1 - y24)*xod + y24*xo24d) * (1 + pi31),
 pi25== ((1 - y25)*xol + y25*xo25l) * (1 + pi24) + ((1 - y25)*xor + y25*xo25r) * (1 + pi26) + ((1 - y25)*xou + y25*xo25u) * (1 + pi18) + ((1 - y25)*xod + y25*xo25d) * (1 + pi32),
 pi26== ((1 - y26)*xol + y26*xo26l) * (1 + pi25) + ((1 - y26)*xor + y26*xo26r) * (1 + pi27) + ((1 - y26)*xou + y26*xo26u) * (1 + pi19) + ((1 - y26)*xod + y26*xo26d) * (1 + pi33),
 pi27== ((1 - y27)*xol + y27*xo27l) * (1 + pi26) + ((1 - y27)*xor + y27*xo27r) * (1 + pi28) + ((1 - y27)*xou + y27*xo27u) * (1 + pi20) + ((1 - y27)*xod + y27*xo27d) * (1 + pi34),
 pi28== ((1 - y28)*xol + y28*xo28l) * (1 + pi27) + ((1 - y28)*xor + y28*xo28r) * (1 + pi29) + ((1 - y28)*xou + y28*xo28u) * (1 + pi21) + ((1 - y28)*xod + y28*xo28d) * (1 + pi35),
 pi29== ((1 - y29)*xol + y29*xo29l) * (1 + pi28) + ((1 - y29)*xor + y29*xo29r) * (1 + pi30) + ((1 - y29)*xou + y29*xo29u) * (1 + pi22) + ((1 - y29)*xod + y29*xo29d) * (1 + pi36),
 pi30== ((1 - y30)*xol + y30*xo30l) * (1 + pi29) + ((1 - y30)*xor + y30*xo30r) * (1 + pi31) + ((1 - y30)*xou + y30*xo30u) * (1 + pi23) + ((1 - y30)*xod + y30*xo30d) * (1 + pi37),
 pi31== ((1 - y31)*xol + y31*xo31l) * (1 + pi30) + ((1 - y31)*xor + y31*xo31r) * (1 + pi32) + ((1 - y31)*xou + y31*xo31u) * (1 + pi24) + ((1 - y31)*xod + y31*xo31d) * (1 + pi38),
 pi32== ((1 - y32)*xol + y32*xo32l) * (1 + pi31) + ((1 - y32)*xor + y32*xo32r) * (1 + pi33) + ((1 - y32)*xou + y32*xo32u) * (1 + pi25) + ((1 - y32)*xod + y32*xo32d) * (1 + pi39),
 pi33== ((1 - y33)*xol + y33*xo33l) * (1 + pi32) + ((1 - y33)*xor + y33*xo33r) * (1 + pi34) + ((1 - y33)*xou + y33*xo33u) * (1 + pi26) + ((1 - y33)*xod + y33*xo33d) * (1 + pi40),
 pi34== ((1 - y34)*xol + y34*xo34l) * (1 + pi33) + ((1 - y34)*xor + y34*xo34r) * (1 + pi35) + ((1 - y34)*xou + y34*xo34u) * (1 + pi27) + ((1 - y34)*xod + y34*xo34d) * (1 + pi41),
 pi35== ((1 - y35)*xol + y35*xo35l) * (1 + pi34) + ((1 - y35)*xor + y35*xo35r) * (1 + pi36) + ((1 - y35)*xou + y35*xo35u) * (1 + pi28) + ((1 - y35)*xod + y35*xo35d) * (1 + pi42),
 pi36== ((1 - y36)*xol + y36*xo36l) * (1 + pi35) + ((1 - y36)*xor + y36*xo36r) * (1 + pi37) + ((1 - y36)*xou + y36*xo36u) * (1 + pi29) + ((1 - y36)*xod + y36*xo36d) * (1 + pi43),
 pi37== ((1 - y37)*xol + y37*xo37l) * (1 + pi36) + ((1 - y37)*xor + y37*xo37r) * (1 + pi38) + ((1 - y37)*xou + y37*xo37u) * (1 + pi30) + ((1 - y37)*xod + y37*xo37d) * (1 + pi44),
 pi38== ((1 - y38)*xol + y38*xo38l) * (1 + pi37) + ((1 - y38)*xor + y38*xo38r) * (1 + pi39) + ((1 - y38)*xou + y38*xo38u) * (1 + pi31) + ((1 - y38)*xod + y38*xo38d) * (1 + pi45),
 pi39== ((1 - y39)*xol + y39*xo39l) * (1 + pi38) + ((1 - y39)*xor + y39*xo39r) * (1 + pi40) + ((1 - y39)*xou + y39*xo39u) * (1 + pi32) + ((1 - y39)*xod + y39*xo39d) * (1 + pi46),
 pi40== ((1 - y40)*xol + y40*xo40l) * (1 + pi39) + ((1 - y40)*xor + y40*xo40r) * (1 + pi41) + ((1 - y40)*xou + y40*xo40u) * (1 + pi33) + ((1 - y40)*xod + y40*xo40d) * (1 + pi47),
 pi41== ((1 - y41)*xol + y41*xo41l) * (1 + pi40) + ((1 - y41)*xor + y41*xo41r) * (1 + pi42) + ((1 - y41)*xou + y41*xo41u) * (1 + pi34) + ((1 - y41)*xod + y41*xo41d) * (1 + pi48),
 pi42== ((1 - y42)*xol + y42*xo42l) * (1 + pi41) + ((1 - y42)*xor + y42*xo42r) * (1 + pi43) + ((1 - y42)*xou + y42*xo42u) * (1 + pi35) + ((1 - y42)*xod + y42*xo42d) * (1 + pi42), 
pi43== ((1 - y43)*xol + y43*xo43l) * (1 + pi42) + ((1 - y43)*xor + y43*xo43r) * (1 + pi44) + ((1 - y43)*xou + y43*xo43u) * (1 + pi36) + ((1 - y43)*xod + y43*xo43d) * (1 + pi43), 
pi44== ((1 - y44)*xol + y44*xo44l) * (1 + pi43) + ((1 - y44)*xor + y44*xo44r) * (1 + pi45) + ((1 - y44)*xou + y44*xo44u) * (1 + pi37) + ((1 - y44)*xod + y44*xo44d) * (1 + pi44), 
pi45== ((1 - y45)*xol + y45*xo45l) * (1 + pi44) + ((1 - y45)*xor + y45*xo45r) * (1 + pi46) + ((1 - y45)*xou + y45*xo45u) * (1 + pi38) + ((1 - y45)*xod + y45*xo45d) * (1 + pi45), 
pi46== ((1 - y46)*xol + y46*xo46l) * (1 + pi45) + ((1 - y46)*xor + y46*xo46r) * (1 + pi47) + ((1 - y46)*xou + y46*xo46u) * (1 + pi39) + ((1 - y46)*xod + y46*xo46d) * (1 + pi46), 
pi47== ((1 - y47)*xol + y47*xo47l) * (1 + pi46) + ((1 - y47)*xor + y47*xo47r) * (1 + pi48) + ((1 - y47)*xou + y47*xo47u) * (1 + pi40) + ((1 - y47)*xod + y47*xo47d) * (1 + pi47), 
pi48 == 0, 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(147,24)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47) * Q(1,48) <= Q(147,24),
# Randomised strategies (proper probability distributions)
xo0l <= 1,
xo0l >= 0,
xo0r <= 1,
xo0r >= 0,
xo0u <= 1,
xo0u >= 0,
xo0d <= 1,
xo0d >= 0,
xo0l + xo0r + xo0u + xo0d == 1,
xo1l <= 1,
xo1l >= 0,
xo1r <= 1,
xo1r >= 0,
xo1u <= 1,
xo1u >= 0,
xo1d <= 1,
xo1d >= 0,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l <= 1,
xo2l >= 0,
xo2r <= 1,
xo2r >= 0,
xo2u <= 1,
xo2u >= 0,
xo2d <= 1,
xo2d >= 0,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l <= 1,
xo3l >= 0,
xo3r <= 1,
xo3r >= 0,
xo3u <= 1,
xo3u >= 0,
xo3d <= 1,
xo3d >= 0,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l <= 1,
xo4l >= 0,
xo4r <= 1,
xo4r >= 0,
xo4u <= 1,
xo4u >= 0,
xo4d <= 1,
xo4d >= 0,
xo4l + xo4r + xo4u + xo4d == 1,
xo5l <= 1,
xo5l >= 0,
xo5r <= 1,
xo5r >= 0,
xo5u <= 1,
xo5u >= 0,
xo5d <= 1,
xo5d >= 0,
xo5l + xo5r + xo5u + xo5d == 1,
xo6l <= 1,
xo6l >= 0,
xo6r <= 1,
xo6r >= 0,
xo6u <= 1,
xo6u >= 0,
xo6d <= 1,
xo6d >= 0,
xo6l + xo6r + xo6u + xo6d == 1,
xo7l <= 1,
xo7l >= 0,
xo7r <= 1,
xo7r >= 0,
xo7u <= 1,
xo7u >= 0,
xo7d <= 1,
xo7d >= 0,
xo7l + xo7r + xo7u + xo7d == 1,
xo8l <= 1,
xo8l >= 0,
xo8r <= 1,
xo8r >= 0,
xo8u <= 1,
xo8u >= 0,
xo8d <= 1,
xo8d >= 0,
xo8l + xo8r + xo8u + xo8d == 1,
xo9l <= 1,
xo9l >= 0,
xo9r <= 1,
xo9r >= 0,
xo9u <= 1,
xo9u >= 0,
xo9d <= 1,
xo9d >= 0,
xo9l + xo9r + xo9u + xo9d == 1,
xo10l <= 1,
xo10l >= 0,
xo10r <= 1,
xo10r >= 0,
xo10u <= 1,
xo10u >= 0,
xo10d <= 1,
xo10d >= 0,
xo10l + xo10r + xo10u + xo10d == 1,
xo11l <= 1,
xo11l >= 0,
xo11r <= 1,
xo11r >= 0,
xo11u <= 1,
xo11u >= 0,
xo11d <= 1,
xo11d >= 0,
xo11l + xo11r + xo11u + xo11d == 1,
xo12l <= 1,
xo12l >= 0,
xo12r <= 1,
xo12r >= 0,
xo12u <= 1,
xo12u >= 0,
xo12d <= 1,
xo12d >= 0,
xo12l + xo12r + xo12u + xo12d == 1,
xo13l <= 1,
xo13l >= 0,
xo13r <= 1,
xo13r >= 0,
xo13u <= 1,
xo13u >= 0,
xo13d <= 1,
xo13d >= 0,
xo13l + xo13r + xo13u + xo13d == 1,
xo14l <= 1,
xo14l >= 0,
xo14r <= 1,
xo14r >= 0,
xo14u <= 1,
xo14u >= 0,
xo14d <= 1,
xo14d >= 0,
xo14l + xo14r + xo14u + xo14d == 1,
xo15l <= 1,
xo15l >= 0,
xo15r <= 1,
xo15r >= 0,
xo15u <= 1,
xo15u >= 0,
xo15d <= 1,
xo15d >= 0,
xo15l + xo15r + xo15u + xo15d == 1,
xo16l <= 1,
xo16l >= 0,
xo16r <= 1,
xo16r >= 0,
xo16u <= 1,
xo16u >= 0,
xo16d <= 1,
xo16d >= 0,
xo16l + xo16r + xo16u + xo16d == 1,
xo17l <= 1,
xo17l >= 0,
xo17r <= 1,
xo17r >= 0,
xo17u <= 1,
xo17u >= 0,
xo17d <= 1,
xo17d >= 0,
xo17l + xo17r + xo17u + xo17d == 1,
xo18l <= 1,
xo18l >= 0,
xo18r <= 1,
xo18r >= 0,
xo18u <= 1,
xo18u >= 0,
xo18d <= 1,
xo18d >= 0,
xo18l + xo18r + xo18u + xo18d == 1,
xo19l <= 1,
xo19l >= 0,
xo19r <= 1,
xo19r >= 0,
xo19u <= 1,
xo19u >= 0,
xo19d <= 1,
xo19d >= 0,
xo19l + xo19r + xo19u + xo19d == 1,
xo20l <= 1,
xo20l >= 0,
xo20r <= 1,
xo20r >= 0,
xo20u <= 1,
xo20u >= 0,
xo20d <= 1,
xo20d >= 0,
xo20l + xo20r + xo20u + xo20d == 1,
xo21l <= 1,
xo21l >= 0,
xo21r <= 1,
xo21r >= 0,
xo21u <= 1,
xo21u >= 0,
xo21d <= 1,
xo21d >= 0,
xo21l + xo21r + xo21u + xo21d == 1,
xo22l <= 1,
xo22l >= 0,
xo22r <= 1,
xo22r >= 0,
xo22u <= 1,
xo22u >= 0,
xo22d <= 1,
xo22d >= 0,
xo22l + xo22r + xo22u + xo22d == 1,
xo23l <= 1,
xo23l >= 0,
xo23r <= 1,
xo23r >= 0,
xo23u <= 1,
xo23u >= 0,
xo23d <= 1,
xo23d >= 0,
xo23l + xo23r + xo23u + xo23d == 1,
xo24l <= 1,
xo24l >= 0,
xo24r <= 1,
xo24r >= 0,
xo24u <= 1,
xo24u >= 0,
xo24d <= 1,
xo24d >= 0,
xo24l + xo24r + xo24u + xo24d == 1,
xo25l <= 1,
xo25l >= 0,
xo25r <= 1,
xo25r >= 0,
xo25u <= 1,
xo25u >= 0,
xo25d <= 1,
xo25d >= 0,
xo25l + xo25r + xo25u + xo25d == 1,
xo26l <= 1,
xo26l >= 0,
xo26r <= 1,
xo26r >= 0,
xo26u <= 1,
xo26u >= 0,
xo26d <= 1,
xo26d >= 0,
xo26l + xo26r + xo26u + xo26d == 1,
xo27l <= 1,
xo27l >= 0,
xo27r <= 1,
xo27r >= 0,
xo27u <= 1,
xo27u >= 0,
xo27d <= 1,
xo27d >= 0,
xo27l + xo27r + xo27u + xo27d == 1,
xo28l <= 1,
xo28l >= 0,
xo28r <= 1,
xo28r >= 0,
xo28u <= 1,
xo28u >= 0,
xo28d <= 1,
xo28d >= 0,
xo28l + xo28r + xo28u + xo28d == 1,
xo29l <= 1,
xo29l >= 0,
xo29r <= 1,
xo29r >= 0,
xo29u <= 1,
xo29u >= 0,
xo29d <= 1,
xo29d >= 0,
xo29l + xo29r + xo29u + xo29d == 1,
xo30l <= 1,
xo30l >= 0,
xo30r <= 1,
xo30r >= 0,
xo30u <= 1,
xo30u >= 0,
xo30d <= 1,
xo30d >= 0,
xo30l + xo30r + xo30u + xo30d == 1,
xo31l <= 1,
xo31l >= 0,
xo31r <= 1,
xo31r >= 0,
xo31u <= 1,
xo31u >= 0,
xo31d <= 1,
xo31d >= 0,
xo31l + xo31r + xo31u + xo31d == 1,
xo32l <= 1,
xo32l >= 0,
xo32r <= 1,
xo32r >= 0,
xo32u <= 1,
xo32u >= 0,
xo32d <= 1,
xo32d >= 0,
xo32l + xo32r + xo32u + xo32d == 1,
xo33l <= 1,
xo33l >= 0,
xo33r <= 1,
xo33r >= 0,
xo33u <= 1,
xo33u >= 0,
xo33d <= 1,
xo33d >= 0,
xo33l + xo33r + xo33u + xo33d == 1,
xo34l <= 1,
xo34l >= 0,
xo34r <= 1,
xo34r >= 0,
xo34u <= 1,
xo34u >= 0,
xo34d <= 1,
xo34d >= 0,
xo34l + xo34r + xo34u + xo34d == 1,
xo35l <= 1,
xo35l >= 0,
xo35r <= 1,
xo35r >= 0,
xo35u <= 1,
xo35u >= 0,
xo35d <= 1,
xo35d >= 0,
xo35l + xo35r + xo35u + xo35d == 1,
xo36l <= 1,
xo36l >= 0,
xo36r <= 1,
xo36r >= 0,
xo36u <= 1,
xo36u >= 0,
xo36d <= 1,
xo36d >= 0,
xo36l + xo36r + xo36u + xo36d == 1,
xo37l <= 1,
xo37l >= 0,
xo37r <= 1,
xo37r >= 0,
xo37u <= 1,
xo37u >= 0,
xo37d <= 1,
xo37d >= 0,
xo37l + xo37r + xo37u + xo37d == 1,
xo38l <= 1,
xo38l >= 0,
xo38r <= 1,
xo38r >= 0,
xo38u <= 1,
xo38u >= 0,
xo38d <= 1,
xo38d >= 0,
xo38l + xo38r + xo38u + xo38d == 1,
xo39l <= 1,
xo39l >= 0,
xo39r <= 1,
xo39r >= 0,
xo39u <= 1,
xo39u >= 0,
xo39d <= 1,
xo39d >= 0,
xo39l + xo39r + xo39u + xo39d == 1,
xo40l <= 1,
xo40l >= 0,
xo40r <= 1,
xo40r >= 0,
xo40u <= 1,
xo40u >= 0,
xo40d <= 1,
xo40d >= 0,
xo40l + xo40r + xo40u + xo40d == 1,
xo41l <= 1,
xo41l >= 0,
xo41r <= 1,
xo41r >= 0,
xo41u <= 1,
xo41u >= 0,
xo41d <= 1,
xo41d >= 0,
xo41l + xo41r + xo41u + xo41d == 1,
xo42l <= 1,
xo42l >= 0,
xo42r <= 1,
xo42r >= 0,
xo42u <= 1,
xo42u >= 0,
xo42d <= 1,
xo42d >= 0,
xo42l + xo42r + xo42u + xo42d == 1,
xo43l <= 1,
xo43l >= 0,
xo43r <= 1,
xo43r >= 0,
xo43u <= 1,
xo43u >= 0,
xo43d <= 1,
xo43d >= 0,
xo43l + xo43r + xo43u + xo43d == 1,
xo44l <= 1,
xo44l >= 0,
xo44r <= 1,
xo44r >= 0,
xo44u <= 1,
xo44u >= 0,
xo44d <= 1,
xo44d >= 0,
xo44l + xo44r + xo44u + xo44d == 1,
xo45l <= 1,
xo45l >= 0,
xo45r <= 1,
xo45r >= 0,
xo45u <= 1,
xo45u >= 0,
xo45d <= 1,
xo45d >= 0,
xo45l + xo45r + xo45u + xo45d == 1,
xo46l <= 1,
xo46l >= 0,
xo46r <= 1,
xo46r >= 0,
xo46u <= 1,
xo46u >= 0,
xo46d <= 1,
xo46d >= 0,
xo46l + xo46r + xo46u + xo46d == 1,
xo47l <= 1,
xo47l >= 0,
xo47r <= 1,
xo47r >= 0,
xo47u <= 1,
xo47u >= 0,
xo47d <= 1,
xo47d >= 0,
xo47l + xo47r + xo47u + xo47d == 1,
xol <= 1,
xol >= 0,
xor <= 1,
xor >= 0,
xou <= 1,
xou >= 0,
xod <= 1,
xod >= 0,
xol + xor + xou + xod == 1,
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y2 == 0 , y2 == 1 ),
Or (y3 == 0 , y3 == 1 ),
Or (y4 == 0 , y4 == 1 ),
Or (y5 == 0 , y5 == 1 ),
Or (y6 == 0 , y6 == 1 ),
Or (y7 == 0 , y7 == 1 ),
Or (y8 == 0 , y8 == 1 ),
Or (y9 == 0 , y9 == 1 ),
Or (y10 == 0 , y10 == 1 ),
Or (y11 == 0 , y11 == 1 ),
Or (y12 == 0 , y12 == 1 ),
Or (y13 == 0 , y13 == 1 ),
Or (y14 == 0 , y14 == 1 ),
Or (y15 == 0 , y15 == 1 ),
Or (y16 == 0 , y16 == 1 ),
Or (y17 == 0 , y17 == 1 ),
Or (y18 == 0 , y18 == 1 ),
Or (y19 == 0 , y19 == 1 ),
Or (y20 == 0 , y20 == 1 ),
Or (y21 == 0 , y21 == 1 ),
Or (y22 == 0 , y22 == 1 ),
Or (y23 == 0 , y23 == 1 ),
Or (y24 == 0 , y24 == 1 ),
Or (y25 == 0 , y25 == 1 ),
Or (y26 == 0 , y26 == 1 ),
Or (y27 == 0 , y27 == 1 ),
Or (y28 == 0 , y28 == 1 ),
Or (y29 == 0 , y29 == 1 ),
Or (y30 == 0 , y30 == 1 ),
Or (y31 == 0 , y31 == 1 ),
Or (y32 == 0 , y32 == 1 ),
Or (y33 == 0 , y33 == 1 ),
Or (y34 == 0 , y34 == 1 ),
Or (y35 == 0 , y35 == 1 ),
Or (y36 == 0 , y36 == 1 ),
Or (y37 == 0 , y37 == 1 ),
Or (y38 == 0 , y38 == 1 ),
Or (y39 == 0 , y39 == 1 ),
Or (y40 == 0 , y40 == 1 ),
Or (y41 == 0 , y41 == 1 ),
Or (y42 == 0 , y42 == 1 ),
Or (y43 == 0 , y43 == 1 ),
Or (y44 == 0 , y44 == 1 ),
Or (y45 == 0 , y45 == 1 ),
Or (y46 == 0 , y46 == 1 ),
Or (y47 == 0 , y47 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 + y46 + y47 == 6
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')