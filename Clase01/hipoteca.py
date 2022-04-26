# -*- coding: utf-8 -*-


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
a = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
while saldo > 0:
    while a >= pago_extra_mes_comienzo and a <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado = total_pagado + (pago_mensual + pago_extra)
        a = a + 1
    if saldo <= 1000:
        total_pagado = total_pagado + saldo
        break
        
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual   
    print(a , round(total_pagado, 2) , 'Saldo: ', round(saldo, 2))
    a = a + 1 
print('Total pagado', round(total_pagado, 2), 'Meses: ', a)
