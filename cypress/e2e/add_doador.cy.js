describe('O gestor de doações adicionará um doador e tentará ver se o doador está salva no banco de dados', () => {
    it('O administrador conseguirá cadastrar um doador e ver ela', () => {
  
      cy.visit('http://127.0.0.1:8000')
      cy.get('nav > .cta').click()
      cy.get('#id_username').type('AdmMestre')
      cy.get('#id_password').type('098')
      cy.get('.submit-row > input').click()
      cy.get('.model-doador > :nth-child(2) > .addlink').click()
      cy.get('#id_nome').type('lucas')
      cy.get('#id_contato').type('8198923456')
      cy.get('#id_email').type('adm23gt@cesar.teste')
      cy.get('#id_endereco').type('rua teste')
      cy.get('#id_usuario').select('lucas')
      cy.get('.default').click()
    })
    it('O administrador nao conseguirá cadastrar um doador e falhará por nao preencher um campo', () => {
  
        cy.visit('http://127.0.0.1:8000')
        cy.get('nav > .cta').click()
        cy.get('#id_username').type('AdmMestre')
        cy.get('#id_password').type('098')
        cy.get('.submit-row > input').click()
        cy.get('.model-doador > :nth-child(2) > .addlink').click()
        cy.get('#id_nome').type('lucas')
        
        cy.get('#id_email').type('adm23gt@cesar.teste')
        cy.get('#id_endereco').type('rua teste')
        cy.get('#id_usuario').select('lucas')
        cy.get('.default').click()
      })
    
    
})