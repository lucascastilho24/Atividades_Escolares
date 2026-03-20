//Arrow Function
function apresentar (nome) {
    return `Meu nom é ${nome}`;
};
const apresentaArrow = (nome) => `Meu nom é ${nome}`;
const soma = (num1,num2) => num1 + num2;
//Arrow Function com mais de uma linha de instrução
const somaNumeros = (num1,num2) => {
    if (num1 >= 10 || num2 >= 10) {
        return "Somente um número de 1 a 9"
    } else{
        return num1 + num2;
    };
 };