<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />
    <div>
      <div v-if="!transactionInfo" style="display: flex; margin: 5%">
        <product-item
              v-for="(product, index) in products"
              :is-cart-page="true"
              :key="index"
              :product-data-overview="product"
            />
      </div>
      <div class="transaction" v-else>
        <div class="discount_detail" v-for="(product, index) in transactionInfo.product_price_detail" :key="index">
          <div>Name: {{ product.product_name }}</div>
          <div class="origin_price">Original price: {{ product.original_price }}</div>
          <div>Discount price: {{ product.discount_price }}</div>
        </div>
        <div class="transaction_info">
          <div>Total: {{ transactionInfo.product_discount_price }}</div>
          <div>Sale off for {{ transactionInfo.user_rank }} user: {{ transactionInfo.user_discount_price }}</div>

        </div>
      </div>
    </div>
    <div v-if="transactionInfo">
    </div>
    <el-button @click="handlePurchase">Purchase</el-button>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductItem from "@/components/ProductItem"
import { make_order } from "@/services/orders"

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
    async handlePurchase() {
      if (!localStorage.getItem('access_token')) {
        this.$message('Please login to continue');
        return
      }

      this.transactionInfo = await make_order(this.products.map(p => p.id))
    }
  },
  mounted() {
    this.getAllProductCart()
  },
};
</script>

<style lang="scss">
.discount_detail + .discount_detail {
  margin-top: 30px;
}

.transaction{
  margin: 50px;

  .transaction_info {
  margin-top: 50px;
  div {
    text-align: left;
    margin: 10px;
    display: block
  }
}

.discount_detail {
  div {
    text-align: left;
    margin: 10px;
    display: block
  }
}
}</style>