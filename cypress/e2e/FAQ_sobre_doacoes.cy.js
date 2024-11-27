describe('template spec', () => {
    it('O usuário entrará na pagina com perguntas pre estabelecidas, procurará pela sua duvida, não a encontrará, e irá escrever uma duvida própria', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/perguntas-frequentes/"]').click()
      cy.get('.btn-submit').click()
      cy.get('textarea').type('Pergunta exemplo do usuário (história 8-9)')
      cy.get('button').click()
    })

    it('O usuário visualizará as duvidas frequentes de outros usuários, tentará enviar outra, mas não escreverá nada', () => {
  
        cy.visit('http://127.0.0.1:8000/')
        cy.get('[href="/perguntas-frequentes/"]').click()
        cy.get('.btn-submit').click()
        cy.get('button').click()
    })
    
})