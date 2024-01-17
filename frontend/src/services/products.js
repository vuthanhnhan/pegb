import axios from "axios";

export const getProducts = async (category_id) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/products/category/' + category_id
  const result = await axios.get(url);
  return result.data
};

export const getProductById = async (id) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/products/' + id
  const result = await axios.get(url);
  return result.data
};

export const getCategories = async () => {
  const url = process.env.VUE_APP_BACKEND_URL + '/categories'
  const result = await axios.get(url);
  return result.data
};

// create new product
export const updateProduct = (id, new_product) => {
  const url = process.env.VUE_APP_BACKEND_URL + '/products/' + id
  return axios.patch(url, new_product, { headers: { "Authorization": localStorage.getItem("access_token")}});
};
