<template>
  <div class="product-detail-page">
    <header-component />
    <product-detail
      :productName="this.productData.name"
      :categoryName="this.productData.categoryName"
      :price="this.productData.price"
      :title="this.productData.title"
      :documentLevel="this.productData.documentLevel"
      :owner="this.productData.owner"
      :status="this.productData.status"
      :documnentSummary="this.productData.identityItemDescription"
    />
    <product-rating :rating="this.productData.rating" />

    <div v-if="similarProduct.length > 0" class="product-similar">
      <div class="product-similar-header">Maybe you like</div>
      <div class="product-similar-body">
        <product-item
          v-for="(product, index) in similarProduct"
          :key="index"
          :product-data-overview="product"
        />
      </div>
    </div>

    <!-- <el-pagination
        class="pagination-box"
        small
        layout="prev, pager, next"
        :total="50"
      >
      </el-pagination> -->
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import ProductDetail from "@/components/ProductDetail/ProductDetail";

import { getProductById } from "@/services/products";

export default {
  name: "ProductDetailPage",
  data() {
    return {
      productData: {},
      similarProduct: [],
      noDataImage: require("@/assets/No_Image_Available.jpg"),
    };
  },
  components: {
    HeaderComponent,
    ProductDetail,
  },
  methods: {
    async getProductDetail(id) {
      this.productData = await getProductById(id);
    },
  },
  mounted() {
    const productId = this.$route.path.split("/")[2];
    this.getProductDetail(productId);
  },
};
</script>

<style lang="scss" scoped>
.product-detail-page {
  background-color: $color-gray;
}

.product-similar {
  &-header {
    background-color: $color-white;
    text-align: start;
    padding: 24px;
    font-weight: bold;
  }
  padding: 24px 200px 0px 200px;
  &-body {
    padding: 24px;
    background-color: $color-white;
    display: flex;
    align-items: flex-start;

    // .title {
    //   font-size: 18px;
    //   padding: 24px;
    //   text-align: start;
    // }
  }
}
</style>
