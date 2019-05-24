import axios, {AxiosPromise} from 'axios';

export const HOST_URL = 'http://localhost:8000';

export interface SignupUser {
  username: string;
  email: string;
  password1: string;
  password2: string;
}

export interface User {
  username: string;
  email: string;
  password: string;
}

export interface AuthenticationResponse {
  key: string
}

/**
 * Signs up the input user
 * @param user - {username, email, password1, password2}
 */
export const signup = (user: SignupUser): AxiosPromise<AuthenticationResponse> => {
  return axios.post(`${HOST_URL}/api/v1/rest-auth/registration/`, user)
};

/**
 * Login for the input user
 * @param user = {username, email, password}
 */
export const login = (user: User): AxiosPromise<AuthenticationResponse> => {
  return axios.post(`${HOST_URL}/api/v1/rest-auth/login/`, user);
};
