

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if estudiantes is None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes
        if asignaturas is None:
            self._asignaturas = []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista = None):
        if(lista is None):
             self.listadoAlumnos = [alumno]          
        else:
           lista.append(alumno)
           self.listadoAlumnos = self.listadoAlumnos + lista


    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return "Grupo de estudiantes: "+ self._grupo
