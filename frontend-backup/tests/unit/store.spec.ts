import flushPromises from 'flush-promises';
import {mutations, actions, State} from '@/store';
import {signup, login} from '@/api/users';

jest.mock('@/api/users');

const authToken = {key: '12345'};

beforeEach(() => {
    localStorage.clear();
});

describe('mutations', () => {
    let state: State;

    beforeEach(() => {
        state = {
            isLoggedIn: false
        };
    });

    test('loginSuccess', () => {
        mutations.loginSuccess(state, authToken.key);
        expect(state.isLoggedIn).toBeTruthy();
        expect(localStorage.getItem('token')).toEqual(authToken.key);
    });
});

describe('actions', () => {
    const commit = jest.fn();
    let loginCredentials = {
        username: 'Lee',
        email: 'lee@e.com',
        password: 'password'
    };

    let signupCredentials = {
        username: loginCredentials.username,
        email: loginCredentials.email,
        password1: loginCredentials.password,
        password2: loginCredentials.password,
    };

    beforeEach(() => {
        jest.resetAllMocks();
        (signup as any).mockResolvedValue({data: authToken});
        (login as any).mockResolvedValue({data: authToken});

        loginCredentials = {
            username: 'Lee',
            email: 'lee@e.com',
            password: 'password',
        };

        signupCredentials = {
            username: loginCredentials.username,
            email: loginCredentials.email,
            password1: loginCredentials.password,
            password2: loginCredentials.password,
        };
    });

    test('login success', async () => {
        await actions.login({commit}, loginCredentials);
        await flushPromises();
        expect(login).toBeCalledWith(loginCredentials);
        expect(commit).toBeCalledWith('loginSuccess', authToken.key);
    });

    test('signup success', async () => {
        await actions.signup({commit}, signupCredentials);
        await flushPromises();
        expect(signup).toBeCalledWith(signupCredentials);
        expect(commit).toBeCalledWith('loginSuccess', authToken.key);
    });
});
