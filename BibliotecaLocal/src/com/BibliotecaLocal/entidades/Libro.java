package com.BibliotecaLocal.entidades;

public class Libro {
    private String titulo;
    private String autor;
    private int ISBN;
    private String editorial;
    private int anioPublicacion;
    private int numPag;
    private String categoria;
    private String estado; // "disponible" o "prestado"

    public Libro(String titulo, String autor, int ISBN, String editorial,
                 int anioPublicacion, int numPag, String categoria, String estado) {
        this.titulo = titulo;
        this.autor = autor;
        this.ISBN = ISBN;
        this.editorial = editorial;
        this.anioPublicacion = anioPublicacion;
        this.numPag = numPag;
        this.categoria = categoria;
        this.estado = estado;
    }

    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }

    public String getAutor() { return autor; }
    public void setAutor(String autor) { this.autor = autor; }

    public int getISBN() { return ISBN; }
    public void setISBN(int ISBN) { this.ISBN = ISBN; }

    public String getEditorial() { return editorial; }
    public void setEditorial(String editorial) { this.editorial = editorial; }

    public int getAnioPublicacion() { return anioPublicacion; }
    public void setAnioPublicacion(int anioPublicacion) { this.anioPublicacion = anioPublicacion; }

    public int getNumPag() { return numPag; }
    public void setNumPag(int numPag) { this.numPag = numPag; }

    public String getCategoria() { return categoria; }
    public void setCategoria(String categoria) { this.categoria = categoria; }

    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }
}
