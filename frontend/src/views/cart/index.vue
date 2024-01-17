<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />
    <div style="display: flex; margin: 5%">
      <product-item
            v-for="(product, index) in products"
            :is-cart-page="true"
            :key="index"
            :product-data-overview="product"
          />
    </div>
    <div v-if="transactionInfo">
    </div>
    <el-button @click="handlePurchase">Purchase</el-button>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductItem from "@/components/ProductItem"
export default {
  data() {
    return {
      products: [],
      transactionInfo: null
    };
  },
  components: {
    ProductItem,
    HeaderComponent
},
  methods: {
    getAllProductCart() {
      this.products = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
    },
  },
  mounted() {
    this.getAllProductCart()
  },
};
</script>

<style lang="scss">
.category {
}
</style>