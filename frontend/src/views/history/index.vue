<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />
    <h1 style="font-size: 30px">Order History</h1>
    <div class="history" v-for="(history, index) in histories" :key="index">
          <div>Id: {{ history.id }}</div>
          <div>Status: {{ history.status }}</div>
          <div>Total price: {{ history.total_amount }}</div>
        </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import { get_history } from "@/services/orders"

export default {
  data() {
    return {
      histories: []
    };
  },
  components: {
    HeaderComponent
},
  methods: {
    async getOrderHistory() {
      this.histories = await get_history()
      console.log("🚀 ~ getOrderHistory ~ this.histories:", this.histories)
    }
  },
  mounted() {
    this.getOrderHistory()
  },
};
</script>

<style lang="scss">
.history {
  margin: 50px;
  div {
    text-align: left;
    margin: 10px;
    display: block
  }
}
</style>