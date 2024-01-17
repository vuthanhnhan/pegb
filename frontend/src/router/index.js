import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "../views/home/HomePage";
import ProductDetailPage from "../views/products/ProductDetailPage";
import Category from "../views/category";
import Cart from "../views/cart";

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
  { path: "*", redirect: "/" },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

// chuyển đến trang login nếu chưa được login
// router.beforeEach((to, from, next) => {
//   const publicPages = ["/login", "/register"];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem("user");

//   if (authRequired && !loggedIn) {
//     return next("/login");
//   }

//   next();
// });

export default router;
