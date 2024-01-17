<template>
  <el-row class="header-component">
    <el-col :span="6" class="navbar__logo-box">
      <img
        src="https://www.pegb.tech/img/logo_white.svg?device=a0181b1e2089aab26466010ef3b1062d"
        alt=""
        class="navbar__logo"
        @click="onClickLogo"
      />
    </el-col>
    <el-col :span="6" class="navbar__menu-box">
      <ul class="el-menu el-menu--horizontal navbar__menu">
        <li class="el-menu-item">
          <router-link to="/">Home</router-link>
        </li>
        <li class="el-menu-item">
          <router-link to="/history">History</router-link>
        </li>
        <li class="el-menu-item">
          <router-link to="/cart">
            <img style="width: 50px;" src="https://cdn.pixabay.com/photo/2016/12/12/13/23/shopping-cart-1901584_640.png" />
          </router-link>
        </li>
        <li class="el-menu-item account-setting-box">
          <ModalLogin/>
        </li>
      </ul>
    </el-col>
  </el-row>
</template>

<script>
import ModalLogin from "./ModalLogin.vue";
export default {
  data() {
    return {
    };
  },
  props: {
    isShowSearchBar: {
      type: Boolean,
      default: true,
    },
  },
  components: {
    ModalLogin
},
  methods: {
    handleNavDropdownCommand: function (command) {
      if (command == "logout") {
        this.$confirm("Do you want to logout?", "Notification", {
          confirmButtonText: "Logout",
          cancelButtonText: "Cancel",
          type: "warning",
        }).then(
          function () {
            this.$message("Logout successfully");
          }.bind(this)
        );
      }
    },
    goTo(route) {
      this.$router.push({ name: route });
    },
    onClickLogo() {
      this.goTo("home");
    },
  },
};
</script>
<style lang="scss" scoped>
.header-component {
  padding: 10px 0;
  background: $color-header-background;
  display: flex;
  justify-content: space-between;
}

.navbar__logo-box {
  background-color: transparent;
}
.navbar__logo {
  display: block;
  height: 60px;
  margin-left: 48px;
  cursor: pointer;
  margin-right: 500px !important ;
}
.navbar_search-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 60px;
}
.navbar__menu-box {
  background-color: transparent;
}
.navbar__menu {
  display: flex;
  margin-left: auto;
  background-color: transparent;
  box-shadow: none;
  border-bottom: unset;
  margin-right: 28px;

  .el-menu-item {
    color: $color-white;

    &:hover {
      background-color: transparent;
      color: hsla(0, 0%, 100%, 0.7);
    }

    .account-setting {
      color: $color-white;
    }
  }
}

.account-setting-box {
  .account-setting {
    &:hover {
      color: hsla(0, 0%, 100%, 0.7);
    }
  }
}
.navbar__dropdown-menu a {
  color: inherit;
  text-decoration: none !important;
}
.navbar__title {
  margin-top: 0;
  margin-bottom: 0;
  margin-left: 12px;
  height: 60px;
  line-height: 60px;
  font-size: 1.5em;
  font-weight: bold;
}
.navbar__title a {
  color: #48576a;
  text-decoration: none !important;
}
.el-menu-item a {
  text-decoration: none !important;
}
</style>