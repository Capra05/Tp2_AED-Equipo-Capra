def es_mayuscula(c):
    return c in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
def es_digito(c):
    return c in "1234567890"
def cant_lineas():
    with open("ordenes.txt","rt") as archivo:
        texto = archivo.readlines()[1:]
    return texto
def iniciar():
    archivo = open("ordenes.txt","rt")
    return archivo
def det_codigo_iso(codigo_orden_pago):
    codigo_iso="no detectado"
    if "ARS" in codigo_orden_pago:
            codigo_iso = "ARS"
    if "USD" in codigo_orden_pago:
            codigo_iso = "USD"
    if "EUR" in codigo_orden_pago:
            codigo_iso = "EUR"
    if "GBP" in codigo_orden_pago:
            codigo_iso = "GBP"
    if "JPY" in codigo_orden_pago:
            codigo_iso = "JPY"
    return codigo_iso
def Calculo_impuesto(identificador_calculo_comision,monto_nominal):
    monto_base=0
    comision=0
    monto_fijo=0
    bloques_miles = 0
    if identificador_calculo_comision==1:
        comision=9*monto_nominal//100
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==2:
        if monto_nominal<50000:
            comision=0
        elif monto_nominal>=50000 and monto_nominal<80000:
            comision=5*monto_nominal//100
        elif monto_nominal>80000:
            comision=7.8*monto_nominal//100    
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==3:
        monto_fijo = 100
        if monto_nominal>25000:
            comision=6*monto_nominal//100
        monto_base=monto_nominal-(comision+monto_fijo)  
    elif identificador_calculo_comision==4:
        if monto_nominal<=100000:
            comision=500
        elif monto_nominal>100000:
            comision=1000
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==5:
        if monto_nominal<500000:
            comision=0
        elif monto_nominal>=500000:
            comision=7*monto_nominal//100
        if comision>50000:
            comision=50000
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==6:
        codigo_iso = "GBP"
        comision=0
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==7: 
        comision=0
        monto_base=monto_nominal-comision
    elif identificador_calculo_comision==8:
        bloques_miles = monto_nominal//1000
        if monto_nominal%1000 > 0:
            bloques_miles +=1
        comision = 20 + (3 * bloques_miles)
        monto_base = monto_nominal - comision
    return monto_base,comision
def calculo_impositivo(identificador_calculo_impositivo,monto_base):
    monto_final=0
    impuesto=0
    if identificador_calculo_impositivo==1:
        if monto_base<=300000:
            impuesto=0
        elif monto_base>300000:
            exedente=monto_base-300000
            impuesto=25*exedente//100
        monto_final=monto_base-impuesto
    if identificador_calculo_impositivo==2:
        if monto_base<50000:
            impuesto=50
        elif monto_base>=50000:
            impuesto=100
        monto_final=monto_base-impuesto
    if identificador_calculo_impositivo==3:
        impuesto=3*monto_base//100
        monto_final=monto_base-impuesto
    return monto_final,impuesto
def moneda_invalida(cadena):
    mensaje_error="Moneda incorrecta"
    if not (("ARS" in cadena)or("USD" in cadena)or("EUR" in cadena)or("GBP" in cadena)or("JPY" in cadena) ):
        return True, mensaje_error
    return False, None
def invalida(cadena):
    mensaje_error = "Destinatario mal identificado"
    for c in cadena:
        if not (es_mayuscula(c) or es_digito(c) or c == '-'):
            return True, mensaje_error

    if all(c == '-' for c in cadena):
        return True, mensaje_error

    return False, None
