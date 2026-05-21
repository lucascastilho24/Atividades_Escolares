/*
1. Saudação Simples
Crie uma função chamada saudar que não recebe parâmetros e apenas exibe a
mensagem "Olá, mundo!" no console.
*/
function saudar() {
    console.log("Olá, mundo!");
};
saudar()
/*
2. Nome Personalizado
Escreva uma função chamada saudarUsuario que recebe um nome como
parâmetro e exibe: "Olá, [nome]! Seja bem-vindo(a)".
*/
function saudarUsuario(nome) {
    console.log(`Olá ${nome}, seja bem-vindo!`);
};
saudarUsuario("Lucas")
/*
3. Somar Dois Números
Crie uma função chamada somar que recebe dois números como parâmetros e
retorna a soma deles. Exiba o resultado no console chamando a função.
*/
function soma(a,b) {
    console.log(a+b);
};
soma(1,2)
/*
4. Verificador de Par ou Ímpar
Desenvolva uma função chamada ePar que recebe um número. Se o número for
par, retorne true. Se for ímpar, retorne false.
*/
function Par(num) {
    console.log(num%2===0);
};
Par(2)
Par(3)
/*
5. Cálculo de Área
Crie uma função chamada calcularAreaRetangulo que recebe a base e a altura de
um retângulo e retorna a área (base * altura).
*/
function CaucularAreaRetangulo(a,b) {
    console.log("A área do retângulo é: "+a*b);
};
CaucularAreaRetangulo(3,5)
/*
6. Converter para Maiúsculas
Escreva uma função chamada gritar que recebe uma string e a retorna totalmente
em letras maiúsculas (Dica: use o método .toUpperCase()).
*/
function gritar(grito) {
    console.log(grito.toUpperCase());
};
gritar("oooooooohhhhhh")
/*
7. Média de Notas
Crie uma função chamada calcularMedia que recebe três notas como parâmetros
e retorna a média aritmética simples delas.
*/
function calcularMedia(a,b,c) {
    console.log("A média simples é:"+(a+b+c)/3);
};
calcularMedia(2.4,1.8,30)
/*
8. Conversor de Idade
Crie uma função que recebe a idade de uma pessoa e retorna quantos dias de vida
ela tem aproximadamente (considere sempre anos de 365 dias).
*/
function conbersorDeIdades(anos) {
    console.log("Você tem aproximadamente: "+anos*365+" dias");
};
conbersorDeIdades(17)
/*
9. Desconto de Produto
Escreva uma função chamada aplicarDesconto que recebe o valorOriginal de um
produto e uma porcentagemDesconto. A função deve retornar o novo valor com o
desconto aplicado.
*/
function aplicarDesconto(valor,desconto) {
    console.log("O Valor descontado é:",valor-(valor*desconto));
};
aplicarDesconto(10,0.2)
/*
10. Verificador de Maioridade

Crie uma função chamada podeDirigir que recebe a idade de uma pessoa. Se a
idade for 18 ou mais, retorne a string "Pode dirigir". Caso contrário, retorne "Não
pode dirigir".
*/
function podeDirigir(idade) {
    if (idade>=18) {
        console.log("Pode dirigir!");
    } else {
        console.log("Não pode dirigir!");
    };
};
podeDirigir(18)
podeDirigir(16)