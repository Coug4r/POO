package com.Biblioteca.main;

import java.time.LocalDate;

import com.BibliotecaLocal.entidades.Biblioteca;
import com.BibliotecaLocal.entidades.Estudiante;
import com.BibliotecaLocal.entidades.Libro;

public class BibliotecaMain {
    public static void main(String[] args) {
        // 1. Crear la biblioteca
        Biblioteca biblioteca = new Biblioteca();
        System.out.println("Biblioteca Benjamin Carrión creada.");

        // 2. Agregar 8 libros de distintos géneros
        biblioteca.registrarLibro(new Libro("Cien años de soledad", "Gabriel García Márquez", 111, "Sudamericana", 1967, 400, "Novela", "disponible"));
        biblioteca.registrarLibro(new Libro("Breve historia del tiempo", "Stephen Hawking", 112, "Bantam", 1988, 256, "Ciencia", "disponible"));
        biblioteca.registrarLibro(new Libro("Historia de Roma", "Tito Livio", 113, "Clásicos", -27, 300, "Historia", "disponible"));
        biblioteca.registrarLibro(new Libro("El Hobbit", "J.R.R. Tolkien", 114, "Allen & Unwin", 1937, 310, "Fantasía", "disponible"));
        biblioteca.registrarLibro(new Libro("1984", "George Orwell", 115, "Secker & Warburg", 1949, 328, "Novela", "disponible"));
        biblioteca.registrarLibro(new Libro("Cosmos", "Carl Sagan", 116, "Random House", 1980, 365, "Ciencia", "disponible"));
        biblioteca.registrarLibro(new Libro("La Segunda Guerra Mundial", "Winston Churchill", 117, "Cassell", 1948, 500, "Historia", "disponible"));
        biblioteca.registrarLibro(new Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 118, "Bloomsbury", 1997, 223, "Fantasía", "disponible"));

        // 3. Registrar 3 usuarios distintos
        Estudiante e1 = new Estudiante("0102030405", "Juan", "Perez", "juan@mail.com", "0999999999", "Loja");
        Estudiante e2 = new Estudiante("0203040506", "Maria", "Lopez", "maria@mail.com", "0988888888", "Quito");
        Estudiante e3 = new Estudiante("0304050607", "Carlos", "Gomez", "carlos@mail.com", "0977777777", "Guayaquil");

        biblioteca.registrarEstudiante(e1);
        biblioteca.registrarEstudiante(e2);
        biblioteca.registrarEstudiante(e3);

        // 4. Realizar 5 préstamos (incluyendo uno de libro ya prestado)
        biblioteca.prestamo("0102030405", "Cien años de soledad", LocalDate.now().plusDays(7));
        biblioteca.prestamo("0203040506", "Breve historia del tiempo", LocalDate.now().plusDays(7));
        biblioteca.prestamo("0304050607", "El Hobbit", LocalDate.now().plusDays(7));
        biblioteca.prestamo("0102030405", "1984", LocalDate.now().plusDays(7));
        // Intento de prestar un libro ya prestado
        biblioteca.prestamo("0203040506", "Cien años de soledad", LocalDate.now().plusDays(7));

        // 5. Intentar que un usuario con multa solicite un préstamo
        biblioteca.multarEstudiante("0102030405", 5.0); // multamos a Juan
        biblioteca.prestamo("0102030405", "Cosmos", LocalDate.now().plusDays(7)); // debe rechazar

        // 6. Registrar 2 devoluciones: una a tiempo y otra con retraso
        biblioteca.devolverLibro(1, 5); // devolución a tiempo (sin multa)
        biblioteca.devolverLibro(2, 10); // devolución con retraso (aplica multa)

        // 7. Buscar libros por género
        biblioteca.buscarPorGenero("Fantasía");

        // 8. Generar reporte final
        biblioteca.generarReporte();
    }
}
