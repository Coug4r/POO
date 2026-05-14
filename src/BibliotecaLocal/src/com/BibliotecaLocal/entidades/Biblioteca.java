package com.BibliotecaLocal.entidades;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Biblioteca {
    private String nombre;
    private String direccion;
    private List<Libro> libros = new ArrayList<>();
    private List<Estudiante> estudiantes = new ArrayList<>();
    private List<Prestamo> prestamos = new ArrayList<>();
    private int ultimoPrestamo = 1;

    // R1: Registrar libros (máximo 20)
    public void registrarLibro(Libro libro) {
        if (libros.size() >= 20) {
            System.err.println("Error: El catálogo ya tiene 20 libros.");
            return;
        }
        if (buscarLibro(libro.getTitulo()) != null) {
            System.err.println("Error: El libro ya existe.");
            return;
        }
        libros.add(libro);
    }

    // R8: Búsqueda por título (case-insensitive)
    public Libro buscarLibro(String titulo) {
        for (Libro l : libros) {
            if (l.getTitulo().equalsIgnoreCase(titulo)) {
                return l;
            }
        }
        return null;
    }

    // R4: Buscar por género
    public List<Libro> buscarPorGenero(String genero) {
        List<Libro> resultado = new ArrayList<>();
        for (Libro l : libros) {
            if (l.getCategoria().equalsIgnoreCase(genero)) {
                resultado.add(l);
                System.out.println(l.getTitulo() + " - Estado: " + l.getEstado());
            }
        }
        if (resultado.isEmpty()) {
            System.out.println("No se encontraron libros del género: " + genero);
        }
        return resultado;
    }

    // R7: Mostrar libros disponibles
    public void mostrarLibrosDisponibles() {
        System.out.println("Libros disponibles:");
        for (Libro l : libros) {
            if (l.getEstado().equalsIgnoreCase("disponible")) {
                System.out.println(l.getTitulo() + " - " + l.getAutor());
            }
        }
    }

    // Registrar estudiante con validación de cédula
    public void registrarEstudiante(Estudiante estudiante) {
        if (!validarCedulaEcuatoriana(estudiante.getCedula())) {
            System.err.println("Error: Cédula inválida.");
            return;
        }
        if (buscarEstudiante(estudiante.getCedula()) != null) {
            System.err.println("Error: El estudiante ya está registrado.");
            return;
        }
        estudiantes.add(estudiante);
    }

    public Estudiante buscarEstudiante(String cedula) {
        for (Estudiante e : estudiantes) {
            if (e.getCedula().equals(cedula)) {
                return e;
            }
        }
        return null;
    }

    // R2, R3: Préstamo con validaciones
    public boolean prestamo(String cedula, String tituloLibro, LocalDate fechaDevolucion) {
        if (!validarCedulaEcuatoriana(cedula)) {
            System.out.println("Cédula inválida.");
            return false;
        }

        Estudiante e = buscarEstudiante(cedula);
        Libro l = buscarLibro(tituloLibro);

        if (e == null) {
            System.out.println("El estudiante no existe.");
            return false;
        }
        if (l == null) {
            System.out.println("El libro no existe.");
            return false;
        }
        if (!l.getEstado().equalsIgnoreCase("disponible")) {
            System.out.println("El libro no está disponible.");
            return false;
        }

        // Control de préstamos activos
        int prestamosActivos = 0;
        for (Prestamo p : prestamos) {
            if (p.getEstudiante().equals(e) && p.getEstado().equalsIgnoreCase("activo")) {
                prestamosActivos++;
            }
        }
        if (prestamosActivos >= 3) {
            System.out.println("El estudiante ya tiene el máximo de 3 préstamos activos.");
            return false;
        }

        // Verificar multas pendientes
        for (Prestamo p : prestamos) {
            if (p.getEstudiante().equals(e) && p.getMulta() > 0 && p.getEstado().equalsIgnoreCase("activo")) {
                System.out.println("El estudiante tiene multas pendientes y no puede solicitar un préstamo.");
                return false;
            }
        }

        int nuevoId = ultimoPrestamo++;
        Prestamo nuevoPrestamo = new Prestamo(nuevoId, e, l, fechaDevolucion, "activo");
        prestamos.add(nuevoPrestamo);
        l.setEstado("prestado");
        return true;
    }

    // R6: Devolver libro con cálculo de multa
    public void devolverLibro(int idPrestamo, int diasPrestado) {
        for (Prestamo p : prestamos) {
            if (p.getIdPrestamo() == idPrestamo && p.getEstado().equalsIgnoreCase("activo")) {
                p.setEstado("devuelto");
                p.setFechaEntregaReal(LocalDate.now());
                p.setDiasPrestado(diasPrestado);

                if (diasPrestado > 7) {
                    double multa = (diasPrestado - 7) * 0.50;
                    p.setMulta(multa);
                    System.out.println("Se aplicó una multa de $" + multa + " al estudiante " + p.getEstudiante().getNombre());
                } else {
                    System.out.println("Devolución sin multa.");
                }
                p.getLibro().setEstado("disponible");
                return;
            }
        }
        System.out.println("No se encontró un préstamo activo con ID: " + idPrestamo);
    }

    // R3: Multar estudiante
    public void multarEstudiante(String cedulaEstudiante, double monto) {
        if (!validarCedulaEcuatoriana(cedulaEstudiante)) {
            System.out.println("Cédula inválida.");
            return;
        }

        Estudiante estudiante = buscarEstudiante(cedulaEstudiante);
        if (estudiante == null) {
            System.out.println("No existe un estudiante con la cédula: " + cedulaEstudiante);
            return;
        }

        for (Prestamo p : prestamos) {
            if (p.getEstudiante().equals(estudiante) && p.getEstado().equalsIgnoreCase("activo")) {
                p.setMulta(monto);
                System.out.println("Multa de $" + monto + " asignada al préstamo ID: " + p.getIdPrestamo());
                return;
            }
        }
        System.out.println("El estudiante no tiene préstamos activos para multar.");
    }

    // R5: Generar reporte
    public void generarReporte() {
        System.out.println("REPORTE DE USUARIOS");
        for (Estudiante e : estudiantes) {
            int cantidadPrestamos = 0;
            boolean tieneMultaPendiente = false;

            for (Prestamo p : prestamos) {
                if (p.getEstudiante().equals(e)) {
                    if (p.getEstado().equalsIgnoreCase("activo")) {
                        cantidadPrestamos++;
                    }
                    if (p.getMulta() > 0) {
                        tieneMultaPendiente = true;
                    }
                }
            }
            System.out.println("Estudiante: " + e.getNombre() + " " + e.getApellido());
            System.out.println("Libros prestados: " + cantidadPrestamos);
            System.out.println("Multa pendiente: " + (tieneMultaPendiente ? "Sí" : "No"));
            System.out.println("-----------------------------------");
        }
    }

    // Método de validación de cédula ecuatoriana (multiplicando 1,2,1,2…)
    public boolean validarCedulaEcuatoriana(String cedula) {
        if (cedula == null || cedula.length() != 10 || !cedula.matches("\\d+")) {
            return false;
        }
        int suma = 0;
        for (int i = 0; i < 9; i++) {
            int num = Character.getNumericValue(cedula.charAt(i));
            if (i % 2 == 0) { // posiciones pares multiplicar por 2
                num *= 2;
                if (num > 9) num -= 9;
            }
            suma += num;
        }
        int digitoVerificador = Character.getNumericValue(cedula.charAt(9));
        int decenaSuperior = ((suma + 9) / 10) * 10;
        int resultado = decenaSuperior - suma;
        if (resultado == 10) resultado = 0;
        return resultado == digitoVerificador;
    }
}