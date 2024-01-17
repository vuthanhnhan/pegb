<!-- eslint-disable vue/multi-word-component-names -->
<template>
<div>
  <button v-if="!isCartPage" class="product-item" style="width: 230px;" @click="handleAddToCart">
    <i class="el-icon-plus" style="margin-left: 50%;" ></i>
  </button>
  <div class="product-item" @click="onClickProductItem">
    <img v-if="imageSrc" class="product-image" :src="imageSrc" alt="" />
    <img
      v-else
      class="product-image"
      src="@/assets/No_Image_Available.jpg"
      alt=""
    />

    <div class="product-name">
      {{ productDataOverview.name }}
    </div>
    <div class="product-id">
      Id: {{ productDataOverview.id || productId }}
    </div>
    <div class="product-price">
      ${{ productDataOverview.price || productPrice }}
    </div>
    <div class="product-star">
      <el-rate v-model="overviewStar" :max="5"></el-rate>
    </div>
    <div class="product-quantity">
      Quantity: {{ productDataOverview.partnerItemQty || productQuantity }}
    </div>
    <div class="product-location">
      {{ productLocation }}
    </div>
  </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      overviewStar: this.productStar,
    };
  },
  props: {
    imageSrc: {
      type: String,
      default: "",
    },
    productName: {
      type: String,
      default:
        "",
    },
    productId: {
      type: String,
      default: "0",
    },
    productPrice: {
      type: String,
      default: "4.99",
    },
    productStar: {
      type: Number,
      default: 4.9,
    },
    productQuantity: {
      type: String,
      default: "16.2k",
    },
    productLocation: {
      type: String,
      default: "VN",
    },
    productDataOverview: {
      type: Object,
      default: () => {},
    },
    isCartPage: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    onClickProductItem() {
      const path = `/product/${this.productDataOverview.id}`;
      if (this.$route.path !== path) {
        this.$router.push(path);

        window.location.reload();
      }
    },
    handleAddToCart() {
      const currentCart = localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
      const found = currentCart.find(c => c.id == this.productDataOverview.id)
      if (found) {
        this.$message('Already in cart');
        return
      }
      currentCart.push(this.productDataOverview)
      localStorage.setItem('cart', JSON.stringify(currentCart))
      this.$message('Added to cart');
    }
  },
};
</script>

<style lang="scss">
.product-item {
  width: 220px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  text-align: start;
  padding: 5px;
  height: fit-content;
  transition: opacity 0.2s ease;

  &:hover {
    cursor: pointer;
    border: 1px solid $color-primary;
  }

  .product-image {
    width: 220px;
    height: 220px;
  }

  .product-name {
    word-wrap: break-word;
    white-space: normal;
    overflow: hidden;
    display: -webkit-box;
    text-overflow: ellipsis;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;

    margin: 5px;
  }

  .product-id {
    margin: 5px;
  }

  .product-price {
    font-size: 1rem;
    color: $color-primary;
    margin: 5px;
  }

  .product-star {
    margin: 5px;
  }

  .product-quantity {
    margin: 5px;
  }

  .product-location {
    margin: 5px;
  }
}
</style>