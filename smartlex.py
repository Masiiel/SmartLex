print("Bienvenido a SmartLex")

alertas = 0

salario = int(input("Ingrese su salario mensual: "))

if salario < 1130:
    print("Alerta: posible vulneración salarial")
    alertas += 1


# Jornada laboral
horas_diarias = int(input("¿Cuántas horas trabaja al día?: "))
dias_semana = int(input("¿Cuántos días trabaja por semana?: "))
refrigerio = int(input("¿Cuántos minutos tiene de refrigerio?: "))

horas_semanales = horas_diarias * dias_semana

print("Horas semanales totales:", horas_semanales)

if horas_diarias > 8:
    print("Alerta: excede la jornada máxima diaria permitida")
    alertas += 1

if horas_semanales > 48:
    print("Alerta: excede la jornada máxima semanal permitida")
    alertas += 1

if refrigerio < 45:
    print("Alerta: posible incumplimiento del tiempo mínimo de refrigerio")
    alertas += 1


renuncia = input("¿El contrato indica renuncia de beneficios? (si/no): ")

if renuncia == "si":
    print("Alerta: posible cláusula abusiva")
    alertas += 1


despido = input("¿El contrato permite despido sin causa? (si/no): ")

if despido == "si":
    print("Alerta: posible vulneración laboral")
    alertas += 1


if alertas >= 4:
    print("RIESGO ALTO: Se recomienda asesoría legal.")
elif alertas >= 2:
    print("RIESGO MEDIO: Revisar condiciones del contrato.")
else:
    print("RIESGO BAJO: No se detectaron riesgos graves.")
