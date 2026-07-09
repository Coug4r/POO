package com.utpl.administracion.DAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import com.utpl.administracion.entidades.Estudiante;

public class EstudianteDAO {
    private Connection con;

    public EstudianteDAO(Connection con) {
        this.con = con;
    }

    public void guardar(Estudiante e) {
        String sql = "INSERT INTO estudiante (cedula, nombres, apellidos, correo, carrera, semestre) " +
                     "VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement ps = con.prepareStatement(sql)) {
            ps.setString(1, e.getCedula());
            ps.setString(2, e.getNombres());
            ps.setString(3, e.getApellidos());
            ps.setString(4, e.getCorreoElectronico());
            ps.setString(5, e.getCarrera());
            ps.setInt(6, e.getSemestre());
            ps.executeUpdate();
            System.out.println("Estudiante guardado correctamente.");
        } catch (SQLException ex) {
            System.err.println("Error al guardar estudiante: " + ex.getMessage());
        }
    }

    public List<Estudiante> listar() {
        List<Estudiante> lista = new ArrayList<>();
        String sql = "SELECT * FROM estudiante";
        try (Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                Estudiante e = new Estudiante(
                    rs.getString("cedula"),
                    rs.getString("nombres"),
                    rs.getString("apellidos"),
                    rs.getString("correo"),
                    rs.getString("carrera"),
                    rs.getInt("semestre")
                );
                e.setCodigo(rs.getInt("id")); 
                lista.add(e);
            }
        } catch (SQLException ex) {
            System.err.println("Error al listar estudiantes: " + ex.getMessage());
        }
        return lista;
    }

    public Estudiante buscarPorId(int codigo) {
        String sql = "SELECT * FROM estudiante WHERE id = ?";
        try (PreparedStatement ps = con.prepareStatement(sql)) {
            ps.setInt(1, codigo);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return new Estudiante(
                        rs.getString("cedula"),
                        rs.getString("nombres"),
                        rs.getString("apellidos"),
                        rs.getString("correo"),
                        rs.getString("carrera"),
                        rs.getInt("semestre")
                    );
                }
            }
        } catch (SQLException ex) {
            System.err.println("Error al buscar estudiante por código: " + ex.getMessage());
        }
        return null;
    }

    public void actualizar(Estudiante e, int id) {
    	if(buscarPorId(id) != null) {
	        String sql = "UPDATE estudiante SET cedula=?, nombres=?, apellidos=?, correo=?, carrera=?, semestre=? " +
	                     "WHERE id=?";
	        try (PreparedStatement ps = con.prepareStatement(sql)) {
	            ps.setString(1, e.getCedula());
	            ps.setString(2, e.getNombres());
	            ps.setString(3, e.getApellidos());
	            ps.setString(4, e.getCorreoElectronico());
	            ps.setString(5, e.getCarrera());
	            ps.setInt(6, e.getSemestre());
	            ps.setInt(7, id);
	            ps.executeUpdate();
	            System.out.println("Estudiante actualizado correctamente.");
	        } catch (SQLException ex) {
	            System.err.println("Error al actualizar estudiante: " + ex.getMessage());
	        }
    	}else {
    		System.out.println("No existe el id!");
    	}
    }

    public void eliminar(int codigo) {
        String sql = "DELETE FROM estudiante WHERE id=?";
        try (PreparedStatement ps = con.prepareStatement(sql)) {
            ps.setInt(1, codigo);
            ps.executeUpdate();
            System.out.println("Estudiante eliminado correctamente.");
        } catch (SQLException ex) {
            System.err.println("Error al eliminar estudiante: " + ex.getMessage());
        }
    }
}
