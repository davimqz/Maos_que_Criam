describe('enviar pergunta', () => {
    it('O usuário irá realizar uma pergunta e a enviará com sucesso', () => {
  
      cy.visit('http://127.0.0.1:8000/enviar-pergunta/')
      cy.get('textarea').type('eu posso enviar quantos produtos por vez ?')
      cy.get('button').click()
    })

    it('O usuário não irá escrever uma pergunta e tentará enviar "nada" ', () => {
      cy.visit('http://127.0.0.1:8000/enviar-pergunta/')
      cy.get('button').click()
    })
    
  })