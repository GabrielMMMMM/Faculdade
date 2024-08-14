/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.exercicio1;
import java.util.Scanner;

public class Exercicio2 {
     public static void main(String[] args) {
        //variáveis
        float salarioMinimo, salario;
        Scanner input = new Scanner(System.in);
       
        System.out.print("Digite o seu Salário: R$");
        salario = input.nextFloat();
        System.out.print("\nDigite o seu Salário Mínimo: R$");
        salarioMinimo = input.nextFloat();
        
        System.out.print("\nVocê ganha até " + Math.floor(salario/salarioMinimo) + " Salário(s) mínimo(s)");
    }
}
