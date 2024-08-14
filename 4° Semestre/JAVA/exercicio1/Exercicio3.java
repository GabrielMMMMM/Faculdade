/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.exercicio1;
import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        //variáveis
        float valor1, valor2;
        Scanner input = new Scanner(System.in);
        System.out.println("Programa calcula Média!");
        System.out.print("Digite 1° número: ");
        valor1 = input.nextFloat();
        System.out.print("Digite 2° número: ");
        valor2 = input.nextFloat();
        
        System.out.printf("\nA média é de:  %f", (valor1 + valor2)/2);
    }
}
