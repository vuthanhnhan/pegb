import axios from "axios";

export const make_order = async (product_ids) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/orders/make'
  const result = await axios.post(url, { product_ids },  { headers: { "Authorization": localStorage.getItem("access_token")}});
  return result.data
};