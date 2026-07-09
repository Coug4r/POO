package com.utpl.administracion.utils;

import java.sql.Connection;
import java.sql.DriverManager;

public class ConexionSQLite {
	public static Connection DbConection() {
		try {
			String jddbcUrl = "jdbc:sqlite:C:\\Users\\nasnd\\OneDrive\\Documentos\\sqlite-tools-win-x64-3530300\\universidad";
			Connection conexion = DriverManager.getConnection(jddbcUrl);
			System.out.println("Conexion exitosa!");
			return conexion;
		} catch (Exception e) {
			System.err.println("Error en la conexiona la base de datos!");
			System.out.println(e.getMessage());
			return null;
		}
	}
}