def mostrar_resultados(r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16):
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', r1) 
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', r2) 
    print(' (r3) - Cantidad de operaciones validas:', r3) 
    print(' (r4) - Suma de montos finales de operaciones validas:', round(r4,2)) 
    print(' (r5) - Cantidad de ordenes para moneda ARS:', r5) 
    print(' (r6) - Cantidad de ordenes para moneda USD:', r6) 
    print(' (r7) - Cantidad de ordenes para moneda EUR:', r7) 
    print(' (r8) - Cantidad de ordenes para moneda GBP:', r8) 
    print(' (r9) - Cantidad de ordenes para moneda JPN:', r9) 
    print('(r10) - Codigo de la orden de pago con mayor diferencia  nominal - final:', r10) 
    print('(r11) - Monto nominal de esa misma orden:', r11) 
    print('(r12) - Monto final de esa misma orden:', r12) 
    print('(r13) - Nombre del primer beneficiario del archivo:', r13) 
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', r14) 
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:',r15 ) 
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', r16)
def principal():
    lineas = cant_lineas()
    archivo = iniciar()  
    # variebles para guardas los datos del archvo
    nombre = ""
    codigo_identificacion = ""
    codigo_orden_pago = ""
    monto_nominal = 0
    identificador_calculo_comision = ""
    identificador_calculo_impositivo = ""
    #vaiables de codigo
    codigo_iso = "Moneda no autorizada"
    comision=0
    monto_base=0
    impuesto=0
    monto_final=0
    total_operaciones=0
    invalidez=False
    orden_invalida="no se modifico"
    cant_invalidas=0
    r1=0
    r2=0
    r3=0
    r4=0
    r5=0
    r6=0
    r7=0
    r8=0
    r9=0
    r10=0
    r11=0
    r12=0
    diff=0
    r13="1ro"
    r14=0
    r15=0

    cont_ars_val=0
    total_op_validas_ars=0
    r16=0
    for i in lineas:
        invalidez,orden_invalida=False,"no pasa nada" #creo que si saco esto no pasa nada
        total_operaciones+=1
        #cambio de linea que ademas elimina la primera (ver si anda bien o volver a lo de antes)
        archivo.readline()
        #obtencion de todo el texo y convertir en numero
        nombre=archivo.readline(20).strip()
        codigo_identificacion=archivo.readline(10).strip()
        codigo_orden_pago=archivo.readline(10).strip()
        monto_nominal=int(archivo.readline(10).strip())
        identificador_calculo_comision = int(archivo.readline(2).strip())
        identificador_calculo_impositivo = int(archivo.readline(2).strip())
        if r13 == "1ro":
            r13=nombre
        if nombre==r13:
            r14+=1

        #calculo de comicion
        codigo_iso=det_codigo_iso(codigo_orden_pago)
        monto_base,comision=Calculo_impuesto(identificador_calculo_comision,monto_nominal)
        #calculo de calculo imporsitivo
        monto_final,impuesto=calculo_impositivo(identificador_calculo_impositivo,monto_base)
        #veificacion si la moneda y el destintario son validos
        invalidez,orden_invalida=moneda_invalida(codigo_orden_pago)
        if invalidez==False:
            invalidez,orden_invalida=invalida(codigo_identificacion)
        if invalidez:
            cant_invalidas+=1
            if orden_invalida=="Moneda incorrecta":
                r1+=1  
            else:
                r2+=1
        elif not invalidez:
            #operaciones validas
            r3+=1
            r4+=monto_final
            if codigo_iso=="ARS":
                cont_ars_val+=1
                total_op_validas_ars+=monto_final
        diferencia = (monto_nominal-monto_final)
        if diff<diferencia:
            diff=monto_nominal-monto_final
            r10=codigo_orden_pago
            r11=monto_nominal
            r12=monto_final
        #calcular cantidad de monedas "validas" tanto no
        if codigo_iso=="ARS" and orden_invalida!="Moneda incorrecta":
            r5+=1
        if codigo_iso=="USD" and orden_invalida!="Moneda incorrecta":
            r6+=1
        if codigo_iso=="EUR" and orden_invalida!="Moneda incorrecta":
            r7+=1
        if codigo_iso=="GBP" and orden_invalida!="Moneda incorrecta":
            r8+=1
        if codigo_iso=="JPY" and orden_invalida!="Moneda incorrecta":
            r9+=1
    r15=(100*cant_invalidas//total_operaciones) if total_operaciones !=0 else 0
    r16=total_op_validas_ars//cont_ars_val if cont_ars_val !=0 else 0
    mostrar_resultados(r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16)

if __name__ == "__main__":
    principal()