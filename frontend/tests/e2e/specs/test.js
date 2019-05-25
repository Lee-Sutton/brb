// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
    beforeEach(() => {
        cy.exec('docker-compose -f ../local.yml run django python manage.py flush --no-input')
    });

    const user = {
        username: 'lmsutton',
        email: 'email@e.com',
        password: 'password123!@#',
        passwordConfirm: 'password123!@#',
    };

    it('Visits the app root url', () => {
        cy.visit('/');

        // The user is greeted
        cy.get('.jumbotron').contains('Welcome to Golf Buddy');

        // The user clicks the sign up link
        // TODO dry out this code
        cy.get('[data-cy=sign-up]').click();
        cy.get('#account-form').within(() => {
            cy.get('#id_username').type(user.username);
            cy.get('#id_email').type(user.email);
            cy.get('#id_password').type(user.password);
            cy.get('#id_password_confirm').type(user.passwordConfirm);
            cy.root().submit();
        });

        cy.contains(`Welcome ${user.username}`);
    })
});
