describe('Feedback do doador', () => {
    it('O usuário irá preencher o formulário corretamente e enviará sua opinião', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/feedbackdoador/"]').click()
      cy.get('#nome').type('Fulando o doador')
      cy.get('#material').type('Material do fulano')
      cy.get('textarea').type('Opinião do fulano')
      cy.get('#opcoes').select(1)
      cy.get('.btn').click()
      
     
    })

    it('O usuário não irá informar o nome no formulário e tentará enviar o feedback', () => {
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/feedbackdoador/"]').click()
      cy.get('#material').type('Material do fulano')
      cy.get('textarea').type('Opinião do fulano')
      cy.get('#opcoes').select(1)
      cy.get('.btn').click()



    })

    it('O usuário não irá informar o material que está sendo doado e tentará enviar o feedback', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/feedbackdoador/"]').click()
      cy.get('#nome').type('Fulando o doador')
      cy.get('textarea').type('Opinião do fulano')
      cy.get('#opcoes').select(1)
      cy.get('.btn').click()
      
     
    })

    it('O usuário não irá informar a opinião e tentará enviar o feedback', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/feedbackdoador/"]').click()
      cy.get('#nome').type('Fulando o doador')
      cy.get('#material').type('Material do fulano')
      cy.get('#opcoes').select(1)
      cy.get('.btn').click()
      
     
    })

    it('O usuário não irá selecionar uma das opções da dropbox e tentará enviar o feedback', () => {
  
      cy.visit('http://127.0.0.1:8000/')
      cy.get('[href="/feedbackdoador/"]').click()
      cy.get('#nome').type('Fulando o doador')
      cy.get('#material').type('Material do fulano')
      cy.get('textarea').type('Opinião do fulano')
      cy.get('.btn').click()
      
     
    })

    
    
  })