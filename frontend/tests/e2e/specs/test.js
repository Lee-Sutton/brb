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

        // The user is logged in
        cy.contains('Welcome user');

        // The user wants to create a score
        cy.get('nav').contains('Scores').click();
        cy.get('[data-cy=create-score]').click();
        cy.get('#score-form').within(() => {
            cy.get('#id_score').type(72);
            cy.root().submit();
        });
        cy.get('[data-cy=scores-table]').contains(72);
    })
});
