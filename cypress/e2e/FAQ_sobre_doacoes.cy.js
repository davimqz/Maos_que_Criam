describe('template spec', () => {
    it('O usuário entrará na pagina e vai vizualizar as duvidas da comunidade e responder', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('nav > .cta').click()
      cy.get('#id_username').type('AdmMestre')
      cy.get('#id_password').type('098')
      cy.get('.submit-row > input').click()
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/gerenciar-perguntas/"]').click()
      cy.get(':nth-child(2) > :nth-child(3) > form > textarea').type('resposta1')
      cy.get(':nth-child(2) > :nth-child(3) > form > .btn-info').click()
    })

    
})