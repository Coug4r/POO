package com.utpl.administracion.menu;

import java.sql.Connection;
import java.util.Scanner;

import com.utpl.administracion.DAO.EstudianteDAO;
import com.utpl.administracion.entidades.Estudiante;
import com.utpl.administracion.utils.ConexionSQLite;

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("========= SISTEMA =========");
        Connection con = ConexionSQLite.DbConection();

        if (con != null) {
            EstudianteDAO estudiantes = new EstudianteDAO(con);

            boolean salir = false;
            while (!salir) {
                System.out.println("\n1. Registrar estudiante");
                System.out.println("2. Listar estudiantes");
                System.out.println("3. Buscar estudiante");
                System.out.println("4. Actualizar estudiante");
                System.out.println("5. Eliminar estudiante");
                System.out.println("6. Salir");
                System.out.print("Seleccione una opción: ");

                int opc = sc.nextInt();
                sc.nextLine(); // limpiar buffer

                switch (opc) {
                    case 1: {
                        System.out.print("Cedula: ");
                        String cedula = sc.nextLine();
                        System.out.print("Nombres: ");
                        String nombres = sc.nextLine();
                        System.out.print("Apellidos: ");
                        String apellidos = sc.nextLine();
                        System.out.print("Correo: ");
                        String correo = sc.nextLine();
                        System.out.print("Carrera: ");
                        String carrera = sc.nextLine();
                        System.out.print("Semestre: ");
                        int semestre = sc.nextInt();
                        sc.nextLine();

                        Estudiante nuevoEstudiante = new Estudiante(cedula, nombres, apellidos, correo, carrera, semestre);
                        estudiantes.guardar(nuevoEstudiante);
                        break;
                    }
                    case 2: {
                        System.out.println("\n=== LISTA DE ESTUDIANTES ===");
                        for (Estudiante e : estudiantes.listar()) {
                            System.out.printf("Código=%d | Cédula=%s | Nombres=%s | Apellidos=%s | Correo=%s | Carrera=%s | Semestre=%d%n",
                                    e.getCodigo(),
                                    e.getCedula(),
                                    e.getNombres(),
                                    e.getApellidos(),
                                    e.getCorreoElectronico(),
                                    e.getCarrera(),
                                    e.getSemestre());
                        }
                        break;
                    }
                    case 3: {
                        System.out.print("Ingrese el id a buscar: ");
                        int id = sc.nextInt();
                        sc.nextLine();
                        Estudiante e = estudiantes.buscarPorId(id);
                        if (e != null) {
                            System.out.printf("Código=%d | Cédula=%s | Nombres=%s | Apellidos=%s | Correo=%s | Carrera=%s | Semestre=%d%n",
                                    e.getCodigo(),
                                    e.getCedula(),
                                    e.getNombres(),
                                    e.getApellidos(),
                                    e.getCorreoElectronico(),
                                    e.getCarrera(),
                                    e.getSemestre());
                        } else {
                            System.out.println("Estudiante no encontrado.");
                        }
                        break;
                    }
                    case 4: {
                        System.out.print("Id: ");
                        int id = sc.nextInt();
                        sc.nextLine();
                        System.out.print("Cedula: ");
                        String cedula = sc.nextLine();
                        System.out.print("Nombres: ");
                        String nombres = sc.nextLine();
                        System.out.print("Apellidos: ");
                        String apellidos = sc.nextLine();
                        System.out.print("Correo: ");
                        String correo = sc.nextLine();
                        System.out.print("Carrera: ");
                        String carrera = sc.nextLine();
                        System.out.print("Semestre: ");
                        int semestre = sc.nextInt();
                        sc.nextLine();

                        Estudiante actualizado = new Estudiante(cedula, nombres, apellidos, correo, carrera, semestre);
                        estudiantes.actualizar(actualizado, id);
                        break;
                    }
                    case 5: {
                    	System.out.print("Ingrese el id del estudiante a eliminar: ");
                    	int id = sc.nextInt();
                    	sc.nextLine();
                        estudiantes.eliminar(id);
                        break;
                    }
                    case 6: {
                        System.out.println("Saliendo...");
                        salir = true;
                        break;
                    }
                    default:
                        System.out.println("Opción inválida.");
                }
            }
        } else {
            System.out.println("No se pudo conectar a la base de datos.");
        }
        sc.close();
    }
}