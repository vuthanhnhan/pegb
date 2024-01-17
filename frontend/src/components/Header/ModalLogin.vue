<template>
  <div>
    <el-button v-if="!access_token" @click="() => isLogin = true" >Login</el-button>
    <el-popover
      v-else
      trigger="click">
      <el-button style="width: 100%;" @click="handleLogout">Logout</el-button>
    <el-button slot="reference">{{myInfo}}</el-button>
  </el-popover>
    <el-dialog :visible.sync="isLogin" class="container" width="25%">
        <el-button-group class="login-mode">
          <el-button @click="isNewUser = false">Login</el-button>
          <el-button @click="isNewUser = true">Register</el-button>
        </el-button-group>
        <div v-if="!isVerify">
          <div v-if="isNewUser" class="name">
            <el-input
              v-model="name"
              name="Name"
              autocomplete="firstName"
              placeholder="Name"
            />
          </div>
          <el-input
            v-model="email"
            type="email"
            placeholder="Email"
          />
          <el-input
            v-model="password"
            type="password"
            autocomplete="password"
            mode="normal"
            placeholder="Password"
          />
        </div>
        <el-input
          v-if="isVerify"
          v-model="otp"
          placeholder="otp"
        />
        <el-button
          @click="() => isVerify ? handleVerify() : isNewUser ? handleRegister() : handleLogin()"
          class="submit"
        >Continue</el-button>
    </el-dialog>
  </div>
</template>


<script>
import { login, register, verify } from '@/services/user'

export default {
  name: "ModalLogin",
  data() {
    return {
      isLogin: false,
      isNewUser: false,
      email: '',
      name: '',
      password: '',
      isRegister: false,
      access_token: localStorage.getItem("access_token"),
      isVerify: false,
      otp: ''
    }
  },
  computed: {
    wasLogin() {
      const access_token = localStorage.getItem("access_token")
      if (!access_token) return false
      return true
    },
    myInfo() {
      if (!this.access_token) return 'Login'
      return 'Welcome ' + JSON.parse(localStorage.getItem("me")).name
    }
  },
  methods: {
    async handleLogin() {
      this.access_token = await login(this.email, this.password)
      this.isLogin = false
    },
    async handleLogout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('me');
      this.access_token = undefined
    },
    async handleRegister() {
      await register(this.email, this.name, this.password)
      this.isVerify = true
    },
    async handleVerify() {
      await verify(this.email, this.otp)
      this.isVerify = false
      this.$message('Account verified')
    }

  }
}
</script>

<style lang="scss">
.container {

  .el-dialog__body {

    .login-mode {
      width: 100%;
    }

    div {
      display: block;
    }
  }
}
</style>