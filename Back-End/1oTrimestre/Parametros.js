//Parâmetros
function soma (num1,num2){
    return num1 + num2;
};
console.log(soma(1,2));
function nomeIdade (nome,idade) {
    return `Meu nome é ${nome} e tenho ${idade} anos`;
};
console.log(nomeIdade("Lucas Daniel",17));
function multiplicacao (num1=1,num2=1) {
    return num1 * num2;
};
console.log(multiplicacao(soma(4,5),soma(3,3)));
console.log(multiplicacao(8));