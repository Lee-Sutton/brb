import {signup, login, SignupUser, User, HOST_URL} from '@/api/users';
import faker from 'faker';
import axios from 'axios';

jest.mock('axios');

const user: User = {
    username: faker.internet.userName(),
    email: faker.internet.email(),
    password: faker.internet.password(),
};

const newUser: SignupUser = {
    username: user.username,
    email: user.email,
    password1: user.password,
    password2: user.password,
};

beforeEach(() => {
    (axios.post as any).mockResolvedValue({data: {key: 42}});
});

afterEach(() => {
    jest.resetAllMocks();
});

test('signup', async () => {
    const result = await signup(newUser);
    expect(result.data.key).toBeTruthy();
    expect(axios.post).toHaveBeenCalledWith(`${HOST_URL}/api/v1/rest-auth/registration/`, newUser);
});

test('login', async () => {
    const result = await login(user);
    expect(result.data.key).toBeTruthy();
    expect(axios.post).toHaveBeenCalledWith(`${HOST_URL}/api/v1/rest-auth/login/`, user);
});
