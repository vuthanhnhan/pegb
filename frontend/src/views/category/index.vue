<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />
    <div style="display: flex; margin: 5%">
      <product-item
            v-for="(product, index) in products"
            :key="index"
            :product-data-overview="product"
          />
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import { getProducts } from "@/services/products"
import ProductItem from "@/components/ProductItem"
export default {
  data() {
    return {
      categoryId: 1,
      products: []
    };
  },
  components: {
    ProductItem,
    HeaderComponent
},
  methods: {
    async getAllProduct() {
      this.products = await getProducts(this.categoryId)
      console.log("🚀 ~ getAllProduct ~ this.products:", this.products)
    }
  },
  mounted() {
    this.categoryId = decodeURIComponent(this.$route.path.split("/")[2]);
    this.getAllProduct()
  },
};
</script>

<style lang="scss">
.category {
}
</style>