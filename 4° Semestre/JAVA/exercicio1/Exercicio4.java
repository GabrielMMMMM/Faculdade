/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.exercicio1;
import java.util.Scanner;

public class Exercicio4 {
    public static void main(String[] args) {
        //variáveis
        float C, F;
        Scanner input = new Scanner(System.in);
        System.out.println("Digite a temperatura em grus celsius: ");
        C = input.nextFloat();
        F = (C *9/5)+32;

        System.out.print("\n Temperatura em Fahrenheit: "+ F + "°F");
    }
}
