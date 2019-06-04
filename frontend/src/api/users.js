import axios from 'axios';

// TODO move this to the api folder /index.js
export const HOST_URL = 'http://localhost:8000';

/**
 * Signs up the input user
 * @param user - {username, email, password1, password2}
 */
export const signup = (user) => {
  return axios.post(`${HOST_URL}/rest-auth/registration/`, user)
};

/**
 * Login for the input user
 * @param user = {username, email, password}
 */
export const login = (user) => {
  return axios.post(`${HOST_URL}/rest-auth/login/`, user);
};
