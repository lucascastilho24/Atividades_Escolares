const cliente = {
    nome:"Seu nome",
    idade:"Sua idade",
    cpf:"12345678900",
    email:"Um email qualquer",
};
console.log(cliente);
console.log(cliente.nome);
console.log(cliente.idade);
console.log(cliente.cpf);
console.log(cliente.email);
console.log(`O nome do cliente é ${cliente["nome"]} e essa pessoa tem ${cliente["idade"]} anos.`);
console.log(`Os 3 primeiros digitos do CPF são ${cliente["cpf"].slice(0,3)}`);

const chaves = [
    "nome",
    "idade",
    "cpf",
    "email"
];
chaves.forEach((chave)=>{
    console.log(`A chave ${chave} tem o valor ${cliente[chave]}`)
});