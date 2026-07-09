package com.utpl.administracion.entidades;

public class Estudiante {
    // Atributos
    private int codigo;
    private String cedula;
    private String nombres;
    private String apellidos;
    private String correoElectronico;
    private String carrera;
    private int semestre;

    // Constructor vacío
    public Estudiante() {
    }

    // Constructor con parámetros
    public Estudiante(String cedula, String nombres, String apellidos,
                      String correoElectronico, String carrera, int semestre) {
        this.cedula = cedula;
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.correoElectronico = correoElectronico;
        this.carrera = carrera;
        this.semestre = semestre;
    }

    // Getters y Setters
    public int getCodigo() {
        return codigo;
    }
    
    public void setCodigo(int codigo) {
		this.codigo = codigo;
	}

	public String getCedula() {
        return cedula;
    }

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public void setCorreoElectronico(String correoElectronico) {
        this.correoElectronico = correoElectronico;
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    public int getSemestre() {
        return semestre;
    }

    public void setSemestre(int semestre) {
        this.semestre = semestre;
    }

    // Método toString
    @Override
    public String toString() {
        return "Estudiante {" +
                "Código='" + codigo + '\'' +
                ", Cédula='" + cedula + '\'' +
                ", Nombres='" + nombres + '\'' +
                ", Apellidos='" + apellidos + '\'' +
                ", Correo='" + correoElectronico + '\'' +
                ", Carrera='" + carrera + '\'' +
                ", Semestre=" + semestre +
                '}';
    }
}