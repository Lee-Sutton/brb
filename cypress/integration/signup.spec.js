/// <reference types="Cypress" />

const user = {
    email: 'lee@e.com',
    username: 'lmsutton',
    password: 'password432123',
};

describe('signup spec', () => {
    beforeEach(() => {
        cy.resetDb();
        cy.visit('http://localhost:8000');
    });

    it('should allow the user to signup', () => {
        cy.get('nav').contains('Sign Up').click();

        // THe user submits the form without filling in any information
        cy.get('form').within(() => {
            cy.root().submit();
        });

        cy.get('form').within(() => {
            // The user sees the fields are required
            cy.contains('This field is required');

            // The user fills in the form fields
            cy.get('#id_email').type(user.email);
            cy.get('#id_username').type(user.username);
            cy.get('#id_password1').type(user.password);
            cy.get('#id_password2').type(user.password);
            cy.root().submit();
        });

        cy.get('.alert').contains(`Confirmation e-mail sent to ${user.email}`)

        // The user wants to log out
        cy.get('#navbarSupportedContent').contains('Log Out').click();

        // The user should be able to sign in
        cy.get('#navbarSupportedContent').contains('Sign In').click();

        // The user submits the form before filling in the fields
        cy.get('form').within(() => {
            cy.root().submit();
        });

        cy.get('form').within(() => {
            // The user sees the fields are required
            cy.contains('This field is required');

            // The user fills in the form fields
            cy.get('#id_login').type(user.username);
            cy.get('#id_password').type(user.password);
            cy.root().submit();
        });
    });
});
