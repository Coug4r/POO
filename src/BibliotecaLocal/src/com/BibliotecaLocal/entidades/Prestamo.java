package com.BibliotecaLocal.entidades;

import java.time.LocalDate;

public class Prestamo {
    private int idPrestamo;
    private Estudiante estudiante;
    private Libro libro;
    private LocalDate fechaPrestamo;
    private LocalDate fechaDevolucion;
    private LocalDate fechaEntregaReal;
    private String estado; // "activo" o "devuelto"
    private double multa;
    private int diasPrestado;

    public Prestamo(int idPrestamo, Estudiante estudiante, Libro libro,
                    LocalDate fechaDevolucion, String estado) {
        this.idPrestamo = idPrestamo;
        this.estudiante = estudiante;
        this.libro = libro;
        this.fechaPrestamo = LocalDate.now();
        this.fechaDevolucion = fechaDevolucion;
        this.estado = estado;
        this.multa = 0.0;
        this.diasPrestado = 0;
    }

    public int getIdPrestamo() { return idPrestamo; }
    public Estudiante getEstudiante() { return estudiante; }
    public Libro getLibro() { return libro; }

    public LocalDate getFechaPrestamo() { return fechaPrestamo; }
    public LocalDate getFechaDevolucion() { return fechaDevolucion; }

    public LocalDate getFechaEntregaReal() { return fechaEntregaReal; }
    public void setFechaEntregaReal(LocalDate fechaEntregaReal) { this.fechaEntregaReal = fechaEntregaReal; }

    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }

    public double getMulta() { return multa; }
    public void setMulta(double multa) { this.multa = multa; }

    public int getDiasPrestado() { return diasPrestado; }
    public void setDiasPrestado(int diasPrestado) { this.diasPrestado = diasPrestado; }
}
