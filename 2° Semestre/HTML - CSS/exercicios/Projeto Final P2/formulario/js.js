const frm = document.querySelector("form")
const resp = document.querySelector("#resposta")
const respN = document.querySelector("#rNome")
const respE = document.querySelector("#rEmail")
const respS = document.querySelector("#rSenha")
const respC = document.querySelector("#rCsenha")

frm.addEventListener("submit", e => {
    e.preventDefault()
    
    // Limpar mensagens de erro anteriores
    respN.innerText = ''
    respE.innerText = ''
    respS.innerText = ''
    respC.innerText = ''
    resp.innerText = ''
    
    const nome = frm.nome.value
    const email = frm.email.value
    const senha = frm.senha.value
    const cSenha = frm.cSenha.value

    var erro = 0

    if (nome === "") {
        respN.innerText = 'Digite o nome!'
        erro += 1
    }
    if (email === "") {
        respE.innerText = 'Digite o email!'
        erro += 1
    }
    if (senha === "") {
        respS.innerText = 'Digite a senha!'
        erro += 1
    }
    if (cSenha === "") {
        respC.innerText = 'Digite a senha novamente!'
        erro += 1
    }

    if (senha !== cSenha) {
        respC.innerText = 'Senhas não estão iguais, tente novamente.'
        erro += 1 // Incrementar erro para impedir submissão com senhas diferentes
    }

    if (erro == 0) {
        resp.innerText = "Cadastro Realizado com Sucesso!"
        frm.reset()
    }
})
