"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente("Jose", 2010, 85, 1.90, "Avenida ABC")

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
#hospital.registrar_paciente(paciente=paciente_tres)
hospital.registrar_medico(medico=medico)

hospital.mostrar_pacientes()
hospital.mostrar_medicos()
hospital.pacientes_menores()
hospital.pacientes_mayores()


#hospital.registrar_consulta(id_paciente=1, id_medico=1)

