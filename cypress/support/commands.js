// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add("login", (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This is will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })
Cypress.Commands.add('resetDb', () => {
    return cy.exec('docker-compose -f local.yml run django python manage.py flush --noinput')
});

Cypress.Commands.add('registerUser', (user) => {
    return cy.request('POST', '/rest-auth/registration/', user)
});

Cypress.Commands.add('seedUserAndLogin', (user) => {
    const registerCredentials = Cypress._.pick(user, 'username', 'email');
    registerCredentials.password1 = user.password;
    registerCredentials.password2 = user.password;
    cy.registerUser(registerCredentials);
    cy.reload();
});
