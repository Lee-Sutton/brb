// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
    it('Visits the app root url', () => {
        cy.visit('/');

        // The user is greeted
        cy.get('.jumbotron').contains('Welcome to Golf Buddy');

        // The user clicks the sign up link
        cy.get('[data-cy=sign-up]').click();
        cy.get('form').within(() => {
            cy.get('[data-cy=username');
            cy.get('[data-cy=email');
            cy.get('[data-cy=password');
            cy.get('[data-cy=password-confirm');
        })
    })
});
