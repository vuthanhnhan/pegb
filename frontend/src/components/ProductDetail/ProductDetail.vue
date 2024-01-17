<template>
  <div class="product-detail">
    <div class="product-detail-body">
      <div class="title">Product Specifications</div>
      <div @click="() => isEdit = !isEdit" style="float: right; width: 50px;"><i class="el-icon-edit"></i></div>
      <div class="content">
        <div class="content-row">
          <div class="col-1">Category</div>
          <div class="col-2">
          <!-- <el-breadcrumb-item :to="{ path: '/' }">Homepage</el-breadcrumb-item> -->
          <el-breadcrumb-item>{{ productName }}</el-breadcrumb-item>
          </div>
        </div>
        <div class="content-row">
          <div class="col-1">Stock</div>
          <div class="col-2">{{ quantity }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Price</div>
          <div v-if="!isEdit" class="col-2">{{ price }}</div>
          <input v-else class="col-2" v-model="newPrice">
        </div>
      </div>

      <div class="documentation">
        <div class="documentation-title">Product Documentation</div>
        <span style="margin: 30px;">Some documents...</span>
      </div>
      <div class="save-btn" v-if="isEdit">
          <el-button @click="handleUpdate">Save</el-button>
      </div>

    </div>
  </div>
</template>

<script>
import { updateProduct } from '@/services/products'
export default {
  props: {
    productName: {
      type: String,
      default: "Some category",
    },
    categoryName: {
      type: String,
      default: "Category",
    },
    quantity: {
      type: String,
      default: "21",
    },
    price: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      isEdit: false,
      newPrice: this.price
    }
  },
  methods: {
    async handleUpdate() {
      const productId = this.$route.path.split("/")[2];
      await updateProduct(productId, { price: this.newPrice })
      window.location.reload(true)
    }
  }
};
</script>

<style lang="scss">
.save-btn {
  margin-left: 50px;
  margin-top: 30px
}
.product-detail {
  padding: 24px 200px 100px 200px;

  &-body {
    background-color: $color-white;
    text-align: start;
    padding-bottom: 12px;

    .title {
      font-size: 18px;
      padding: 24px;
      text-align: start;
    }

    .content {
      &-row {
        display: grid;
        grid-template-columns: 10fr 25fr;
        padding: 12px 24px;

        .el-breadcrumb__item {
          font-size: 16px;
        }

        .col-1,
        .col-2 {
          text-align: left;
        }
      }
    }

    .documentation {
      padding-top: 24px;

      .documentation-title {
        font-size: 18px;
        margin-left: 24px;
        margin-right: 24px;
        padding-top: 24px;
        padding-bottom: 24px;

        border-top: 1px solid $color-border-tag;
      }

      .content {
        &-row {
          display: grid;
          grid-template-columns: 10fr 25fr;
          padding: 12px 24px;

          .el-breadcrumb__item {
            font-size: 16px;
          }

          .col-1,
          .col-2 {
            text-align: left;
          }
        }
      }
    }
  }
}
</style>