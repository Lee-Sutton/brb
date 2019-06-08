
import {signup, login, HOST_URL} from '@/api/users';
import faker from 'faker';
import axios from 'axios';


const user = {
  username: faker.internet.userName(),
  email: faker.internet.email(),
  password: faker.internet.password(),
};

const newUser = {
  username: user.username,
  email: user.email,
  password1: user.password,
  password2: user.password,
};

beforeEach(() => {
  axios.post.mockResolvedValue({data: {key: 42}});
});

afterEach(() => {
  jest.resetAllMocks();
});

test('signup', async () => {
  const result = await signup(newUser);
  expect(result.data.key).toBeTruthy();
  expect(axios.post).toHaveBeenCalledWith(`${HOST_URL}/rest-auth/registration/`, newUser);
});

test('login', async () => {
  const result = await login(user);
  expect(result.data.key).toBeTruthy();
  expect(axios.post).toHaveBeenCalledWith(`${HOST_URL}/rest-auth/login/`, user);
});
