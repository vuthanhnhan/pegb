import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "../views/home/HomePage";
import ProductDetailPage from "../views/products/ProductDetailPage";
import Category from "../views/category";
import Cart from "../views/cart";
import OrderHistory from "../views/history"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  // Product
  {
    path: "/product/:productName",
    name: "productDetail",
    component: ProductDetailPage,
  },
  {
    path: "/cart",
    name: "cart",
    component: Cart,
  },
  // Add new product
  {
    path: "/add-product",
    name: "addProduct",
    component: () => import("../views/products/AddNewProductPage"),
  },

  // ******************************
  // Category
  {
    path: "/category/:id",
    name: "category",
    component: Category,
  },
  {
    path: "/history",
    name: "history",
    component: OrderHistory,
  },
  { path: "*", redirect: "/" },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
