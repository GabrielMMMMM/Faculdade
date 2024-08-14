/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.exercicio1;
import java.util.Scanner;


public class Exercicio1 {
    
    public static void main(String[] args) {
        //variáveis
        String produto;
        float valor, novoValor;
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o nome do produto: ");
        produto = input.next();
        System.out.print("Digite o valor do produto: R$");
        valor = input.nextFloat();
        
        novoValor = valor -(valor/100 *9);
        
        System.out.printf(String.format("\n O produto com desconto vai custar: R$ %.2f", novoValor));
    }
}

        
        
 