# Создайте программу, имитирующую работу клиники. Создайте базовый
# класс Doctor с методом treat(). От него создайте три дочерних класса:
# Surgeon, Dentist и Therapist. В каждом дочернем классе
# переопределите метод treat(), чтобы каждый врач выводил сообщение
# о своём способе лечения.
# Создайте класс Patient, содержащий атрибуты treatment_plan — код плана лечения и doctor —
# назначенный пациенту врач. В классе Therapist реализуйте метод назначения врача пациенту.
# Если код плана лечения равен 1, пациенту назначается хирург; если код равен 2 — дантист;
# при любом другом значении — терапевт.
# После назначения врача необходимо сохранить соответствующий объект врача в patient.doctor
# и вызвать у него метод treat(). Создайте пациента, задайте ему план лечения и продемонстрируйте работу программы.

class Doctor:
    title = "врач"
    def treat(self):
        print("Врач проводит лечение.")


class Surgeon(Doctor):
    title = "хирург"
    def treat(self):
        print("Хирург оперирует.")


class Dentist(Doctor):
    title = "стоматолог"
    def treat(self):
        print("Стоматолог лечит кариес.")


class Therapist(Doctor):
    title = "терапевт"
    def treat(self):
        print("Терапевт собирает анамнез и назначает лечение.")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()

        print(
            f"Пациенту с планом лечения {patient.treatment_plan} "
            f"назначен врач: {patient.doctor.title}."
        )

        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


patient_1 = Patient(1)
patient_2 = Patient(2)
patient_3 = Patient(5)

therapist = Therapist()

therapist.assign_doctor(patient_1)
print("\n")

therapist.assign_doctor(patient_2)
print("\n")

therapist.assign_doctor(patient_3)
