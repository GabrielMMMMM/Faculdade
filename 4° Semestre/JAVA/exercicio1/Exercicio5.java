/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.exercicio1;
import java.util.Scanner;

public class Exercicio5 {
    public static void main(String[] args){
        //variaveis
        double volume, raio, altura;
        final float  pi = 3.14159f;
        
        Scanner input = new Scanner (System.in);
        System.out.print("Digite o tamanho do raio: ");
        raio = input.nextFloat();
        System.out.print("Digite o tamanho da altura: ");
        altura = input.nextFloat();
        
        volume = pi*Math.pow(raio, 2)*altura;
        System.out.printf(String.format("O volume da lata é de: %.2f", volume));
    } 
}
