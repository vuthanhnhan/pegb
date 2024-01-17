import axios from "axios";

export const make_order = async (product_ids) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/orders/make'
  const result = await axios.post(url, { product_ids },  { headers: { "Authorization": localStorage.getItem("access_token")}});
  return result.data
};

export const get_history = async () => {
  const url = process.env.VUE_APP_BACKEND_URL + '/orders/history'
  const result = await axios.get(url,  { headers: { "Authorization": localStorage.getItem("access_token")}});
  return result.data
}