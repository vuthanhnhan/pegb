import axios from "axios";

export const login = async (email, password) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/users/login'
  const result = await axios.post(url, { email, password });
  localStorage.setItem("access_token", result.data.access_token);
  await me()
  return result.data.access_token
}

export const me = async () => {
  const url = process.env.VUE_APP_BACKEND_URL + '/users/me'
  const result = await axios.get(url, { headers: { "Authorization": localStorage.getItem("access_token")}});
  localStorage.setItem("me", JSON.stringify(result.data));
}

export const register = async (email, name, password) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/users/register'
  await axios.post(url, { email, name, password });
}